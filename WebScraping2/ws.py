import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

url = 'https://www.nba.com/stats/leaders/?SeasonType=Regular%20Season'

option = Options()
option.headless = True
drive = webdriver.Chrome()

drive.get(url)

time.sleep(10)

drive.find_element("")

drive.quit()
