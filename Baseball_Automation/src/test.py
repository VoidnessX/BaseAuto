#-*- coding: utf-8 -*-
import os, sys, re, urllib
from bs4 import BeautifulSoup as bs
from state import *
from playerData import *
from team_player import *
from selenium import webdriver
import selenium 

# for unicode setting
reload(sys)
sys.setdefaultencoding('utf-8')


'''
THIS CODE NEEDS IMPROVEMENT ON EVENT HANDLING PART.
'''

def getIdLst(raw_path):
	res = []
	for date in os.listdir(raw_path):
		date_path = os.path.join(raw_path, date)
		if os.path.isdir(date_path):
			res.extend([elem.split(".")[0] for elem in os.listdir(date_path)])
		
	return res
	
def checkText(res_path):
	error = []
	res = []
	for date in os.listdir(res_path):
		date_path = os.path.join(res_path, date)
		if os.path.isdir(date_path):
			res.extend([os.path.join(date_path, elem) for elem in os.listdir(date_path)])
			
	for elem in res:
		f = open(elem, "r")
		for idx, line in enumerate(f.readlines()):
			line = line.strip()
			if line == "" or line.startswith("Event"):
				pass
			else:
				id = elem.split("\\")[-1].split(".")[0]
				error.append((id, idx, line))
		f.close()
				
	return error

'''
test function for parseText 
only for offenseResult list
'''
def getScore(id):
	lst = parseText(id)
	current_turn = 0
	
	home_score = 0 
	away_score = 0
	for turn, event in lst:		
		if turn%2 == 0:
			if event == "Score":
				away_score += 1
			elif event == "HomeRun":
				away_score += 1
		else:
			if event == "Score":
				home_score += 1
			elif event == "HomeRun":
				away_score += 1
	#print away_score, home_score
	return away_score, home_score
	
def scoreTest(id, browser):
	url = "http://sports.news.naver.com/gameCenter/gameResult.nhn?category=kbo&gameId=" + id
	#print url
	while True:
		try:
			browser.get(url)
			away = browser.find_element_by_id('away_total_score').text.replace(" ","") 
			home = browser.find_element_by_id('home_total_score').text.replace(" ","") 
			#print id, away, home
			return int(away), int(home)
		except selenium.common.exceptions.NoSuchElementException:
			pass
			
		
		
	
	
def parseId(id):
	date = id[:8]
	away = id[8:10]
	home = id[10:12]
	print date, away, home
	
def updateOffenseResult(tmp_res):
	#-------------------------------------------------------------------
	# highly likely to have error 
	#-------------------------------------------------------------------
	# refresh res_tmp 
	
	# should handle unknown cases 

	temp = [0,0,0,0]
	
	# check for strike-notout case
	upper_bound = 1
	if tmp_res[0] == -2: # if the hitter's next base is unknown
		for idx, elem in enumerate(tmp_res):
			if elem != 0 and idx > 0:
				upper_bound = max(idx, elem)
				break
			if tmp_res == [-2,0,0,0]:
				temp = [0,-2,-2,-2]
	
			for i in range(1, upper_bound):
				temp[i] = -2
			
			
			
	
					

	for elem in tmp_res:
		if elem in [1,2,3]:
			temp[elem] = elem # move to appropriate base 

	return temp
	#-------------------------------------------------------------------
def push(lst): 
	for idx, elem in enumerate(lst):
		if idx == elem:
			lst[idx] = elem + 1
		else:
			return


