import os

os.chdir("src/")
os.system("python crawlLeagueInfo.py")
os.system("python crawlTextRelay.py")
os.system("python processArticle.py")
