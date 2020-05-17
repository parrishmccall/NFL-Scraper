from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re
from time import sleep
import os

years = ["2015", "2016", "2017", "2018", "2019"]

os.makedirs("team_url")

for x in years:
    driver = webdriver.Chrome()
    driver.get('https://www.pro-football-reference.com/years/' + str(x))
    soup = BeautifulSoup(driver.page_source,'lxml')
    driver.quit()
    count = 0

    url = re.findall(r'(teams/\S+)', str(soup))
    url_list = []

    for y in url:
        y = y.split("\">")
        if x != str(2019):
            if y[0] not in url_list and "2019" not in y[0] and len(y[0]) > 7:
                url_list.append(y[0])
        elif x == str(2019):
            if y[0] not in url_list and len(y[0]) > 7:
                url_list.append(y[0])

    df = pd.DataFrame(url_list)
    df.to_csv("team_url/team_urls_" + x + ".csv")
    sleep(20)
