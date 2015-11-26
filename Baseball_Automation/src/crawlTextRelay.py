#-*- coding: utf-8 -*-
from selenium import webdriver
from pyvirtualdisplay import Display
import selenium 
from bs4 import BeautifulSoup as bs 
import urllib
import os, sys, re
from team_player import *
import datetime
import path
import requests

# for unicode setting
reload(sys)
sys.setdefaultencoding('utf-8')

RAW_TXT_PATH = path.RAW_TXT_PATH

'''
getPage : url -> html source
basic html crawling function.
url : url
res : return html source of the url
'''
def getPage(url):
    return urllib.urlopen(url).read()


'''
getUrlList : int -> listof int
return list of game id in the specific month
month : value of month
res : list of game ids in the input month
'''
def getUrlList(month):
     # need to be extended to more urls 
    source_url = "http://sports.news.naver.com/schedule/index.nhn?uCategory=&category=kbo&year=2015&month=%s"%month

    soup = bs(getPage(source_url), 'html.parser')

    tmp = soup.find_all('div', {'class' , 'sch_tb', 'sch_tb2'})

    gameIdLst = []

    for elem in tmp:
        for link in elem.find_all('a', href=True):
            gameIdLst.append(link['href'].split('=')[-1])
            print link['href'].split('=')[-1]

    gameIdLst = list(set(gameIdLst))

    return gameIdLst

'''
parseContent : listof (int, string) tuple
parse the lineup of fielders
lst : list of raw input 
res : listof (player, position) tuple
'''
def parseContent(lst):
    res = []
    tmp = []

    '''
    for idx, elem in enumerate(lst):
        if elem == u"평균자책":
            res = [0, lst[idx+1], u"선발투수"].extend(res)
            if elem != "" and re.match(r'^[0-9]+$', elem.strip()):
                if elem in [num for num, player, pos in res]:
                    res[-1] = (lst[idx], lst[idx+1], lst[idx+2].split()[0])
                else:
                    res.append((lst[idx], lst[idx+1], lst[idx+2].split()[0]))

                    if res[-1][1] in [u"지명타자"]: # exception handling
                    res = res[:-1]
                    '''         

    tmp.append((lst[lst.index(u"평균자책")+1], u"선발투수"))
    lineup = lst[lst.index(u"타율")+1:]
    for idx, elem in enumerate(lineup):
        if re.match(r'^[0-9]+$', elem.strip()):
            pos_lst = [pos for player, pos in tmp]
            if lineup[idx+2].split()[0] in pos_lst:
                old = pos_lst.index(lineup[idx+2].split()[0])
                tmp[old] = (lineup[idx+1], lineup[idx+2].split()[0])
            else:
                tmp.append((lineup[idx+1], lineup[idx+2].split()[0]))

    trans_dic = { u"선발투수" : "pitcher", 
                 u"포수" : "catcher", 
                 u"1루수" : "b1man" , 
                 u"2루수" : "b2man", 
                 u"3루수" : "b3man", 
                 u"유격수" : "shotstop", 
                 u"좌익수" : "leftfielder", 
                 u"중견수" : "centerfielder", 
                 u"우익수" : "rightfielder", }

    pos_lst = [pos for player, pos in tmp]

    for pos in trans_dic.keys():
        if pos in pos_lst:
            res.append((tmp[pos_lst.index(pos)][0], trans_dic[pos]))

    for player, pos in res:
        print player, pos

    print 

    return res





