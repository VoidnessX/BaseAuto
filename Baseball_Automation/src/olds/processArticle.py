#-*- coding: utf-8 -*-
import os, sys
import re 
import datetime

#from leagueData import LGList, DSList, KIAList, SSList, LTList, HWList, SKList, NXList, NCList, KTList
from leagueData import *
#import leagueData

# for unicode setting
reload(sys)
sys.setdefaultencoding('utf-8')


'''
Baseball ontology 

Season
- duration

- seasonRecord

- matches
-- home
-- away
-- matchRecord

- team
-- number
-- name
-- homeGround
-- playedSeasons
--- seasonRecord
---- matchRecord
-- player
--- name
--- position
--- playerRecord
---- playerSeasonRecord
----- playerMatchRecord
'''


#---------------------------------------------------------------
# auxiliary function
#---------------------------------------------------------------

def getKey(dic, value):
	res = u"unspecified"
	for key in dic.keys():
		for word in dic[key]:
			if word in value: 
				res = key
			
	return res

def getItem(dic):
	res = []
	for (key, val) in dic.items():
		res.extend(val)
		
	return res
	


#---------------------------------------------------------------
# auxiliary classes
#---------------------------------------------------------------


'''
class BallRecord : record class for one ball/unit event. 
				   player change, ball hit, catch, home run, etc.... 
	homePlayerList, awayPlayerList : player list for the ball.
	turnNo : No of turn. For normal game, should be <9.
	record : string for describing what happend in the ball.
			 specified in the method ParseString().
'''
class BallRecord():
	def __init__(self, homePlayerList, awayPlayerList, turnNo, initial_state, record):
		self.homePlayerList = homePlayerList
		self.awayPlayerList = awayPlayerList
		self.turnNo = turnNo
		self.record = record
		self.initial_state = initial_state
		
	# parse the self.record to update 
	# 1. player's record
	# 2. team's record (both home and away)
	def parseRecord(self):
		'''
		parseString should follow grammar specified here;
		ParseSrting = chg from to 
					| hit num 
					| hr 
					| foul
					| stk 
					| ball
		'''
		pass
		
# record class for the match. 		
class Record():
	def __init__(self, homePlayerList, awayPlayerList, ballList, record):
		self.homePlayerList = homePlayerList
		self.awayPlayerList = awaylayerList
		self.ballList = ballList
		self.record = record
	
	# update Record for all balls when ballList is updated
	def updateRecord(self):
		for ball in ballList:
			ball.parseRecord()

#---------------------------------------------------------------
# Main classes for ontology
#---------------------------------------------------------------

'''
class Season
	teamList : list of class Team in the season.
	matchList : list of class Match in the season.
	duration : tuple of date (start, end).
	seasonRecord : for now, N/A.
'''
class Season():
	def __init__(self, teamList, duration, matchList, record):
		self.teamList = teamList
		self.duration = duration
		self.matchList = matchList
		self.seasonRecord = record
		
'''
class Match
	home, away : class Team for home, away.
	date : date for the match .
	recordList : list of class BallRecord for record for 
				 each ball in the game. 
	isCanceled : if canceled, true. 
'''
class Match():
	def __init__(self, home, away, date, ballList):
		self.home = home
		self.away = away
		self.date = date
		self.recordList = ballList
		self.isCanceled = False 
		
	def setCanceled(self):
		self.isCanceled = True

	def __unicode__(self):
		return self.home + " : " + self.away + " at " + self.date 

		
'''
class Team
	official_name : official name of the team. 
	names : contain list of possible names. 
	number : should be assigned a unique integer. 
	playerList : list of class Player for player in the team.
'''
class Team():
	def __init__(self, official_name, names, number, playerList, home): 
		self.official_name = official_name
		self.names = names
		self.number = number
		self.playerList = playerList
		self.record = ""
		self.homeGround = home
'''
class Player
	team should contain team name. 
	number should be assigned a integer. 
	position should be one of 투수, 포수, 내야수, 외야수. 
	hundreds(and maybe thousands) should be a integer for team number
	ones and tens are for player identification.

class Player():
	def __init__(self, team, name, position, number): 
		self.team = team
		self.name = name 
		self.position = position
		self.number = number
		self.record = ""
'''
		
# -------------------------------------------------------------
# Global variables
# These SHOULD NOT BE ASSIGNED OTHER VALUE
# -------------------------------------------------------------


# player list for whole league. 
#PLAYERLIST = leagueData.LGList + leagueData.DSList + leagueData.KIAList + leagueData.SSList + leagueData.LTList + leagueData.HWList + leagueData.SKList + leagueData.NXList + leagueData.NCList + leagueData.KTList
PLAYERLIST = LGList + DSList + KIAList + SSList + LTList + HWList + SKList + NXList + NCList + KTList

