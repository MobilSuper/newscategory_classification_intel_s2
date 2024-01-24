from bs4 import BeautifulSoup #pip install bs4
import requests
import re
import pandas as ps
import datetime

category = ['Politics', 'Economic', 'Social', 'Culture', 'World', 'IT']
url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100'

resp = requests.get(url)

print(resp)
print(type(resp))
print(list(resp))

soup = BeautifulSoup(resp.text, 'html.parser')
print(soup)
title_tags = soup.select('.sh_text_headline')
print(title_tags)
print(len(title_tags))
print(type(title_tags[0]))
titles = []
for title_tag in title_tags:
    titles.append(re.compile('[^가-힣]|a-z|A-Z]').sub(' ', title_tag.text))
print(titles)

df_title = pd.DataFrame()
