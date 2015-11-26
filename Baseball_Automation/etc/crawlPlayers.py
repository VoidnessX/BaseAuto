#-*- coding: utf-8 -*-
import requests as rq
import os, sys
import urllib
import re 
from bs4 import BeautifulSoup as bs 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0



# for unicode setting
reload(sys)
sys.setdefaultencoding('utf-8')

print "Begin crawling player data."

def get_page(url):
	return urllib.urlopen(url).read()
	

	
playerInfoList = [ "http://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx", 
"http://www.koreabaseball.com/Record/Player/PitcherBasic/Basic1.aspx", 
"http://www.koreabaseball.com/Record/Player/Defense/Basic.aspx", 
"http://www.koreabaseball.com/Record/Player/Runner/Basic.aspx"]

for url in playerInfoList[:1]: 
	soup = bs(get_page(url))
	#print get_page(url)
	player_list = soup.find_all('div', {'class', 'record_result'})[0]
	for player_link in player_list.find_all('a'):
		driver = webdriver.PhantomJS()
		driver.get("http://www.koreabaseball.com/Record/Player/Runner/Basic.aspx")
		driver.save_screenshot('page1.png')
		driver.find_element_by_id('cphContainer_cphContents_ucPager_btnNo2').click()
		driver.save_screenshot('page2.png')
		'''
		if player_link['href'].startswith("/Record"):
			print player_link['href']
		'''
		
	
	