print len(PLAYERLIST)

# team list for league
TEAMLIST = [
	Team(u"LG 트윈스", [u"LG", u"트윈스", u"LG 트윈스"], 1, LGList, [u"잠실야구장", u"잠실", u"잠실구장",]),
	Team(u"두산 베어스", [u"두산 베어스", u"베어스", u"두산"], 2, DSList, [u"잠실야구장", u"잠실", u"잠실구장"]),
	Team(u"KIA 타이거즈", [u"KIA 타이거즈", u"KIA", u"기아"], 3, KIAList, [u"무등야구장", u"무등", u"광주", u"무등구장"]),
	Team(u"삼성 라이온즈", [u"삼성 라이온즈", u"삼성", u"라이온즈"], 4, SSList, [u"시민야구장", u"시민구장", u"대구"]),
	Team(u"롯데 자이언츠", [u"롯데 자이언츠", u"롯데", u"자이언츠"], 5, LTList, [u"사직야구장", u"사직", u"사직구장", u"부산"]),
	Team(u"한화 이글스", [u"한화 이글스", u"한화", u"이글스"], 6, HWList, [u"한밭야구장", u"대전", u"한밭구장"]),
	Team(u"SK 와이번스", [u"SK 와이번스", u"SK", u"와이번스"], 7, SKList,  [u"문학야구장", u"문학",  u"문학구장"]),
	Team(u"넥센 히어로즈", [u"넥센 히어로즈", u"넥센", u"히어로즈"], 8, NXList,  [u"목동야구장", u"목동구장", u"목동"]),
	Team(u"NC 다이노스", [u"NC 다이노스", u"NC", u"다이노스"], 9, NCList, [u"마산야구장", u"마산", u"마산구장"]),
	Team(u"KT 위즈", [u"KT 위즈", u"KT", u"위즈", u"kt"], 10, KTList,  [u"수원야구장", u"수원", u"수원구장"] ),
]

EVENTDICT = {
	u"winlose" : [u"승리", u"패배", u"패전", u"승전"],
	u"offensive" : [u"홈런", u"안타", u"적시타", u"번트", u"파울"], 
	u"defensive" : [u"삼진", u"사구", u"고의사구", u"아웃", u"스트라이크", u"볼넷"],
	u"mistake" : [u"병살", u"폭투", u"난조"],
}

		
TAGDICT = {
	u"player" : [player.name for player in PLAYERLIST], 
	u"team" : [name  for team in TEAMLIST for name in team.names ], 
	u"event" : getItem(EVENTDICT), 
	u"stadium" : [stadiums for team in TEAMLIST for stadiums in team.homeGround],
	u"league" : [u"KBO", u"메이저리그", u"한국야구위원회"],
	u"position" : [u"타자", u"피쳐", u"투수", u"포수", u"유격수", u"내야수", u"외야수", u"1루수", u"2루수", u"3루수", u"대주자", u"대타자", u"대타"],
	u"place" : [u"1루", u"2루", u"3루", u"홈", u"베이스", u"외야", u"내야", u"벤치", u"관중석"],
	u"time" : [u"1회초", u"2회초", u"3회초", u"4회초", u"5회초", u"6회초", u"7회초", u"8회초", u"9회초", u"연장",
				u"1회말", u"2회말", u"3회말", u"4회말", u"5회말", u"6회말", u"7회말", u"8회말", u"9회말", 
				u"1회", u"2회", u"3회", u"4회", u"5회", u"6회", u"7회", u"8회", u"9회", ],
	u"score" : ["%d-%d"%(homeScore, awayScore) for homeScore in range(30) 
												for awayScore in range(30)],
	#u"date" : dateList,
}

# -------------------------------------------------------------


def tagSentence(sent):
	return [(w, getKey(TAGDICT, w)) for w in sent.split()]

#if TAGDICT[u"player"] 
#for word, tag in tagSentence(u"장성우 최대성, 하준호. 롯데 자이언츠가 세대교체 주역으로 꼽아오던 선수들이다"):
#	print word.decode('utf-8'), tag 



'''
wrapper class for saving articles in class Article and save it as file. file->class function and class->file function need to be implemented.  

class Article should have following attributes; 
- article id : for identification. 
- news provider : company for providing the news
- news writer : who writes the article 
- date : when was the article published 
- content : main content of the article
- title : title that the author gave to the article

Article files should be saved in the directory articles/date/
'''

