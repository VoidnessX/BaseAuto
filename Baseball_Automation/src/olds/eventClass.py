#-*- coding: utf-8 -*-
import os, sys, re
import datetime
from playerData import Player, PLAYER_LIST

# for unicode setting
reload(sys)
sys.setdefaultencoding('utf-8')



#---------------------------------------------------------------
# Class Definitions
#---------------------------------------------------------------


'''
class Team : wrapper class for team 
	official_name, names : official/possible name for the team.
	number : our identification.
	player_list : player in the team for specified date.
	record : nothing for now.
	home : home stadium
'''	
class Team():
	def __init__(self, official_name, names, number, home): 
		self.official_name = official_name
		self.names = names
		self.number = number
		self.player_lst = []
		self.record = ""
		self.home = home
	'''
	constructPlayerList : listof players  date -> listof players
		construct player list for team in specified date
		date : specified date. default today. 
	'''
	def constructPlayerList(self, date=datetime.date.today()):
		res = []
		for player in PLAYER_LIST:
			for team, start, end in player.career:
				#print team
				#print self.official_name
				if team == self.official_name and start < date and date <= end: # might need some debugging comparing date
					res.append(player)
					print player
			
		self.player_lst = res
		
'''
class OffenseTeam : wrapper function for team in offense state. 
	position : dictionary of {position_name : class Player}
	is_home : if offense team is home team in game, True. else False.
'''
class OffenseTeam():
	def __init__(self, player_lst):
		self.position = {"hitter" : None, "b1runner" : None, "b2runner" : None, "b3runner" : None} 
		self.is_home = True
	
		self.position["hitter"] = player_lst[0]
		self.position["b1runner"] = player_lst[1]
		self.position["b2runner"] = player_lst[2]
		self.position["b3runner"] = player_lst[3]
	
	def setTeam(self, bool):
		self.is_home = bool
		
	def getPlayerLst(self):
		return [player for pos, player in self.position.items()]
			
	
'''
class DefenseTeam : wrapper function for team in defense state. 
	position : dictionary of {position_name : class Player}
	is_home : if defense team is home team in game, True. else False.
'''
class DefenseTeam():
	def __init__(self, player_lst):
		position_lst = ["pitcher", "catcher", "b1man", "b2man",  "b3man", "shotstop", "leftfielder", "centerfielder", "rightfielder"]
		self.position = {}
		for elem in position_lst: 
			self.position.update({elem : None})
		self.is_home = True
		
		self.position["pitcher"] = player_lst[0]
		self.position["catcher"] = player_lst[1]
		self.position["b1man"] = player_lst[2]
		self.position["b2man"] = player_lst[3]
		self.position["b3man"] = player_lst[4]
		self.position["shotstop"] = player_lst[5]
		self.position["leftfielder"] = player_lst[6]
		self.position["centerfielder"] = player_lst[7]
		self.position["rightfielder"] = player_lst[8]
		
	def setTeam(self, bool):
		self.isHome = bool
	
	def getPlayerLst(self):
		return [player for pos, player in self.position.items()]
	
'''
class State : a snapshot of baseball game.
	offense_team : class OffenseTeam.
	offense_team : class DefenseTeam.
	xx_cnt : xx count. ball, out, 
	is_home : if True, home team is offense. 
	score : tuple of (home_score, away_score)
'''
class State():
	def __init__(self, offense_lst, defense_lst, ball, out, strike, turn, score, bool):
		self.offense_team = OffenseTeam(offense_lst)
		self.defense_team = DefenseTeam(defense_lst)
		self.ball = ball
		self.out = out
		self.strike = strike
		self.turn = turn
		self.score = score
		self.is_home = bool
	
	
