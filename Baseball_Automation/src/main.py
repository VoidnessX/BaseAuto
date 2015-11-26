# -*- coding: utf-8 -*-
import datetime
from preference import Bias, Filter
from match import Match, load_matches


def write_articles_period(start_date, end_date, bias, filter):
    """Write articles according to the given query.
    :param start_date -- Only the matches from this day (inclusive) will be written as articles.
    :param end_date -- Only the matches until this day (inclusive) will be written as articles.
    :param bias -- Options affecting the event selection.
    :param filter -- Options used to filter out less significant matches.
    :return List of biased articles (each represented as a single string)
        about the significant matches (according to filter) in the given period.
    """
    # Type check.
    assert isinstance(start_date, datetime.date)
    assert isinstance(end_date, datetime.date)
    assert isinstance(bias, Bias)
    assert isinstance(filter, Filter)

    matches = load_matches(start_date, end_date)
    all_articles = [write_article(match, bias, filter) for match in matches]
    return filter(lambda x: x is not None, all_articles)


def write_article(match, bias, filter):
    """Write an article about the given match, according to the given preferences.
    :param match -- The match about which the article will be written.
    :param bias -- Options affecting the event selection.
    :param filter -- Options used to filter out less significant matches.
    :return A biased article (represented as a single string) about the match.
        If the match is insignificant according to filter, return None.
    """
    # Type check.
    assert isinstance(match, Match)
    assert isinstance(bias, Bias)
    assert isinstance(filter, Filter)

    return process_article(match, select_event(match, bias), filter)


# TODO
def select_event(match, bias):
    """Select the significant events that occurred in the match, according to the bias.
    :param match -- The match we will write an article about.
    :param bias -- Options affecting the event selection.
    :return List of events (in time order) that will be written in the generated article.
    """
    # Load the classifier based on the data before match.date.
    pass
    # Using the classifier, select the significant events.
    # default: return all the events
    return match.event_list


# TODO
def process_article(match, selected_list, filter):
    """Using the classified event list and filter, compute and return the actual article.
    match -- Whole unprocessed data of the match.
    selected_list -- List of significant(i.e. selected by the classifier) Events
    filter -- set of boolean flags used to determine if we should write an article for this match.

    return
    - None, if no article is written.
    - The news article, otherwise
    """
    pass
