import gamelocker
from typing import List
from requests.exceptions import HTTPError
from datetime import timedelta, datetime
from . import utils
from .elo import appendToComps, totalWinRate
import os
import pickle
from progress.bar import IncrementalBar
import time

Match = gamelocker.datatypes.Match
regions = ['na', 'eu', 'sg', 'sa', 'cn']


def start(apikey: str, begin: datetime):
    api = gamelocker.Gamelocker(apikey).Vainglory()

    participants = []
    comps = []
    matchIDs = []

    bar = IncrementalBar('Collecting Starter Players', max=len(utils.START))
    for player in utils.START:
        matches = collectAllMatches(
            api, player["name"], player['region'], begin)

        for p in collectParticipants(matches):
            participants.append({"name": p, "region": player["region"]})

        for match in matches:
            if match.id not in matchIDs:
                comps = appendToComps(comps, match)
                matchIDs.append(match.id)

        bar.next()
    bar.finish()

    # Converts list of dicts to list of tuple and back to remove duplicates with set(l)
    participants = [dict(t) for t in set([tuple(d.items())
                                          for d in participants])]
    participants = participants[0:500]

    bar = IncrementalBar('Processing Additional Players',
                         max=len(participants))

    for p in participants:
        matches = collectAllMatches(api, p['name'], p['region'], begin)
        for m in matches:
            if m.id not in matchIDs:
                comps = appendToComps(comps, m)
                matchIDs.append(m.id)

        bar.next()

    bar.finish()

    winrate = totalWinRate(comps)

    with open(os.getcwd() + os.sep + 'comp.p', 'wb') as f:
        pickle.dump(
            {
                "comps": comps,
                "winrate": winrate
            }, f, protocol=pickle.HIGHEST_PROTOCOL
        )


def collectAllMatches(api: gamelocker.Gamelocker, player: str, region: str, begin: datetime) -> List[Match]:
    matches = []
    now = datetime.now()

    # API only allows requests within a 28 day time period
    if (now - begin).days <= 27:
        end = now
    else:
        end = begin + timedelta(days=27)

    while True:
        time.sleep(3)
        offset = 0
        # Collect all matches within that 28 day time period
        while True:
            try:
                m = api.matches(params={
                    "filter[playerNames]": player,
                    "page[offset]": str(offset),
                    "filter[createdAt-start]": toISO8601(begin),
                    "filter[createdAt-end]": toISO8601(end),
                    'filter[gameMode]': 'ranked'
                },
                    region=region)
                if len(m) >= 50:
                    matches.extend(m)
                    offset += 50
                else:
                    matches.extend(m)
                    break
            except HTTPError:
                break

        if now == end:
            # No more matches to fetch
            break

        # Choose a new time period
        # To avoid the off chance of an overlap
        begin = end + timedelta(minutes=1)

        if (now - end).days <= 27:
            end = now
        else:
            end = begin + timedelta(days=27)

    return matches


def toISO8601(date: datetime) -> str:
    return date.replace(microsecond=0).isoformat() + "Z"


def collectParticipants(matches: List[Match]) -> List[str]:
    participants = []
    for match in matches:
        for roster in match.rosters:
            for p in roster.participants:
                participants.append(p.player.name)

    # Get rid of duplicates
    return list(set(participants))