'''
class OffenseResult : wrapper class for result of offense state after any change.
	hitter, b1runner, b2runner, b3runner : where does player go. n -> nth base, 4 -> home in, -1 -> out.
'''
class OffenseResult():
	def __init__(self, hitter, b1runner, b2runner, b3runner):
		self.hitter = hitter
		self.b1runner = b1runner
		self.b2runner = b2runner
		self.b3runner = b3runner
	
	def getResultLst(self):
		return [self.hitter, self.b1runner, self.b2runner, self.b3runner]
		
	'''
	evalOffenseTeam : class OffenseTeam, class OffenseResult -> class OffenseTeam
		evaluate offense team state with offense result and original offense team state.
		evalOffenseTeam : OffenseResult, OffenseTeam -> OffenseTeam
		before : before event happen
	'''
	def evalOffenseTeam(self, before):
		player_lst = [None, None, None, None]
		ind_lst = [self.hitter, self.b1runner, self.b2runner, self.b3runner]
		elem_lst = [elem[1] for elem in before.position.items()]
		
		for i in range(len(ind_lst)):
			ind = ind_lst[i]
			elem = elem_lst[i]
			if ind != -1 or ind!=4:
				player_lst[ind]=elem
		
		res = OffenseTeam(player_lst)
		res.setTeam(before.isHome)
		return res
	
	def evalScore(self):
		res = 0
		for elem in self.getResultLst():
			if elem==4:
				res += 1
		return res

	def evalOutCnt(self):
		res = 0
		for elem in self.getResultLst():
			if elem == -1:
				res += 1
		return res
		
'''
class Event : class for whole event. Every event inherits this class.
	before : state before event 
	after : state after event
	offense_result : result of offense
'''
class Event():
	def __init__(self, before, after, event_name, offense_result):
		self.offense_result = offense_result
		self.before = before
		self.after = after
		self.event_name = event_name
			
# Each event classes need no explanation. 
# If explanation needed, refer to the documentation event table. 
class Hitted(Event):
	def __init__(self, before, after, offense_result):
		Event.__init__(self, before, after, "hitted", offense_result)

class Fair(Hitted):
	def __init__(self, before, after, offense_result):
		Hitted.__init__(before, after, offense_result)
		self.event_name += "\nhitted"
		
class Foul(Hitted):
	def __init__(self, before, after, offense_result):
		Hitted.__init__(self, before, after,  offense_result)
		self.event_name += "\nfoul"
		
class Hit(Fair):
	def __init__(self, before, after, offense_result):
		Fair.__init__(self, before, after, offense_result)
		self.event_name += "\nhit"

class Single(Hit):
	def __init__(self, before, after, offense_result):
		Hit.__init__(self, before, after, offense_result)
		self.event_name += "\nsingle"

class Double(Hit):
	def __init__(self, before, after, offense_result):
		Hit.__init__(self, before, after, offense_result)
		self.event_name += "\ndouble"
		
class Triple(Hit):
	def __init__(self, before, after, offense_result):
		Hit.__init__(self, before, after, offense_result)
		self.event_name += "\ntriple"

class Homerun(Hit):
	def __init__(self, before, after, offense_result):
		Hit.__init__(self, before, after, offense_result)
		self.event_name += "\nhomerun"

class Error(Hit):
	def __init__(self, sub_event, before, after, offense_result):
		# sub_event : Should be one of Event class children. 
		# when error does not exist, this event should happen. 
		self.sub_event = sub_event
		self.event_name += "\nerror"
		Hit.__init__(self, before, after, offense_result)
	
class Out(Fair):
	def __init__(self, before, after, offense_result):
		Fair.__init__(self, before, after, offense_result)
		self.event_name += "\nout"
		
class SingleOut(Out):
	def __init__(self, before, after, offense_result):
		Out.__init__(self, before, after, offense_result)
		self.event_name += "\nsingleout"

class DoublePlay(Out):
	def __init__(self, before, after, offense_result):
		Out.__init__(self, before, after, offense_result)
		self.event_name += "\ndoubleplay"
		
class TriplePlay(Out):
	def __init__(self, before, after, offense_result):
		Out.__init__(self, before, after, offense_result)
		self.event_name += "\ntripleplay"

class SacrificeFly(Out):
	def __init__(self, before, after, offense_result):
		Out.__init__(self, before, after, offense_result)
		self.event_name += "\nsacrificeplay"
		
class SacrificeBunt(Out):
	def __init__(self, before, after, offense_result):
		Out.__init__(self, before, after, offense_result)
		self.event_name += "\nsacrificebunt"

class NonHitted(Event):
	def __init__(self, before, after, offense_result):
		Event.__init__(self, before, after, "nonthitted", offense_result)

class Strike(NonHitted):
	def __init__(self, before, after, offense_result):
		NonHitted.__init__(self, before, after, offense_result)
		self.event_name += "\nstrike"

class Swing(Strike):
	def __init__(self, before, after, offense_result):
		Strike.__init__(self, before, after, offense_result)
		self.event_name += "\nswing"

class StrikeOut(Strike):
	def __init__(self, before, after, offense_result):
		Strike.__init__(self, before, after, offense_result)
		self.event_name += "\nstrikeout"