def parseText(id):
	"""parse text relay and return list of state
	"""
	state_list = []
	event_list = []
	metadata = {}
	current_state = None
	res_val = [] #
	raw_path = "../raw/texts/%s"%id[:8]
	res_path = "../res/texts/%s"%id[:8]
	#print "parsing %s"%id
	
	if not os.path.exists(res_path):
		os.makedirs(res_path)
		
	raw = open(raw_path + "/%s.txt"%id, "r")
	res = open(res_path + "/%s.txt"%id, "w+")
	
	lineup = []
	game = [[]]
	is_lineup = True
	for line in raw.readlines():
		line = line.strip()
		is_lineup = is_lineup and (line!= u"Start Relay Text")
		if is_lineup:
			lineup.append(unicode(line))
		else:
			if line.endswith(u"종료"):
				game.append([])
			else:
				game[-1].append(unicode(line))
				
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
				
	away = id[8:10]
	home = id[10:12]
   
		
	position_lst = [u"pitcher", u"catcher", u"b1man", u"b2man",  u"b3man", u"shotstop", u"leftfielder", u"centerfielder", u"rightfielder"]
		

	init_state = State(get_team_by_code(away),
					   get_team_by_code(home),
					   away_lineup, 
					   home_lineup, 
					   0, # offense score
					   0, # defense score
					   0, False, # inning
					   3, # outcount
					   None, None, None, None)
	
	current_state = init_state
	
	
	
	
	
	
	for elem in game:
		elem.reverse()
	
	hitter_event = []
	tmp = []
	for idx, turn in enumerate(game[-1:0:-1]):
		for elem in turn:
			if re.match(u"^[1-9]+[번타자]", elem):
				hitter_event.append((idx, elem , tmp)) 
				tmp = []
			else:
				tmp.append(elem)
				
			
	
	
	new_turn = True
	tmp = -1
	tmp_off_res = [0,0,0,0] # containing offense_result
	is_strknot = False # if true, strike notout 
	base_state_lst = []
	problem = False # flag for strike_notout existence
	
	for turn, name, event in hitter_event:
		new_turn = turn != tmp
		if new_turn:
			current_state.switch()
			#current_state.format()
			#print current_state.inning
			print turn/2 + 1, turn%2
			tmp_off_res = [0,0,0,0]
			tmp = turn
		
		current_hitter = None
		if ":" in name: # pinch hitter
			old, new = name.split(":")
			old_pit = old.split()[-1]
			new_pit = new.split(u" (으)")[0].split()[-1]
			
			current_state.enter_plate(new_pit) # added now
			current_hitter = new_pit 
		else: 
			name = name.split()[-1]

			current_state.enter_plate(name) # added now
			
			#print name
			current_hitter = name
		
		

		
		
		tmp_flag_for_test = False
		tmp_off_res = updateOffenseResult(tmp_off_res)
		for e in event:
			
			
			# ball, strike, hit, ... 
			
			if re.match(u"^- [0-9]+구 ", e): 
				
				if tmp_flag_for_test:
					pass
				else:
					print 
					tmp_flag_for_test = True
			
			else:
				print e
				
				tmp_flag_for_test = False
				#------------------------------------------------------------------------------------------
				# parse line to event -> need to be changed to real Class Event! 
				#------------------------------------------------------------------------------------------
				if ":" in e: # need to check 2 cases : homerun, time
					
					player, ev = e.split(":")[:2]
					player = player.split()[-1]
					
					
					if ev.endswith(u"루타"):
						tmp_off_res[0] = int(ev[-3])
						
					elif u"아웃" in ev:
						current_state.out()
						if u"스트라이크 낫" in ev:
							# NEED TO BE DEBUGGED
							tmp_off_res[0] = -1
						elif u"도루실패아웃" in ev:
							runner_from = int(e[0])
							
							tmp_off_res[runner_from] = 0
							current_state.out()
						elif e[0] in ['1', '2', '3']: #runnerout
							runner_from = int(e[0])
							tmp_off_res[runner_from] = -1
						
							
						else:
							tmp_off_res[0] = -1	
							
					elif u"진루" in ev:
						if u"도루" in ev:
							runner_from = int(e[0])
							runner_to = int(ev.split()[1][0])
							tmp_off_res[runner_from] = 0
							tmp_off_res[runner_to] = runner_to
						elif u"보크" in ev:
							runner_from = int(e[0])
							runner_to = int(ev.split()[1][0])
							tmp_off_res[runner_from] = 0
							tmp_off_res[runner_to] = runner_to
						elif u"폭투" in ev:
							runner_from = int(e[0])
							runner_to = int(ev.split()[1][0])
							tmp_off_res[runner_from] = 0
							tmp_off_res[runner_to] = runner_to
				
						else:
							try:
								tmp_off_res[int(e[0])] = int(ev.strip()[0])
							except UnicodeEncodeError, ValueError:
								tmp_off_res[int(e[0])] = int(ev[ev.index(u"루까")-1])
							
					elif u"홈인" in ev:
						tmp_off_res[int(e[0])] = 4
						
					elif u"볼넷" in ev:
						push(tmp_off_res)
					elif u"교체" in ev:
						new_player = ev.split(" (으)")[0].split()[-1]
						
					elif u"변경" in ev:
						new_pos = ev.split("(으)")[0]
						
					elif u"출루" in ev: 
						push(tmp_off_res)
					elif u"몸에 맞는 볼" in ev:
						push(tmp_off_res)
					elif u"홈런" in ev:
						tmp_off_res[0] = 4
						for idx, elem in enumerate(tmp_off_res):
							if elem != 0:
								tmp_off_res[idx] = 4
						
					elif u"고의4구" in ev:
						push(tmp_off_res)
					elif u"안타" in ev:
						# might have error here 
						for idx, elem in enumerate(tmp_off_res):
							if idx == elem:
								tmp_off_res[idx] = elem + 1
							else:
								break
					elif u"타석이탈" in e: # This event was not covered
						pass
					elif u"중단" in e or u"경기중단" in e:
						pass
					elif u"지연" in e:
						pass
					elif u"콜드" in e:
						pass
					elif u"주심부상" in e or u"주심 부상" in e :
						pass
					elif u"12" in e: # This event was not covered
						pass
					elif u"합의판정" in e:	
						pass
					elif u"퇴장" in e:
						pass
					elif u"실책" in e:
						pass
					elif u"야수선택" in e:
						pass
					else: # should not happen
						print "error 1" # event type specified
				else: # event type unspecified
					if u"12초" in e:
						pass
					elif u"10초" in e:
						pass
					elif u"퇴장" in e:
						pass
					elif u"경고" in e:
						pass
					elif u"실책" in e:
						pass
					elif u"합의" in e:	
						pass # need to be parsed exceptionally 
					elif u"중단" in e or u"경기중단" in e:
						pass
					elif u"타석이탈" in e or u"타석 이탈": # This event was not covered
						pass
					elif "2분" in e or "스피드업" in e:
						pass
					
					else: #this should not happen
						print "error 2"

		print tmp_off_res
		current_state.move(tmp_off_res)
		
	raw.close()
	res.close()
	
	
