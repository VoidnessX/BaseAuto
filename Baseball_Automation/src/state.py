# -*- coding: utf-8 -*-
"""
Classes used to simulate baseball games.
"""


class Position():
    """Defense position of a team."""

    def __init__(self, pitcher, catcher, baseman1, baseman2, baseman3,
                 shortstop, left_fielder, center_fielder, right_fielder):
        self.pitcher = pitcher
        self.catcher = catcher
        self.baseman1 = baseman1
        self.baseman2 = baseman2
        self.baseman3 = baseman3
        self.shortstop = shortstop
        self.left_fielder = left_fielder
        self.center_fielder = center_fielder
        self.right_fielder = right_fielder


POSITION_KR_TO_EN = {"투수": "pitcher", "포수": "catcher", "1루수": "baseman1", "2루수": "baseman2",
                     "3루수": "baseman3", "유격수": "shortstop", "좌익수": "left fielder",
                     "중견수": "center fielder", "우익수": "right fielder"}
POSITION_EN_TO_KR = {"pitcher": "투수", "catcher": "포수", "baseman1": "1루수", "baseman2": "2루수",
                     "baseman3": "3루수", "shortstop": "유격수", "left fielder": "좌익수",
                     "center fielder": "중견수", "right fielder": "우익수"}


# TODO (Issue: Should we replace assertions with appropriate error messages?)
class State():
    """A snapshot of a match."""

    def __init__(self, offense_team, defense_team,
                 offense_position, defense_position,
                 offense_score=0, defense_score=0,
                 inning=1, top=True, out_count=0,
                 hitter=None, runner1=None, runner2=None, runner3=None):
        self.offense_team = offense_team
        self.defense_team = defense_team
        self.offense_position = offense_position  # Defense position of the offending team.
        #for pos in offense_position:
        #  print pos + " : " + offense_position[pos]
        self.defense_position = defense_position  # Defense position of the defending team.
        self.offense_score = offense_score  # Score of the offending team.
        self.defense_score = defense_score  # Score of the defending team.
        self.inning = inning  # (e.g. 1, 2, 3, ...)
        self.top = top  # True if top, False if bottom.
        self.out_count = out_count
        self.hitter = hitter  # None when there is none.
        self.runner1 = runner1  # None when there is none.
        self.runner2 = runner2  # None when there is none.
        self.runner3 = runner3  # None when there is none.

    def switch(self):
        """Switch the roles.(공수 교대)
        Even when the out count hits 3, offense/defense will not be switched automatically.
        Call this method when a switch happens."""

        assert (self.out_count >= 3)

        # Switch offense/defense
        self.offense_team, self.defense_team = self.defense_team, self.offense_team
        self.offense_position, self.defense_position = self.defense_position, self.offense_position
        self.offense_score, self.defense_score = self.defense_score, self.offense_score

        # Half-inning update
        if self.top:
            top = False
        else:
            self.inning += 1
            top = True

        # Clear stats.
        self.out_count = 0
        self.hitter = None
        self.runner1 = None
        self.runner2 = None
        self.runner3 = None

    def enter_plate(self, next_hitter):
        """Start a new turn by placing a new hitter at the plate.(다음 타자가 타석에 선다)"""
        assert (self.hitter is None)
        self.hitter = next_hitter

    def run(self):
        """Score a run.(득점)"""
        self.offense_score += 1

    def out(self):
        """Increase an out count.(아웃)
        Clear the ball and strike counters."""
        self.out_count += 1

    def clear_plate(self):
        """End the turn of a hitter.(타자가 타석을 떠남)
        Called whenever a hitter leaves the plate."""
        self.hitter = None

    def change_defender(self, position_name, new_player):
        if position_name == "pitcher":
            self.defense_position.pitcher = new_player
        elif position_name == "catcher":
            self.defense_position.catcher = new_player
        elif position_name == "baseman1":
            self.defense_position.baseman1 = new_player
        elif position_name == "baseman2":
            self.defense_position.baseman2 = new_player
        elif position_name == "baseman3":
            self.defense_position.baseman3 = new_player
        elif position_name == "shortstop":
            self.defense_position.shortstop = new_player
        elif position_name == "left fielder":
            self.defense_position.left_fielder = new_player
        elif position_name == "center fielder":
            self.defense_position.center_fielder = new_player
        elif position_name == "right fielder":
            self.defense_position.right_fielder = new_player

    def change_runner1(self, new_player):
        assert (self.runner1 is not None)
        self.runner1 = new_player

    def change_runner2(self, new_player):
        assert (self.runner2 is not None)
        self.runner2 = new_player

    def change_runner3(self, new_player):
        assert (self.runner3 is not None)
        self.runner3 = new_player

    #def move(self, hitter_to, runner1_to, runner2_to, runner3_to):
    def move(self, lst):
        """Update the runners' positions.(타자와 주자의 위치 이동)
        Handle the resulting runs and outs. (득점과 아웃도 처리됨)
        Caller should guarantee that there is no conflict. (e.g. runner1 and runner2 both move to the third base.)
        :param hitter_to -- To where the hitter should move.
                0: still hitting (This hitter's turn is not over yet.)
                1, 2, 3: 1,2,3th base
                4: home
                -1: out.
        :param runner1_to -- To where the runner at the first base should move.
                0: doesn't care about runner1. (If there is no runner1, use 0)
                1, 2, 3, 4, -1: Same as above.
        :param runner2_to -- Similar to runner1_to.
        :param runner3_to -- Similar to runner1_to.
        """
        hitter_to = lst[0]
        runner1_to = lst[1]
        runner2_to = lst[2]
        runner3_to = lst[3]

        new_runner1 = None
        new_runner2 = None
        new_runner3 = None
        for (to, runner) in [(hitter_to, self.hitter), (runner1_to, self.runner1),
                             (runner2_to, self.runner2), (runner3_to, self.runner3)]:
            assert (to in [-1, 0, 1, 2, 3, 4])
            if to == 1:
                assert (new_runner1 is None)
                new_runner1 = runner
            elif to == 2:
                assert (new_runner2 is None)
                new_runner2 = runner
            elif to == 3:
                assert (new_runner3 is None)
                new_runner3 = runner
            elif to == 4:
                self.run()
            elif to == -1:
                self.out()

        if runner1_to == 0 and self.runner1 is not None:
            assert (new_runner1 is None)
            new_runner1 = runner
        if runner2_to == 0 and self.runner2 is not None:
            assert (new_runner2 is None)
            new_runner2 = runner
        if runner3_to == 0 and self.runner3 is not None:
            assert (new_runner1 is None)
            new_runner3 = runner

        # Update the hitter.
        if hitter_to is not 0:
            self.clear_plate()

        # Update the runners
        self.runner1, self.runner2, self.runner3 = new_runner1, new_runner2, new_runner3

    '''def walk(self):
        """The hitter walks to the first base.
        Whenever a conflict occurs, the runner at the base moves forward."""
        if self.runner1 is not None:
            if self.runner2 is not None:
                if self.runner3 is not None:
                    self.move(1, 2, 3, 4)
                else:
                    self.move(1, 2, 3, 0)
            else:
                self.move(1, 2, 0, 0)
        else:
            self.move(1, 0, 0, 0)'''

    def copy(self):
        """Return a copy of this state."""
        return State(self.offense_team, self.defense_team,
                     self.offense_position, self.defense_position, self.offense_score, self.defense_score,
                     self.inning, self.top, self.ball_count, self.strike_count, self.out_count,
                     self.hitter, self.runner1, self.runner2, self.runner3)
