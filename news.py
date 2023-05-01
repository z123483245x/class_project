import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime
import pytz
import csv

url = 'https://www.dailyfxasia.com/cn/sp-500/news-and-analysis'

res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

dfx_widget = soup.find('div', class_='dfx-widget__content')

links = dfx_widget.find_all(['a'])

# 使用正則表達式抓取日期
pattern = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')

news_list = []
for link in links:
    text = link.text.strip()
    href = link.get('href')
    time_string = pattern.search(text).group()  # 使用正則表達式搜尋日期
    title = text.replace(time_string, '').strip()  # 去除日期後的文字就是新聞標題
    time_format = datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')  # 將時間字串轉換為 datetime 物件
    tw_tz = pytz.timezone('Asia/Taipei')  # 取得台灣時區的 tzinfo 物件
    time_tw = time_format.replace(tzinfo=pytz.utc).astimezone(tw_tz)  # 將時區轉換為台灣時區
    news_list.append({
        'title': title,
        'time': time_tw.strftime('%Y-%m-%d %H:%M:%S'),
        'url': href
    })

# 寫入 CSV 檔案
with open('new.csv', 'w', newline='', encoding='utf-8-sig') as f:
    fieldnames = ['標題', '日期', '網址']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for news in news_list:
        writer.writerow({'標題': news['title'], '日期': news['time'], '網址': news['url']})
# 列印出所有新聞的標題、日期、網址
for news in news_list:
    print(news['title'], news['time'], news['url'])