'''
textRelayCrawler : listof int, string -> None
crawl text relays for given gameid and write to path 
'''
def textRelayCrawler(gameIdLst, path):  
    display = Display(visible=0, size=(800, 800))
    display.start()
    browser_text = webdriver.Chrome()
    browser_line = webdriver.Chrome()
    browser_info = webdriver.Chrome()
    for id in gameIdLst:
        newText = True
        try:
            state = open(RAW_TXT_PATH + "/current_data.txt", "r")
            for line in state.readlines():
                if line.strip() == id:
                    newText = False
            state.close()
        except IOError:
            open(RAW_TXT_PATH+'current_data.txt','w+').close()

        #if newText and id[:4]=="2015": # for 2015 season                       
        if id[:4]=="2015": # for 2015 season
            date = id[:8]
            if not os.path.exists("%s/%s"%(path, date)):
                os.makedirs("%s%s"%(path, date))
            text = open("%s%s/%s"%(path, date, id + ".txt"), "w+")

            date = id[:8]
            # need to changed to datetime
            # date here 
            if date > "20150806":
                print date
                break

            url_text = 'http://sports.news.naver.com/gameCenter/miniTextRelay.nhn?category=kbo&date=%s&gameId=%s'%(date, id)

            url_line = 'http://sports.news.naver.com/gameCenter/textRelay.nhn?gameId=%s&category=kbo'%id

            url_gameInfo = 'http://sports.news.naver.com/gameCenter/gameRecord.nhn?gameId=%s&category=kbo'%id

            print "parsing from %s"%id

            browser_text.get(url_text)
            browser_line.get(url_line)
            browser_info.get(url_gameInfo)
            try:
                while True:
                    try:
                        # crawling gameInfo
                        result_board = browser_info.find_element_by_class_name('t_result_board')
                        away_score = result_board.find_element_by_id('box_aScoreR').text
                        home_score = result_board.find_element_by_id('box_hScoreR').text
						
                        away = get_team_by_code(id[8:10]).sponsor
                        home = get_team_by_code(id[10:12]).sponsor
                        d = datetime.datetime.strptime(id[0:8], "%Y%m%d")

                        text.write(d.strftime("%Y.%-m.%d") + " " + away + " vs " + home + " " + away_score + " " + home_score + "\n")
                        print d.strftime("%Y.%-m.%d") + " " + away + " vs " + home + " " + away_score + " " + home_score + "\n"

                        game_place = browser_info.find_element_by_id('box_gamePlace')
                        stadium = game_place.text
                        text.write("구장 : "+stadium[13:15]+"구장\n")
                        print "구장 : "+stadium[13:15]+"구장\n"

                        detail_info = browser_info.find_element_by_id("box_detail")
                        text.write(detail_info.text+"\n")
                        print detail_info.text+"\n"
	
                        # crawling lineup
                        button = browser_line.find_element_by_id('away_lineup_btn')
                        button.click()

                        content = browser_line.find_element_by_id('lineup_box')
                        away_raw = content.text
                        
                        flag=0
                        for elem in content.find_elements_by_tag_name('tr'):
                       	    td_length = len(elem.find_elements_by_tag_name('td'))
                            cnt=0
                            if td_length == 0:
                                if flag == 0:
                                    text.write("이름 이닝 투구수 피안타 홈런 볼넷 삼진 실점 자책 오늘평균자책 시즌평균자책 상대평균자책")
                                    flag = 1
                                else:
                                    text.write("타순 이름 포지션 타수 득점 안타 타점 홈런 볼넷 삼진 사구 오늘타율 시즌타율 상대타율")
                            for td_elem in elem.find_elements_by_tag_name('td'):
                                if td_length == 12:	#pitcher
                                    if cnt == 0:
                                        text.write("%s " % td_elem.find_element_by_tag_name('a').text)
                                    else:
                                        text.write("%s " % td_elem.text)
                                
                                elif td_length == 14: #batter
                                    if cnt == 1:
                                        text.write("%s " % td_elem.find_element_by_tag_name('a').text)
                                    else:
                                        text.write("%s " % td_elem.text)
                                cnt+=1
                            # end of for
                            text.write("\n")
                        button.click()

                        button = browser_line.find_element_by_id('home_lineup_btn')
                        button.click()

                        content = browser_line.find_element_by_id('lineup_box')
                        home_raw = content.text

                        flag=0
                        for elem in content.find_elements_by_tag_name('tr'):
                       	    td_length = len(elem.find_elements_by_tag_name('td'))
                            cnt=0
                            if td_length == 0:
                                if flag == 0:
                                    text.write("이름 이닝 투구수 피안타 홈런 볼넷 삼진 실점 자책 오늘평균자책 시즌평균자책 상대평균자책")
                                    flag = 1
                                else:
                                    text.write("타순 이름 포지션 타수 득점 안타 타점 홈런 볼넷 삼진 사구 오늘타율 시즌타율 상대타율")
                            for td_elem in elem.find_elements_by_tag_name('td'):
                                if td_length == 12:	#pitcher
                                    if cnt == 0:
                                        text.write("%s " % td_elem.find_element_by_tag_name('a').text)
                                    else:
                                        text.write("%s " % td_elem.text)
                                
                                elif td_length == 14: #batter
                                    if cnt == 1:
                                        text.write("%s " % td_elem.find_element_by_tag_name('a').text)
                                    else:
                                        text.write("%s " % td_elem.text)
                                cnt+=1
                            # end of for
                            text.write("\n")

                        away_lst = [elem for elem in away_raw.split("\n") if elem!=""]

                        home_lst = [elem for elem in home_raw.split("\n") if elem!=""]
                        
                        text.write("LineUp\n")
                        # writing home lineup
                        text.write("Home\n")
                        for name, pos in parseContent(home_lst):
                            text.write("%s - %s\n"%(name, pos))

                        # writing away lineup   
                        text.write("Away\n")
                        for name, pos in parseContent(away_lst):
                            text.write("%s - %s\n"%(name, pos)) 
                        break

                    except selenium.common.exceptions.NoSuchElementException:
                        pass

                text.write("Start Relay Text\n")

                # crawling relay text
                button = browser_text.find_element_by_id('inning_tab_all')
                button.click()
                # Get Relay_Text
                relay_text = browser_text.find_element_by_id('relay_text')
                text.write(relay_text.text)


                text.close()


                # write to current data 
                state = open(RAW_TXT_PATH+"current_data.txt", "a+")
                state.write(id + "\n")
                state.close()
                #print relay_text.text
            except selenium.common.exceptions:
                pass


        else:
            pass
    browser_text.quit()
    browser_line.quit()
    browser_info.quit()     

if __name__ == "__main__":
    if not os.path.exists(RAW_TXT_PATH):
        os.makedirs(RAW_TXT_PATH)

    gameLst = []

    #for i in range(3, 10): # season from 2015.03~2015.09
    #       gameLst.extend(getUrlList(str(i)))

    gameLst = ['20150319SSNC0']

    textRelayCrawler(gameLst, RAW_TXT_PATH)


