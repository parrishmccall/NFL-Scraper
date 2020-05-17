from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import os
import random

years = ["2015", "2016", "2017", "2018", "2019"]

player_urls = []

os.makedirs("player_data")

for folder, city, files in os.walk("player_url"):
    for name in files:
        df = pd.read_csv(os.path.join(folder, name))
        for x, y in df.iterrows():
            if y[1] not in player_urls:
                player_urls.append(y[1])

count = 0
for url in player_urls:
    driver = webdriver.Chrome()
    driver.minimize_window()
    driver.get('https://www.pro-football-reference.com/' + str(url))
    soup = BeautifulSoup(driver.page_source,'lxml')
    driver.quit()

    name = url.split("/")
    os.makedirs("player_data/" + str(name[2]) +"/")

    for x in range(100):
        try:
            table = soup.find_all('table')[x]#This is the index of any table of that page. If you change it you can get different tables.

            tab_data = [[celldata.text for celldata in rowdata.find_all(["th","td"])]
                                    for rowdata in table.find_all("tr")]

            df = pd.DataFrame(tab_data)
            df.to_csv("player_data/" + str(name[2]) + "/" + "table_" + str(count) + ".csv")
            count += 1
        except:
            print("out of range")
    count = 0
    sleep(random.randint(20,35))