if __name__ == "__main__":	
	raw_path = "../raw/texts/"
	res_path = "../res/texts/"
	
	'''
	for id in getIdLst(raw_path):
		parseText(id)
	'''
	
	'''
	# test code
	browser = webdriver.Chrome()
	right = 0
	wrong = 0
	wrong_lst = []
	for id in getIdLst(raw_path):
		away, home = getScore(id) 
		away_t, home_t = scoreTest(id, browser)
		if away == away_t and home == home_t:
			right += 1
		else:
			wrong += 1
			wrong_lst.append(id)
	browser.quit()
			
	print right, wrong
	print wrong_lst
	'''
	
	
	
	
	# for unit test
	id = '20150319SKKT0'
	
	parseText(id)
	
	

		
		
		
	'''
	#------------------------------------------------------------------------------------------
	# for checking error
	
	error = open(os.path.join(res_path, "errors.txt"), "w+")
	for id, idx, line in checkText(res_path):
		
		error.write( "Error in %s line %d\n"%(id, idx))
		
		error.write(line + "\n")
	error.close()
		
	
	print len(checkText(res_path))
	#------------------------------------------------------------------------------------------
	'''
	
	
	
	
	# wrong_lst = ['20150307KTWO0', '20150308KTWO0', '20150311LGLT0', '20150312OBHH0', '20150313HTWO0', '20150313LGSS0', '20150315SKSS0', '20150320SKKT0', '20150321HTKT0', '20150328LGHT0', '20150402OBHH0', '20150403SSLG0', '20150407WOOB0', '20150408KTSK0', '20150412HHLT0', '20150416WOSK0', '20150418LTOB0', '20150421HHLG0', '20150423SKKT0', '20150425SKHH0', '20150428NCSK0', '20150430LTWO0', '20150430NCSK0', '20150501NCKT0', '20150502NCKT0', '20150505SSWO0', '20150508LGKT0', '20150510HHOB0', '20150514HHSS0', '20150516LTKT0', '20150520HHSK0', '20150521HHSK0', '20150522LGLT0', '20150522SKOB0', '20150523NCWO0', '20150524NCWO0', '20150526LTSK0', '20150527WOSS0', '20150528WOSS0', '20150529SSLG0', '20150530NCHT0', '20150531NCHT0', '20150531OBKT0']

	
	
	
	
