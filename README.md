# vgcomp
Vainglory Team Composition Generator

Uses Python Type Hints for readability

## INCOMPLETE.

## Setup
Assumes a working Python 3.5 Setup

### Usage
1. `git clone https://github.com/jaynagpaul/vgcomp`
2. `cd vgcomp`
3. `pip3 install -r requirements.txt`
4. `python run.py`

## How It Works
1. Start a spider to save matches from players in/above tier X playing ranked matches. **THIS HAS ALREADY BEEN DONE FOR YOUR CONVENIENCE.**
    Collect only for this patch.
    Stop after a reasonable amount of matches.

2. Calculate the "ELO" of each comp, by considering each comp as a separate player in traditional ELO.
    (Wins + Weight * Average Win % of All Comps) / (Wins + Losses + Weight)
    Ref: https://stackoverflow.com/a/7509441

3. Sort by "ELO

## Screenshots
**TODO**
