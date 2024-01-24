from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd
import re
import time
import datetime

category = ['Politics', 'Economic', 'Social', 'Culture', 'World', 'IT']

options = ChromeOptions()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
options.add_argument = ('user_agent=' + user_agent)
options.add_argument('lang=ko_KR')
service=ChromeService(executable_path=ChromeDriverManager().install())
driver=webdriver.Chrome(service=service, options=options)
pages=[105, 105, 105, 81, 105, 81]

df_titles = pd.DataFrame()
for l in range(6):
    section_url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100{}'.format(l)
    titles=[]
    for k in range(1, pages[l]):
        url = section_url + '#&date=%2000:00:00&page{}'.format(k)
        try:
            driver.get(url)
            time.sleep(0.5)

        except:
            print('drvier.get')

