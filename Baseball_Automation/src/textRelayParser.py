#-*- coding: utf-8 -*-
import os, sys, re
from state import *
from team_player import *
from playerData import *

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
				#id = elem.split("\\")[-1].split(".")[0]
				# modified by zeroOne
                                id = elem.split("/")[-1].split(".")[0]
				error.append((id, idx, line))
		f.close()
				
	return error
	

def parseText(id):
    # test.py에서 주루상황 체크하는중
    # 스트라이크 낫아웃의 경우도 잘 안되는듯
    # TODO : 이제는 event.py의 event들을 return 해야함
	raw_path = "../raw/texts/%s"%id[:8]
	res_path = "../res/texts/%s"%id[:8]
	#print "parsing %s"%id
	
	if not os.path.exists(res_path):
		os.makedirs(res_path)
		
	raw = open(raw_path + "/%s.txt"%id, "r")
	raw_temp = open(raw_path + "/%s.txt"%id, "r")
	res = open(res_path + "/%s.txt"%id, "w+")

        #####################################################################
        ## crawler에서 gameInfo 정보도 받아오므로 그에 따른 parser도 필요 ###
        ## 일단  무시하게 함 ################################################
        # match 클래스 meta Data 채울떄 새로 받은 데이터 사용 ###############
        #####################################################################
	
	lineup = []
	game = [[]]

	# wirte game info
	is_lineup = True
	for line in raw_temp.readlines():
		line = line.strip()
		if line == "Start Relay Text":
			is_lineup = False
		if is_lineup:
			res.write(line+'\n')
			print line

	is_lineup = False
	for line in raw.readlines():
		line = line.strip()
		#is_lineup = is_lineup and (line!= u"Start Relay Text")
		if line == "Start Relay Text":
			is_lineup = False
		if is_lineup:
			lineup.append(unicode(line))
		else:
			if line.endswith(u"종료"):
				game.append([])
			else:
				game[-1].append(unicode(line))
				if line == "LineUp":
					is_lineup = True


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
	position_lst = [u"pitcher", u"catcher", u"b1man", u"b2man",  u"b3man", u"shotstop", u"leftfielder", u"centerfielder", u"rightfielder"]
	#position_lst = [u"지명타자", u"포수", u"1루수", u"2루수",  u"3루수", u"유격수", u"좌익수", u"중견수", u"우익수"]

        home = id[10:12]
        away = id[8:10]

        """
	print "-------------------------"
	for pos in position_lst:
		print pos + " : " + home_lineup[pos]
	print "-------------------------"
	for pos in position_lst:
		print pos + " : " + away_lineup[pos]
        """
	
        #1120
	# home team attack first
	init_state = State(get_team_by_code(home), get_team_by_code(away), home_lineup, away_lineup, 0, 0, 1, True, 0, None, None, None, None)
	
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
	
	for turn, name, event in hitter_event:
		new_turn = turn != tmp
		if new_turn:
			if turn%2 == 0:
				if turn != 0:
					res.write(u"Event team_change : away -> home \n\n")
				res.write(u"%d회 초\n"%(turn/2+1)) # comment out when checking error
			else:
				if turn != 0:
					res.write(u"Event team_change : home -> away \n\n")
				res.write(u"%d회 말\n"%(turn/2+1)) # comment out when checking error
			
			tmp = turn
		
		
		if ":" in name: # pinch hitter
			old, new = name.split(":")
			old_pit = old.split()[-1]
			new_pit = new.split(u" (으)")[0].split()[-1]
			res.write("%s\n\n"%old) # comment out when checking error
			res.write("Event pinch_hitter : %s to %s\n"%(old_pit, new_pit))
		else: 
			pass
			name = name.split()[-1]
			res.write(u"Event change_hitter %s\n\n"%name) # comment out when checking error
		name = name.split()[-1]
		for e in event:
			# ball, strike, hit, ... 
			if re.match(u"^- [0-9]+구 ", e): 
				event_name = e.split()[-1]
				if event_name != u"타격":
					res.write("Event %s by %s\n"%(event_name, name))
			else:
				#------------------------------------------------------------------------------------------
				# parse line to event -> need to be changed to real Class Event! 
				#------------------------------------------------------------------------------------------
				if ":" in e: # need to check 2 cases : homerun, time
					# these regexp need to be checked
					#time_pattern = re.complie(r"[0-9]{2}:[0-9]{2}")
					#homerun_pattern = re.compile(u"홈런거리 : ")
					player, ev = e.split(":")[:2]
					player = player.split()[-1]
					
					# switch-case for each event 
					# If in ev case, well formalized. 
					if ev.endswith(u"루타"):
						res.write("Event hit : %s루타 by %s"%(ev[-3], name))
					elif u"아웃" in ev:
						res.write("Event out : %s out"%player)
					elif u"진루" in ev:
						res.write("Event walk : %s walk"%player)
					elif u"홈인" in ev:
						res.write("Event score : %s to home"%player)
					elif u"볼넷" in ev:
						res.write("Event base_on_balls : %s bob"%player)
					elif u"교체" in ev:
						new_player = ev.split(" (으)")[0].split()[-1]
						res.write("Event change : %s to %s"%(player, new_player))
					elif u"변경" in ev:
						new_pos = ev.split("(으)")[0]
						res.write("Event pos_change : %s to pos %s"%(player, new_pos))
					elif u"출루" in ev: 
						res.write("Event walk : %s walk"%player)
					elif u"몸에 맞는 볼" in ev:
						res.write("Event deadball : %s"%player)
					elif u"홈런" in ev:
						res.write("Event homerun : %s"%player)
					elif u"고의4구" in ev:
						res.write("Event baseonball_purpose : %s"%player)
					elif u"안타" in ev:
						res.write("Event hit(probably_out) : %s"%player)
					elif u"타석이탈" in e: # This event was not covered
						res.write(u"Event 타석이탈 : %s"%player)
					elif u"중단" in e or u"경기중단" in e:
						res.write("Event halt : %s"%e)
					elif u"지연" in e:
						res.write("Event delay : %s"%e)
					elif u"콜드" in e:
						res.write("Event call_edgame : %s"%e)
					elif u"주심부상" in e or u"주심 부상" in e :
						res.write("Event refree_injury : %s"%e)
					elif u"12" in e: # This event was not covered
						res.write("Event 12second_rule : %s"%player)
					elif u"합의판정" in e:	
						res.write("Event judge : %s"%e)
					elif u"퇴장" in e:
						res.write("Event expelled : %s"%e)
					elif u"실책" in e:
						res.write("Event error : %s"%e)
					elif u"야수선택" in e:
						res.write("Event fielder_select : %s"%ev)
					else: # should not happen
						res.write(e) # event type specified
				else: # event type unspecified
					if u"12초" in e:
						res.write("Event 12second rule violate : %s"%e)
					elif u"10초" in e:
						res.write("Event rule violate : %s"%e)
					elif u"퇴장" in e:
						res.write("Event expelled : %s"%e)
					elif u"경고" in e:
						res.write("Event warning :%s"%e)
					elif u"실책" in e:
						res.write("Event error : %s"%e)
					elif u"합의" in e:	
						res.write("Event judge : %s"%e)
					elif u"중단" in e or u"경기중단" in e:
						res.write("Event halt : %s"%e)
					elif u"타석이탈" in e or u"타석 이탈": # This event was not covered
						res.write(u"Event 타석이탈 : %s"%e)
					elif "2분" in e or "스피드업" in e:
						res.write(u"Event speedup : %s"%e)
					
					else: #this should not happen
						res.write("n" + e)
				res.write("\n")
				#------------------------------------------------------------------------------------------
						
					
		res.write("\n")
			
			
		
	raw.close()
	raw_temp.close()
	res.close()
	
	
	
if __name__ == "__main__":	
	raw_path = "../raw/texts/"
	res_path = "../res/texts/"
	
	#for id in getIdLst(raw_path):
	#	parseText(id)
	
	
	#parseText('20150731LGSK0')
	parseText('20150319HTOB0')
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