class Article():
	def __init__(self, id, provider, author, date, content, title):
		self.id = id
		self.provider = provider
		self.author = author
		self.date = date
		self.content = content
		self.title = title 
		
	def saveArticle(self, path):
		tmp = open(path, "w+")
		tmp.write("Id : " + self.id +  "\n")
		tmp.write("Title : " + self.title +  "\n")
		tmp.write("Date : " + self.date +  "\n")
		tmp.write("Provider : " + self.provider +  "\n")
		tmp.write("Author : " + self.author + "\n")
		tmp.write(self.content)
		tmp.close()
		
# getArticle : path -> class Article			
def getArticle(filePath):
	art = open(filePath, "r")
		
	id = art.readline().split(" : ")[1]
	title = art.readline().split(" : ")[1]
	date = art.readline().split(" : ")[1]
	provider = art.readline().split(" : ")[1]
	author = art.readline().split(" : ")[1]
	
	content = ""
	for line in art.readlines():
		content += line
	
	art.close()
	return Article(id, provider, author, date, content, title)

	
#---------------------------------------------------------------

'''
Process article class by doing

- tag article paragraphs
- get specific words
- make a database and put them in database
- neatly print them 

Finally making a corpora related to the baseball ontology. 
For further analysis, article writing can be done by using corpora made here. 
'''

# process : path -> class Article -> string
# processes article 

# -------------------------------------------------------------
# values and functions for tagging
# -------------------------------------------------------------


class Event():
	def __init__(self, tag, playerLst):
		self.tag = tag
		self.playerList = playerLst
		if tag in tagList[u"offensive"]:
			self.attribute = u"offense"
		elif tag in tagList[u"defensive"]:
			self.attribute = u"defense"
	def __unicode__(self):
		return self.tag
	
	
'''
process article in path 
'''
def process(path):
	res = u""
	
	# path -> article
	article = getArticle(path)
	
	
	#article -> string process
	id = article.id
	provider = article.provider
	author = article.author
	date = article.date
	title = article.title 
	
	# get basic information 
	res = "title : %s \n id : %s \n provider : %s \n author : %s \n date : %s \n" %(title, id, provider, author, date)
	
	# get content
	content = article.content
	
	# split sentences(sentence segmentation)
	raw_sents = content.split(".") 
	sents = []
	
	# exception handling for split(".")
	for idx, sent in enumerate(raw_sents): 
		if idx == 0:
			sents.append(sent)
		elif sent == "" or raw_sents[idx-1] == "":
			pass
		else:
			# for number ex)1.2 
			def isNumber(str):
				num = re.compile('[0-9]')
				return num.match(str)
			# for url ex) www.xxx.com
			def isWWW(str): 
				return str.endswith('www')
			def isCom(str):
				return str.startswith('com')
			# additional exceptions should be handled
			# need to be added... 
			
			def isError(str):
				return isNumber(str) or isWWW(str) or isCom(str)  
			
			if(isError(raw_sents[idx-1][-1]) and isError(sent[0])):
				sents[-1]+= "." + sent
			else:
				sents.append(sent)
	# segmentation finished
		
		
	# variables for essential information 
	stadium = ""
	homeTeam = 0
	awayTeam = 0
	winner = 0
	loser = 0
	score = [0,0]
	
	# variables for additional information
	
	
	for sent in sents: 
		# sentence tagging 
		res = u"%s\n" %(res)
		tagged_sent = tagSentence(sent)
		dic = dict()
		
		for w,t in tagged_sent: 
			if t in dic.keys():
				dic[t].append(w)
			else: 
				dic.update({t : [w]})
		res = u"%s \n %s \n" %(res, sent) 
		for tag, words in dic.items():
			#res = u"%s \n %s :" %(res, tag)
			for w in words: 
				res = u"%s %s/%s" %(res, w, tag)	
	return res



	
#---------------------------------------------------------------
# save the processed result
#---------------------------------------------------------------

def createPath(path):
	if not os.path.exists(path): 
		os.makedirs(path)


raw_path = "../raw/articles/"
res_path = "../res/articles/"

createPath(res_path)

dates = os.listdir(raw_path)

# main processing is done in here

for date in dates: 
	date_path = os.path.join(raw_path, date)
	res_date_path = os.path.join(res_path, date)
	
	createPath(res_date_path)
	
	if os.path.isdir(date_path):
		print date_path
		articles = os.listdir(date_path)
		for article in articles: 
		
			data_path = os.path.join(date_path, article)
			
			
			# data : article txt files crawled from web
			data = open(data_path, "r")
			# do necessary processing
			'''
			# only for one article 
			if article == "0000714483":
				result = process(data_path)
			'''
			
			result = data.readlines()[4]
			#data.close()

			res_data_path = os.path.join(res_date_path, article)
			
			#print "write from %s to %s"  %(data_path, res_data_path)
			
			# res : text file for saving processed data of article
			res = open(res_data_path,"w+")
			
			# write processed data accordingly
			res.write(result)
			
			res.close()
