from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import os
from time import sleep
import random
import re

count = 0

years = ["2015", "2016", "2017", "2018", "2019"]

for file in os.listdir("team_url/"):
    team_df = pd.read_csv("team_url/" + file)
    for x , y in team_df.iterrows():
        team = y[1].split("/")
        year = team[2].split(".")

        if os.path.exists("team_data/" + str(team[1]) + "/" + str(year[0])):
            continue

        else:
            driver = webdriver.Chrome()
            driver.get('https://www.pro-football-reference.com/' + y[1])
            soup = BeautifulSoup(driver.page_source,'lxml')
            driver.quit()

            z = y[1].split("/")
            w = z[2].split(".")

            os.makedirs("team_data/" + str(z[1]) + "/" + str(w[0]))

            for x in range(100):
                try:
                    table = soup.find_all('table')[x]#This is the index of any table of that page. If you change it you can get different tables.

                    tab_data = [[celldata.text for celldata in rowdata.find_all(["th","td"])]
                                            for rowdata in table.find_all("tr")]

                    df = pd.DataFrame(tab_data)
                    #os.makedirs("team_data/" + str(z[1]) + "/" + str(w[0]))
                    df.to_csv("team_data/" + str(z[1]) + "/" + str(w[0]) + "/" + str(count) + ".csv")
                    count += 1
                    print(count)
                except:
                    print("out of range")


            url_list = []
            url = re.findall(r'(players/\S+)', str(soup))

            for b in url:
                b = b.split("\">")
                if b[0] not in url_list and len(b[0]) > 8 and ".cgi" not in b[0] and "\"" not in b[0]:
                    url_list.append(b[0])

            if os.path.isfile("player_url/" + str(w[0]) + "/" + str(z[1])):
                continue
            else:
                os.makedirs("player_url/" + str(w[0]) + "/" + str(z[1]))
                df = pd.DataFrame(url_list)
                df.to_csv("player_url/" + str(w[0]) + "/" + str(z[1]) + "/player_urls_" + str(w[0]) + ".csv")

            count = 0
            sleep(random.randint(30,35))
