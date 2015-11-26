#-*- coding: utf-8 -*-
import os, sys
import urllib
import re 
from bs4 import BeautifulSoup as bs 


# for unicode setting
reload(sys)
sys.setdefaultencoding('utf-8')

print "Begin crawling data."

# ARTICLE_DIR : directory for saving raw articles
ARTICLE_DIR = "..\\raw\\articles\\"

# basic html crawling function 
def get_page(url):
    return urllib.urlopen(url).read()

	
# target urls
leagueInfo = "http://sports.news.naver.com/schedule/index.nhn?category=kbo"


# soup_list manually made for 2015 season
soup_list = ["http://sports.news.naver.com/schedule/index.nhn?uCategory=&category=kbo&year=2015&month=%s"%month for month in ['03','04','05','06','07','08','09']]



print "Season informations are from following url."
for elem in soup_list:
	print elem

'''
League information crawling
matchList, teamList
'''

print "Get team list."
# template page for getting team information
soup = bs(get_page(leagueInfo), 'html.parser')

raw_team = soup.find_all('div', {'class', 'tab_team'})[0].find_all('a')

# list of teams
teamList = [elem.contents[0] for elem in raw_team[1:]]  


print "Get match list."
# list of matches
class Match():
	def __init__(self, home, away, date):
		self.home = home
		self.away = away
		self.date = date
		self.isCanceled = False 
		
	def setCanceled(self):
		self.isCanceled = True

	def __unicode__(self):
		return self.home + " : " + self.away + " at " + self.date 

# for league information url		
def getMatchList(sp):
	raw_match1 = sp.find_all('div', {'class':'sch_tb'})
	raw_match2 = sp.find_all('div', {'class':'sch_tb2'})

	#raw_match = raw_match2
	raw_match = raw_match1 + raw_match2 
	matchList = []

	for elem in raw_match:
		date = elem.find_all('span', {'class', 'td_date'})[0].text
		print date
		
		for idx, lft in enumerate(elem.find_all('span', {'class', 'team_lft'})):
			lft = lft.text
			try:
				rgt = elem.find_all('span', {'class', 'team_rgt'})[idx].text
				#print lft, rgt
				matchList.append(Match(lft, rgt, date))
			except IndexError:
				print "missing %s"%lft
				pass
			

	return matchList
	

	
# matchList contains all match for the given season. 
# matchList should be about 750~800 matches per season. 
	
matchList = []
for url in soup_list:
	matchList.extend(getMatchList(bs(get_page(url),'html.parser')))

print "Number of matches : %d"%len(matchList)


print "League information crawling finished."
print "Now crawl articles."



'''
get article links from article 
'''

# -----------------------------------------------------------------------------------------------
#Functions for parsing crawled data 
# -----------------------------------------------------------------------------------------------
# auxiliary functions for parsing articles
# need optimization - now too slow! 
def parseProvider(provider):
	return provider.split(':')[1].replace(' ', '').replace('\n', '')

def parseTitle(title):
	return title.split(u"기사입력")[0].replace("\n", '').strip()
	
def parseDate(title):
	return title.split(u"기사입력")[1].split('|')[0].replace("\n", '').split(" ")[0]

def parseArticle(article):
	res = article.replace(u'\xa0', u' ').split('(function')[0].split(u'관련뉴스언론사 페이지로 이동합니다.')[0]
	res = res.strip('\n').strip()
	return res.split('\n')[-1]
	
	
# auxillary function for parseAuthor
def isHangul(txt):
    res = True
    han = re.compile(u'[가-힣]')
    for char in txt: 
        if han.match(char):
            res = True
        else: 
            return False
    return res
	
# need to be more specific
def parseAuthor(article): 
	word_lst = article.split()
	candidate = []
	for idx, word in enumerate(word_lst):
		# assume 3 word name 
		if word.startswith(u'기자'):
			candidate.append(word_lst[idx-1][-3:])
		elif u'기자' in word:
			candidate.append(word.split(u'기자')[0][-3:])	
			
	tmp = set(candidate)
	res = []

	exceptionList = [u'객원', u'인턴', u'인터넷', u'즐', u'복귀', u'이' , u'아' , u'선임' , u'지난해' , u'직후'	, u'기에서' , ]
	

	for elem in tmp:
		if elem in exceptionList:
			pass
		elif isHangul(elem):
			res.append(elem)
		else:
			pass
			
	return res
	
def parseId(url):
	return url.split('&')[4].split('=')[1]
	
	

	
	

def crawlURL(url):
	newArticle = True
	try:
		state = open("..\\raw\\articles\\current_data.txt", "r")
		for line in state.readlines():
			if line.strip() == parseId(url):
				newArticle = False
		state.close()
	except IOError:
		open('..\\raw\\articles\\current_data.txt','w+').close()
		
	if newArticle: # comment when testing for small number of articles are done
		print "parsing " + url
		
		soup = bs(get_page(url))
		# title : get title and time 
		title = soup.find_all('div', {'class', 'articlehead'})[0].text
		# article : get article content and author
		article = soup.find_all('div', {'class', 'article'})[0].text
		# provider : get provider
		provider = soup.find_all('p', {'class', 'sourcecompany'})[0].text
		
		if not os.path.exists("..\\raw\\articles\\" + parseDate(title)):
			os.makedirs("..\\raw\\articles\\" + parseDate(title))
		tmp = open("..\\raw\\articles\\" + parseDate(title) + "\\" + parseId(url) + ".txt" , "w+")
		tmp.write("Id : " + parseId(url) +  "\n")
		tmp.write("Title : " + parseTitle(title) +  "\n")
		tmp.write("Date : " + parseDate(title) +  "\n")
		tmp.write("Provider : " + parseProvider(provider) +  "\n")
		
		authors = parseAuthor(article)
		if len(authors) == 0:
			tmp.write("Author : n/a \n")
		else:
			tmp.write("Author : ")
			for author in authors:
				tmp.write(author + " ")
			tmp.write("\n")
		tmp.write(parseArticle(article))
		tmp.close()
		state = open("..\\raw\\articles\\current_data.txt", "a+")
		state.write(parseId(url) + "\n")
		state.close()	
		
	else:
		pass
		#print "Already exists : " + url
#-----------------------------------------------------------------------------------------------------------------------------------


def listlink(date, ind):
	return 	"http://sports.news.naver.com/sports/index.nhn?category=kbo&ctg=news&mod=lst&type=news&date="+ date + "&page=" + str(ind+1)

# for more article in a date, should increase pagenum 
PAGENUM = 5
DATENUM = 10 # maximum 157 for this season
dates = []

for date in set([match.date for match in matchList]):
	month, day = date.split()[0].split('.')
	if len(month) == 1: 
		month = '0' + month
	if len(day) == 1: 
		day = '0' + day 
	dates.append("2015" + month + day)

	
articlelist_urls = [listlink(date, i) for i in range(PAGENUM) for date in dates[:DATENUM+1]]

# get link of articles
article_num = 0
if not os.path.exists(ARTICLE_DIR):
    os.makedirs(ARTICLE_DIR)
	
	
for url in articlelist_urls:
	soup = bs(get_page(url))
	articleLst = soup.find_all('td', {'class', 'ln15'})
	for elem in articleLst:
		try:
			crawlURL("http://sports.naver.com" + elem.find_all('a')[0]['href'])
		except IndexError: 
			err = open('..\\raw\\articles\\error.txt','a+')
			err.write("Indexerror : %s \n"%url)
			print "IndexError in %s"%url
			err.close()