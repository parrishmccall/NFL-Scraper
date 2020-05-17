from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re
from time import sleep
import os

years = ["2015", "2016", "2017", "2018", "2019"]

for year in years:
    os.makedirs("games_url/games_" + year)
    driver = webdriver.Chrome()
    driver.get('https://www.pro-football-reference.com/years/' + year + "/games.htm")
    soup = BeautifulSoup(driver.page_source,'lxml')
    driver.quit()

    url_list = []
    url = re.findall(r'(boxscores/\S+)', str(soup))

    for w in url:
        w = w.split("\">")
        if w[0] not in url_list and len(w[0]) > 10 and ".cgi" not in w[0] and "\"" not in w[0]\
                and "game-scores.htm" not in w[0]:
            url_list.append(w[0])

    df = pd.DataFrame(url_list)
    df.to_csv("games_url/games_" + year + "/games.csv")
    sleep(20)