class Ball(NonHitted):
	def __init__(self, before, after, offense_result):
		NonHitted.__init__(self, before, after, offense_result)
		self.event_name += "\nball"
		
class WildPitch(Ball):
	def __init__(self, before, after, offense_result):
		Ball.__init__(self, before, after, offense_result)
		self.event_name += "\nwildpitch"
		
class HitByPitch(Ball):
	def __init__(self, before, after, offense_result):
		Ball.__init__(self, before, after, offense_result)
		self.event_name += "\nhitbypitch"
		
class BaseOnBalls(Ball):
	def __init__(self, before, after, offense_result):
		Ball.__init__(self, before, after, offense_result)
		self.event_name += "\nbaseonballs"

class Steal(Event):
	def __init__(self, before, after, offense_result):
		Event.__init__(self, before, after, "steal", offense_result)
		

class Safe(Steal):
	def __init__(self, before, after, offense_result):
		Steal.__init__(self, before, after, offense_result)
		self.event_name += "\nsafe"

class CaughtStealing(Steal):
	def __init__(self, before, after, offense_result):
		Steal.__init__(self, before, after, offense_result)
		self.event_name += "\ncaughtsteal"

class DoubleSteal(Steal):
	def __init__(self, before, after, offense_result):
		Steal.__init__(self, before, after, offense_result)
		self.event_name += "\ndoublesteal"

class Balk(Event):
	def __init__(self, before, after, offense_result):
		Event.__init__(self, before, after, "balk",  offense_result)
		
class Change(Event):
	def __init__(self, before, after, offense_result):
		Event.__init__(self, before, after, "change",  offense_result)
	
class PinchHitter(Change):
	def __init__(self, pinch_hitter, before, after, offense_result):
		Change.__init__(self, before, after,  offense_result)
		self.event_name += "\npinchhitter"
		
class PinchRunner(Change):
	def __init__(self, pinch_runner, base, before, after, offense_result):
		self.pinch_runner = pinch_runner
		self.pinch_runner_base = base
		Change.__init__(self, before, after,  offense_result)
		self.event_name += "\npinchrunner"
			
		
class PitcherChange(Change):
	def __init__(self, bullpen, before, after, offense_result):
		self.bullpen_picther = bullpen
		Change.__init__(self, before, after,  offense_result)
		self.event_name += "\npitcherChange"
		
class FielderChange(Change):
	def __init__(self, new_fielder, pos, before, after, offense_result):
		self.new_fielder = new_fielder
		self.change_position = pos
		Change.__init__(self, before, after,  offense_result)
		self.event_name += "\nfielderchange"
		
class Penalty(Change):
	def __init__(self, penalty_player, penalty_position, before, after, offense_result):
		self.penalty_player = penalty_player
		self.penalty_position = penalty_position
		Change.__init__(self, before, after,  offense_result)
		self.event_name += "\npenalty"
		
class BenchClear(Event):
	def __init__(self, before, after, offense_result):
		Event.__init__(self, before, after, "benchclear", offense_result)
		
class TeamChange(Event):
	def __init__(self, before, after, offense_result):
		Event.__init__(self, before, after, "teamchange", offense_result)
		
class ChangeHitter(Event):
	def __init__(self, before, after, offense_result):
		Event.__init__(self, before, after, "hitterChange", offense_result)
	
#---------------------------------------------------------------
# evalState function - code in eventHandler.py
#---------------------------------------------------------------


'''
Common for event handler functions
	
handler_func : Event State (might have more inputs) -> State 
	all handler_func is for evaluating next state. 
	event : class Event. 
	before : class State for state before event happens.
	res : state after event happens.
'''

'''
Few notes about implementation

- Next hitter issue
Note that all hitter change is done by event pinchHitter or hitterChange, so before_state for other classes should already have next hitter before actuall event happens.
- Score evaluation issue
No exact calculation on score is now available. Need to be implemented. Escpecially when score is made in case of teamChange, it should be handled carefully.  
- teamChange issue
teamChange function requires state of each team. Therefore, inside the function, initial OffenseTeam/DefenseTeam should be saved for both home and away team. When players change with team change, this should be handled with teamChange function plus necessary playerChange functions. 
- event duplication
singlehit, doublehit, ... have duplicate function implementation. 
'''


