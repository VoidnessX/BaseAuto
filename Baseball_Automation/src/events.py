# -*- coding: utf-8 -*-
from state import State


class PlateAppearance:
    """
    - inning: (int, boolean)
    - hitter: Player
    - pitcher: Player
    - runs: int
    - outs: int
    - name: string

    hit
    - multiplicity: 1, 2, 3, 4(home run)
    - bunt: boolean
    - pinch hitter: boolean
    - location: string (optional)
    - range: string (optional)
    - error: (Player, string)

    base on ball
    - intentional (boolean)

    hit by pitch

    hit out
    - sacrifice: boolean
    - hit type: string (fly, ground ball, bunt)
    - defender

    strikeout
    - pitcher
    - hitter

    non hit walk
    - kind: string (wild pitch, steal out, pick off)
    - runner Player

    non hit out
    - kind: string (wild pitch, steal out, pick off)
    - runner: Player


    """
    def __init__(self, before, hitter_to, runner1_to, runner2_to, runner3_to, info):
        self.before = before
        # Compute the state after this event.
        self.after = before.copy()
        self.after.move(hitter_to, runner1_to, runner2_to, runner3_to)
        # Additional information
        self.info = info