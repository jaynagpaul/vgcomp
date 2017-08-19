from typing import List
from gamelocker.datatypes import Match
from .utils import convHero


class Comp:
    """
    Each comp as a seperate player in traditional ELO
    """

    def __init__(self, heroes: List[str], wins: int, losses: int):
        self.heroes = heroes
        self.wins = wins
        self.losses = losses

    def elo(self, totalwinrate: float, weight: float) -> float:
        # Detailed(ish) explanation in README

        wins = self.wins
        losses = self.losses

        return (wins + weight * totalwinrate) / (wins + losses + weight)

    def addGame(self, result: bool):
        if result:
            self.wins += 1
        else:
            self.losses += 1

    @property
    def winrate(self):
        # to convert to percentage and truncate at the hundredths
        return int(100 * self.wins / (self.wins + self.losses)) / 100


def totalWinRate(comps: List[Comp]) -> float:
    wins = 0
    losses = 0

    for c in comps:
        wins += c.wins
        losses += c.losses

    return int(100 * wins / (wins + losses)) / 100


def appendToComps(comps: List[Comp], m: Match) -> List[Comp]:
    for roster in m.rosters:
        heroes = []
        for p in roster.participants:
            heroes.append(convHero(p.actor))

        comp = [c for c in comps if sorted(c.heroes) == sorted(heroes)]

        didWin = roster.participants[0].stats['winner']
        # Comp exists in list
        if len(comp) > 0:
            comp = comp[0]
            comp.addGame(
                didWin
            )
        else:
            if didWin:
                comps.append(Comp(heroes, 1, 0))
            else:
                comps.append(Comp(heroes, 0, 1))
    return comps
