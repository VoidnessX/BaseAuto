#-*- coding: utf-8 -*-
import sys
from selenium import webdriver
from pyvirtualdisplay import Display

# for unicode setting
reload(sys)
sys.setdefaultencoding('utf-8')

display = Display(visible=0, size=(800, 800))
display.start()
browser = webdriver.Chrome()
#browser.get('http://sports.news.naver.com/gameCenter/miniTextRelay.nhn?category=kbo&date=20150725&gameId=20150725LTHT0')
browser.get('http://sports.news.naver.com/gameCenter/miniTextRelay.nhn?category=premier12&gameId=88881111KRDO02015')

#All HTML source View
#print browser.page_source

button = browser.find_element_by_id('inning_tab_all')
button.click()
text = browser.find_element_by_id('relay_text')
print text.text 

browser.quit()

