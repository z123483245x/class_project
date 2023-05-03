# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime, date

# url = 'https://news.ltn.com.tw/list/breakingnews/business'

# res = requests.get(url)
# soup = BeautifulSoup(res.text, 'html.parser')

# news = soup.select('ul.list > li')

# for item in news:
#     # 获取新闻标题和時間
#     title_and_time = item.select_one('a.tit').text.strip()
#     time_str = title_and_time.split()[0]
#     title = ' '.join(title_and_time.split()[1:])

#     # 获取新闻链接
#     link = item.select_one('a.tit')['href']

#     # 解析新闻时间
#     hour, minute = time_str.split(':')
#     time = datetime.strptime(time_str, '%H:%M')
#     today = date.today()
#     datetime_obj = datetime.combine(today, time.time())
#     formatted_date = datetime_obj.strftime('%Y-%m-%d')

#     # 输出结果
#     print(f'Title: {title}\nLink: {link}\nTime: {hour}:{minute}\nDate: {formatted_date}\n')

import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date

url = 'https://news.ltn.com.tw/list/breakingnews/business'

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

news = soup.select('ul.list > li')

with open('news.csv', mode='w', encoding='big5', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Link', 'Date', 'Time'])

    for item in news:
        # 获取新闻标题和时间
        title_and_time = item.select_one('a.tit').text.strip()
        time_str = title_and_time.split()[0]
        title = ' '.join(title_and_time.split()[1:])

        # 获取新闻链接
        link = item.select_one('a.tit')['href']

        # 解析新闻时间
        hour, minute = time_str.split(':')
        time = datetime.strptime(time_str, '%H:%M')
        today = date.today()
        datetime_obj = datetime.combine(today, time.time())
        formatted_date = datetime_obj.strftime('%Y-%m-%d')

        # 写入 CSV 文件
        writer.writerow([title, link, formatted_date, f'{hour}:{minute}'])
