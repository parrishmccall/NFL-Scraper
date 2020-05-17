from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import os
from time import sleep

years = ["2015", "2016", "2017", "2018", "2019"]

for year in years:
    game_df = pd.read_csv("games_url/games_" + str(year) + "/games.csv")
    for x , y in game_df.iterrows():
        driver = webdriver.Chrome()
        driver.get('https://www.pro-football-reference.com/' + y[1])
        soup = BeautifulSoup(driver.page_source,'lxml')
        driver.quit()

        count = 0
        game_name = y[1].split("/")
        g2 = game_name[1].split(".")
        os.makedirs("games_data/" + str(year) + "/" + str(g2[0]))

        for x in range(100):
            try:
                table = soup.find_all('table')[x]#This is the index of any table of that page. If you change it you can get different tables.

                tab_data = [[celldata.text for celldata in rowdata.find_all(["th","td", "cap"])]
                                        for rowdata in table.find_all(["tr", "caption"])]

                df = pd.DataFrame(tab_data)
                df.to_csv("games_data/" + str(year) + "/" + str(g2[0]) + "/" + str(count) + ".csv")
                count += 1
            except:
                print("out of range")
        sleep(20)
