import sys
import crayons
from . import spider
from datetime import datetime, timedelta
import pickle
import os
from .utils import convHero

WEIGHT = 5


def cli():
    if len(sys.argv) == 1:
        print("""
        VGComp

        Get a team composition that works with a hero you choose.
        
        Usage: %s
        """ % crayons.red('python run.py taka'))
        sys.exit()

    if len(sys.argv) == 2:
        with open("{}{}comp.p".format(os.path.dirname(os.path.realpath(__file__)), os.sep), 'rb') as f:
            data = pickle.load(f)
        num = 0
        while True:
            try:
                out = formatData(data, num)
                print(out)

                if out == 'No more comps.':
                    sys.exit()

                ans = input("Next? (y/n)")

                if ans.lower() == 'n':
                    sys.exit()
                elif ans.lower() == 'y':
                    num += 1
                print(ans.lower(), num)
            except (IndexError, KeyboardInterrupt) as e:
                # Check for ctrl+c
                if e is KeyboardInterrupt:
                    sys.exit()
                else:
                    print(e)

                sys.exit()
    if len(sys.argv) == 4 and sys.argv[1].lower() == 'spider':
        print(crayons.cyan('Starting the spider.'))
        spider.start(sys.argv[2], datetime.now() - timedelta(days=sys.argv[3]))
        print(crayons.cyan('Finished the spider.'))
        sys.exit()


def formatData(data: dict, num: int) -> str:
    comps = data['comps']
    totalwinrate = data['winrate']

    hero = convHero(sys.argv[1])

    # Compositions including the hero.
    possibleComps = []
    for comp in comps:
        if hero in comp.heroes:
            possibleComps.append(comp)

    possibleComps = sorted(
        possibleComps, key=lambda k: k.elo(totalwinrate, WEIGHT), reverse=True)

    if len(possibleComps) == 0:
        raise IndexError(
            "Couldn't find anything for %s. Maybe the data collected hasn't been update for the patch." % hero)
    if len(possibleComps) < num:
        return "No more comps."
    heroes = [h.capitalize() for h in possibleComps[num].heroes]
    heroesStr = ", ".join(heroes)

    return "VGComp recommends %s.\nIt has a score of %f" % (crayons.cyan(heroesStr), possibleComps[num].elo(totalwinrate, WEIGHT))