'''
def singleHit(event, before): 
	offense_before = before.offense_team
	offense_after = event.offense_result.evalOffenseTeam(offense_before)
	defense_after = before.defense_team
	ball_after = before.ball
	out_after = event.offense_result.evalOutCnt() + before.out
	strike_after = before.strike
	turn_after = before.turn
	score_after = before.score
	# divide case - if home is offense/away is offense
	if before.is_home == True: # if home is offense
		score_after[0] += event.offense_result.evalScore()
	else: # if away is offense
		score_after[1] += event.offense_result.evalScore() 
	is_home_after = before.is_home
	
	return State(offense_after.getPlayerLst(), 
				 defense_after.getPlayerLst(),
				 ball_after, 
				 out_after, 
				 strike_after, 
				 turn_after, 
				 score_after, 
				 is_home_after)

# implementation should be same as singleHit				 
def doubleHit(event, before):
	pass
	
# implementation should be same as singleHit
def tripleHit(event, before):
	pass
	
	
# implementation should be same as singleHit	
def homerun(event, before):
	pass



# implementation should be same as singleHit
# might need slight modification
def error(event, before):
	pass
	
# implementation should be same as singleHit
def foul(event, before):
	pass
	
# it is also very similar to singleHit... should be checked.	
def singleOut(event, before):
	offense_before = before.offense_team
	offense_after = event.offense_result.evalOffenseTeam(offense_before)
	defense_after = before.defense_team
	ball_after = before.ball
	
	# should be handled in case of more than 3 out
	out_after = event.offense_result.evalOutCnt() + before.out 
	
	strike_after = before.strike
	turn_after = before.turn
	score_after = before.score
	# divide case - if home is offense/away is offense
	if before.is_home == True: # if home is offense
		score_after[0] += event.offense_result.evalScore()
	else: # if away is offense
		score_after[1] += event.offense_result.evalScore() 
	is_home_after = before.is_home
	
	return State(offense_after.getPlayerLst(), 
				 defense_after.getPlayerLst(),
				 ball_after, 
				 out_after, 
				 strike_after, 
				 turn_after, 
				 score_after, 
				 is_home_after)
	
def doublePlay(event, before):
	pass
def triplePlay(event, before):
	pass
def sacrificeFly(event, before):
	pass
def sacrificeBunt(event, before):
	pass
	
def swing(event, before):
	pass
def strikeOut(event, before):
	pass

	
def wildPitch(event, before):
	pass
def hitByPitch(event, before):
	pass
def baseOnBalls(event, before):
	pass
def safe(event, before):
	pass
def caughtSteal(event, before):
	pass
def doubleSteal(event, before):
	pass
def balk(event, before):
	pass

# handlers for player change of any sort
	
def pinchHitter(event, before_state):
	pass
def pinchRunner(event, before_state):
	pass
def pitcherChange(event, before_state):
	pass
def fielderChange(event, before_state):
	pass
def teamChange(event, before_state):
	pass
def hitterChange(event, before):	
	pass

# handlers for exceptional cases	
def benchClear(event, before_state):
	pass
def penalty(event, before_state):
	pass
def benchChange(event, before_state):
	pass
def hitInference(event, before_state):
	pass
	
# handler functions end 

		
def evalState(event, before_state):
	func_dict = {"single" : singleHit, 
				 "double" : doubleHit, 
				 "triple" : tripleHit, 
				 "homerun" : homerun, 
				 "error" : error, 
				 "foul" : foul, 
				 "singleout" : singleOut, 
				 "doubleplay" : doublePlay, 
				 "tripleplay" : triplePlay, 
				 "sacrificebunt" : sacrificeBunt, 
				 "sacrificefly" : sacrificeFly, 
				 "swing" : swing, 
				 "strikeout" : strikeOut, 
				 "wildpitch" : wildPitch, 
				 "hitbypicth" : hitByPitch, 
				 "baseonballs" : baseOnBalls, 
				 "safe" : safe, 
				 "caughtsteal" : caughtSteal, 
				 "doubleSteal" : doubleSteal, 
				 "balk" : balk, 
				 "pinchhitter" : pinchHitter, 
				 "pinchRunner" : pinchRunner, 
				 "pitcherchange" : pitcherChange, 
				 "fielderchange" : fielderChange, 
				 "benchclear" : benchClear, 
				 "penalty" : penalty, 
				 "teamchange" : teamChange, 
				 "benchchange" : benchChange, # class not implemented
				 "hitinference" : hitInference, # class not implemented
				 "hitterchange" : hitterChange, # class not implemented
				}
	
	
	return FUNC_DICT[event.event_name.split("\n")[-1]](event, before_state)
	
	'''
	
	