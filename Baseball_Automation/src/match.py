# -*- coding: utf-8 -*-
import state


class Match:
    """A single match.
    Contains all information about the match.
    The sequence of states are computed immediately after the match data is crawled.
    After that, all the information including the sequence of states is saved in the database,
    so that we don't need to compute them again.
    """

    def __init__(self, date, home_team, away_team, event_list, metadata):
        """
        :param date:
        :param home_team: Team object
        :param away_team: Team object
        :param event_list:
        :param metadata:
            {"result": (home score: int, away score: int),
             "winner": winning team: Team, None if draw,
             "home start pitcher": {"pitcher": Player, "strikeout": int, "lost": int, "pitches": int, "innings": int},
             "away start pitcher": (same as above),
             "leading team": List of (Team, int),
             "rank change": ((int, int), (int, int)),
             "box score": *load from KBO*,
             "number of innings": int,
             "home team player list": List of strings
             "away team player list": List of strings}
        """
        self.date = date
        self.home_team = home_team
        self.away_team = away_team
        self.event_list = event_list
        self.metadata = metadata


# TODO
def record_to_match(file_name):
    """Read a text record of a match, and make it into a Match object.
    This function is where all the simulations are done."""

    # Open file_name
    pass

    # Read the date, home team, away team, stadium, and the winner
    date = None
    home_team = None
    away_team = None
    stadium = None
    winner = None

    # Read the player entry, and construct the initial state
    pass

    event_list = []
    # for each event, construct an event object, and append it to event_list.
    pass

    # Close file_name
    pass

    return Match(date, home_team, away_team, stadium, winner, event_list)


# TODO
def save_match(match):
    """Save a match information to the database."""
    pass


# TODO
def load_matches(start_date, end_date):
    """Load the list of matches played during the given period. (from database)
    :param start_date -- The start date of the sample period. (inclusive)
    :param end_date -- The end date of the sample period. (inclusive)
    :return: List consisting of the matches played during the given period, in time order.
    """
    pass
