#-*- coding: utf-8 -*-
import sys

from eventClass import Team, Event, State
from eventHandler import evalState

# for unicode setting
reload(sys)
sys.setdefaultencoding('utf-8')

# need to be initialized
home_init_state = State() 
away_init_state = State()
event_lst = []

def evalGame(home_init_state, away_init_state, event_lst):
		
	
	res = [init_state] # need to evaluate init_state 
	
	for event in event_lst:
		res.append(evalState(event, res[-1]))
		
	return res
	
