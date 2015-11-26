#-*- coding: utf-8 -*-
import sys
from datetime import date

# for unicode setting
reload(sys)
sys.setdefaultencoding('utf-8')
'''
class Player : wrapper class for player
	name, birthday, salary : basic information of player.
	id_number : id in our system. 
	position : positions that player have played. 
	career : list of tuple (class Team, from_date, when_date). 
'''
class Player():
	def __init__(self, name, career, position, id_number): 
		self.name = name
		self.career = career
		self.position = position
		self.id_number = id_number
	
	# for now, done manually. (7/18)
	def updateCareer(self):
		pass
		
	def updateId(self, id):
		self.id_number = id
		
	'''
	getCurrentTeam : datetime.date -> class Team
		return team of the player in specified date
		date : given date
	'''
	def getCurrentTeam(self, date):
		for team, start, end in self.career:
			if start < date and date <= end:
				return team
		
		
def makePlayerLst(team_name, date):
	res = []
	for player in playerLst:
		if player.getCurrentTeam(date == team_name):
			res.append(player)
	return res
			

		
		
n = 0
PLAYER_LIST = [Player(u"안지만", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"백정현", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"차우찬", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"클로이드", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"피가로", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"저마노", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"임현준", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"임진우", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"장필준", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"장원삼", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"조현근", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"정인욱", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"김현우", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"김동호", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"김건한", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"김기태", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"김재우", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"김성한", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"권오준", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"임창용", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"노진용", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"박근홍", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"박민규", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"박종철", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"박재윤", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"서동환", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"심창민", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"신용운", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"윤석환", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"윤대경", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"진갑용", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"정민우", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"김희석", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"이정식", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"이흥련", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"이지성", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"이용재", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"박근용", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"백상원", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"차화준", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"채태인", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"최정용", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"조동찬", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"김성표", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"김태완", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"김상수", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"김정혁", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"김재현", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"구자욱", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"권용철", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"이승엽", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"나바로", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"박계범", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"박석민", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"윤영수", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"최민구", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"최선호", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"최형우", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"허승민", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"강봉규", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"김기환", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"이창원", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"이상훈", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"이용욱", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"문선엽", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"나광남", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"박한이", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"박찬도", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"박해민", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"송준석", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"우동균", [(u"삼성", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 

# player in NC
Player(u"배재환", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"최금강", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"해커", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"임정호", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"힘창민", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"강장산", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"김학성", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"김진성", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"고창성", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"구창모", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"이우석", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"이호중", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"이혜천", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"이훈", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"이민호", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"이승호", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"이재학", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"이대환", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"이태양", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), # same name
Player(u"민성기", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"문수호", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"문석종", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"노성호", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"박민석", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"박명환", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"박진우", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"류진욱", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"찰리", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"손민한", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"손정욱", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"스튜어트", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"원종현", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"윤형배", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"윤강민", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 


Player(u"정성민", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"김태군", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"김지호", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"이승재", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"박광열", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"박세웅", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), # same name
Player(u"용덕한", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), # trade between season
Player(u"홍지은", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"황윤호", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"지석훈", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"조평호", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"조용훈", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"강민국", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"김태진", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"이창섭", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"이호준", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"모창민", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"노진혁", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"박민우", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"손시헌", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"테임즈", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"유용준", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"최재원", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"김성욱", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"김준완", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"김종호", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"이종욱", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"마낙길", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"나성범", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"박으뜸", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"박정준", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 
Player(u"윤병호", [(u"NC", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), 

# Doosan

Player(u"변진수", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"채지선", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"최병욱", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"함덕주", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"한주성", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"허준혁", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"임태훈", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"장원준", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"장민익", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"전용훈", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"진야곱", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"조승수", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"정은재", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"강동연", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"김강률", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"김명성", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"김수완", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"이용호", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), #same name
Player(u"이정호", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), #same name
Player(u"이현호", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"이현승", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"이원재", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"이재우", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"마야", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"남경호", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"니퍼트", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"노경은", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"오현택", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"박성민", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"박종기", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"성영훈", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"스와잭", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"양현", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"유창준", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"윤명준", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 
Player(u"유희관", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), 

Player(u"최재훈", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"장승현", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"김응민", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"박종욱", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"양의지", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"최영진", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"최주환", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"최형록", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"허경민", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"홍성흔", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"정진철", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"김강", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"김재환", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"김재호", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"고영민", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"루츠", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"문진재", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"오재일", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"오장훈", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"오재원", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"로메로", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"류지혁", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"양종민", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"유민상", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"장민석", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"정수빈", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"정진호", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"김현수", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"김진형", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"구명환", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"국해성", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"민병헌", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"박건우", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"사공엽", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"윤태수", [(u"두산", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),



# Nexen


Player(u"배힘찬", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"최원태", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"피어밴드", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"하영민", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"한현희", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"조덕길", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"조상우", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"정용준", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"정재복", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"정회찬", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"금민철", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"김동준", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"김대우", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"김정훈", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"김택형", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"김해수", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"김영민", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"구자형", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"권택형", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"이상민", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"이정훈", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"마정길", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"문성현", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"오재영", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"박병훈", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"박성훈", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"박주현", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"신명수", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"손승락", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"송신영", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"밴헤켄", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n),
Player(u"양훈", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "pitcher", n), # trade

Player(u"임태준", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"정종수", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"김재현", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), # same name
Player(u"박동원", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"유선정", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"안태영", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"백승룡", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"임병욱", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"임동휘", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"장시윤", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"장용석", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"김지수", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"김민성", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"김하성", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"박병호", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"서동욱", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"서건창", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"송성문", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"윤석민", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n), # same name
Player(u"허정협", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"홍성갑", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"강지광", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"김민준", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"고종욱", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"이택근", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"문우람", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"박헌도", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"박정음", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"스나이더", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"송우현", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"유한준", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
Player(u"유재신", [(u"넥센", date(2014, 1, 1), date(2015, 12, 12))], "fielder", n),
]

for player in PLAYER_LIST:
	player.updateId(n)
	n += 1
	
# same team, same name players should be considered 
def findPlayer(team_name, player_name):
	for player in PLAYER_LIST:
		if player.name == player_name and player.getcurrentTeam(datetime.date.today()) == team_name:
			return player
	
	
