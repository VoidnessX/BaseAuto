# -*- coding: utf-8 -*-


class Team:
    """A baseball team.
    Initialized when the process is initialized.
    For each team, exactly one Team instance exists during the entire life of the process.
    """

    def __init__(self, id, sponsor, name, home_stadiums):
        self.id = id  # An integer. Also used in the Database.
        self.sponsor = sponsor  # e.g. 삼성, 두산, SK
        self.name = name  # e.g. 라이온즈, 베어스, 와이번스
        self.home_stadiums = home_stadiums  # e.g. [사직 야구장, 울산 문수 야구장], [잠실 야구장]

    # TODO
    def load_stats(self, end_date):
        """Load the team stats, as of end_date, from the database.
        :param end_date: The end date of the sample period. (inclusive)
        :return (wins, losses, draws, streak, rank): streak > 0 means winning streak,
            streak < 0 means losing streak, and streak = 0 means no games played this season.
        """
        pass


teams = {}  # Dictionary of all baseball teams. Each team is represented by (name : Team object).


# TODO
def initialize_teams():
    # Load (from database? from a text file?) the team information into the dictionary 'teams'.
    pass

TEAM_LIST = {"LG 트윈스" : Team(0, "LG", "트윈스", "잠실"), 
        "두산 베어스" : Team(1, "두산", "베어스", "잠실"), 
        "KIA 타이거즈" : Team(2, "KIA", "타이거즈", "광주"), 
        "삼성 라이온즈" : Team(4, "삼성", "라이온즈", "대구"),
        "롯데 자이언츠" : Team(5, "롯데", "자이언츠", "부산"),
        "한화 이글스" : Team(6, "한화", "이글스", "대전"),
        "SK 와이번스" : Team(7, "SK", "와이번스", "인천"),
        "넥센 히어로즈" : Team(8, "넥센", "히어로즈", "목동"),
        "NC 다이노스" : Team(9, "NC", "다이노스", "마산"),
        "KT 위즈" : Team(10, "KT", "위즈", "수원"),
        }


# TODO
def get_team(name):
    """Get the Team object with the given name. (A simple lookup of the dictionary 'teams')
    :param name -- The name of the player.
    :return Team object representing the given team.
    """
    return TEAM_LIST[name]

def get_team_by_code(code):
    code_team_list = {"LG" : Team(0, "LG", "트윈스", "잠실"), 
        "OB" : Team(1, "두산", "베어스", "잠실"), 
        "HT" : Team(2, "KIA", "타이거즈", "광주"), 
        "SS" : Team(4, "삼성", "라이온즈", "대구"),
        "LT" : Team(5, "롯데", "자이언츠", "부산"),
        "HH" : Team(6, "한화", "이글스", "대전"),
        "SK" : Team(7, "SK", "와이번스", "인천"),
        "WO" : Team(8, "넥센", "히어로즈", "목동"),
        "NC" : Team(9, "NC", "다이노스", "마산"),
        "KT" : Team(10, "KT", "위즈", "수원"),
        }
    return code_team_list[code]

class Player:
    """A baseball player.
    Initialized when the process is initialized.
    For each player, there may exist several distinct Player objects.
    Note that,
    1. the name of the player may change during a season.
    2. there is no clear distinction between a hitter and a pitcher.
    """

    def __init__(self, id):
        self.id = id

    # TODO (Issue: Should we add more stats?)
    def load_hitter_stats(self, end_date):
        """Load the player stats as a hitter, as of end_date, from the database.
        :param end_date -- The end date of the sample period. (inclusive)
        :return (name, team, plate_appearances, at_bats, hits, walks, ): name is as of end_date.
        """
        pass

    # TODO (Issue: Should we add more stats?)
    def load_pitcher_stats(self, end_date):
        """Load the player stats as a pitcher, as of end_date, from the database.
        :param end_date -- The end date of the sample period. (inclusive)
        :return (name, team, out_counts, earned_run): 3 out_counts denotes 1 inning. earned_run: 자책점
        """
        pass


# TODO
def load_player_table(team, date):
    """From database, load the table of the given team, as of the given date.
    :param team -- Team object.
    :return Dictionary mapping the name of a player to the corresponding Player object.
    """
