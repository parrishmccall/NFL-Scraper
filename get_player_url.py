from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re
from time import sleep
import os


"""Deprecated. Functionality moved to get_team_stats.py"""


years = ["2015", "2016", "2017", "2018", "2019"]

for year in years:
    team_df = pd.read_csv("team_url/team_urls_" + str(year) + ".csv")


    for x , y in team_df.iterrows():
        driver = webdriver.Chrome()
        driver.get('https://www.pro-football-reference.com/' + y[1])
        soup = BeautifulSoup(driver.page_source,'lxml')
        driver.quit()

        url_list = []

        url = re.findall(r'(players/\S+)', str(soup))

        for w in url:
            w = w.split("\">")
            if w[0] not in url_list and len(w[0]) > 8 and ".cgi" not in w[0] and "\"" not in w[0]:
                url_list.append(w[0])

        z = y[1].split("/")

        if os.path.isfile("player_url/" + str(year) + "/" + str(z[1])):
            continue
        else:
            os.makedirs("player_url/" + str(year) + "/" + str(z[1]))
            df = pd.DataFrame(url_list)
            df.to_csv("player_url/" + str(year) + "/" + str(z[1]) + "/player_urls_" + str(year) +".csv")
        sleep(20)
