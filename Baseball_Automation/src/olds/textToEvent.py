#-*- coding: utf-8 -*-
import os, sys, re
from eventClass import *
from eventHandler import *
from playerData import *


# for unicode setting
reload(sys)
sys.setdefaultencoding('utf-8')

EVENT_DIC = {"볼" : Ball, 
				"스트라이크" : Strike,
				"파울" : Foul,
				"헛스윙" : Swing,
				"hit" : Hitted,
				"walk" : None, #maybe safe? 
				"out" : Out,
				"score" : None, 
				"base_on_balls" : BaseOnBalls, 
				"change" : Change, 
				"pos_change" : None, #pitcherChange, FielderChange... 
				"deadball" : HitByPitch, 
				"homerun" : Homerun, 
				"baseonball_purpose" : None,
				"hit(probably_out)" : None, 
				"타석이탈" : None,
				"halt" : None,
				"delay" : None,
				"called_game" : None,
				"refree_injury" : None,
				"12second_rule" : None,
				"judge" : Strike,
				"expelled" : Strike,
				"error" : Strike,
				"warning" : None, 
				"fielder_select" : None, 
				"speedup" : None, # 스피드업 위반 
				"change_hitter" : ChangeHitter,
				"pinch_hitter" : PinchHitter,
				"team_change" : TeamChange,
				}
				
def getInitState(id):
	txt_path = "../res/texts/%s"%id[:8]
	raw_path = "../raw/texts/%s"%id[:8]
	
	txt = open(txt_path + "/%s.txt"%id, "r")
	raw = open(raw_path + "/%s.txt"%id, "r")
	
	lineup = []
	is_lineup = True
	
	hitter = txt.readlines()[1].split()[-1]
	
	for line in raw.readlines():
		line = line.strip()
		is_lineup = is_lineup and (line!= u"Start Relay Text")
		if is_lineup:
			lineup.append(unicode(line))
	
	
	ishome = True
	home_lineup = {}
	away_lineup = {}
	for elem in lineup:
		if elem.strip() == "Home":
			ishome = True 
		elif elem.strip() == "Away":
			ishome = False
		else:
			player, pos = elem.split(" - ")
			if ishome:
				home_lineup[pos] = player
			else:
				away_lineup[pos] = player
				
	#print home_lineup
	position_lst = [u"pitcher", u"catcher", u"b1man", u"b2man",  u"b3man", u"shotstop", u"leftfielder", u"centerfielder", u"rightfielder"]
	
	
	
	away_def_lst = [away_lineup[pos] for pos in position_lst]
	
	return State([hitter, None, None, None], 
					[away_lineup[pos] for pos in position_lst], 
					0,0,0,1,(0,0), True)
					
def parseLine(line):
	if line.startswith("Event"):
		return EVENT_DIC[line.split()[1].strip()]
		
def getEventLst(id):
	txt_path = "../res/texts/%s"%id[:8]
	txt = open(txt_path + "/%s.txt"%id, "r")
	res = []
	for line in txt.readlines():
		res.append(parseLine(line))
		
	return res

	
def simulateGame(id):
	print "parsing %s into events"%id
	event_lst = getEventLst(id)
	init_state = getInitState(id)
	
	res = [init_state]
	
	for event in event_lst:
		res.append(evalState(event, res[-1])) # need to care about teamchange 
	
	return res
		
	
	
	
	
if __name__ == "__main__":	
	simulateGame('20150319HTOB0')
	
	
