import bs4 #importing beautiful soup for parsing through html contents

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#User input for summoner name, fixes space issues
print("What is your summoner name?")
noModName = input()
modifiedName = noModName.replace(' ', '+')
my_url = "https://na.op.gg/summoner/userName=" + modifiedName #saving url in variable

#reads the url and information
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#parses through html and stores all raw html code in page_soup
page_soup = soup(page_html, "html.parser")

#finding the object we need in the html code from op.gg.summonerName
rank_container = page_soup.findAll("div", {"class":"TierRank"})
rank = rank_container[0].text
print("Your rank is", rank)

winRate_container = page_soup.findAll("span", {"class":"winratio"})
winRate = winRate_container[0].text
print(winRate)

ladder_container = page_soup.findAll("span", {"class":"ranking"})
ladder = ladder_container[0].text
print("Your current rank on your country's ladder is", ladder)

champ_container = page_soup.findAll("div", {"class":"ChampionName"})
champ = champ_container[0].text
print("Your most played champion in ranked is", champ)

gameType_container = page_soup.findAll("div", {"class":"GameType"})
gameType = gameType_container[0].text
print("Your last game was", gameType)

