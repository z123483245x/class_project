# import requests
# from bs4 import BeautifulSoup
# import csv
# import datetime
# from dateutil.relativedelta import relativedelta
# import time

# start_time = time.time()
# # 設定起始日期和結束日期
# start_date = datetime.datetime(1927, 12, 31)
# end_date = datetime.datetime.now()

# # 設定要取得的時間區間，每個時間區間為一個月
# periods = []
# while start_date < end_date:
#     next_month = start_date + relativedelta(months=1)
#     periods.append((start_date, min(next_month, end_date)))
#     start_date = next_month

# # 設定標頭和 User-Agent
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
# }

# # 初始化儲存資料的變數
# data = []

# # 逐一取得每個時間區間的資料
# for period in periods:
#     start_date, end_date = period
#     start_timestamp = int(start_date.replace(tzinfo=datetime.timezone.utc).timestamp())
#     end_timestamp = int(end_date.replace(tzinfo=datetime.timezone.utc).timestamp())

#     url = f'https://finance.yahoo.com/quote/%5EGSPC/history?period1={start_timestamp}&period2={end_timestamp}&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'

#     response = requests.get(url, headers=headers, timeout=10)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     table = soup.find_all('table')[0]

#     # 將表格內容存儲到 list 中
#     rows = table.find_all('tr')
#     for row in rows:
#         cols = row.find_all('td')
#         cols = [ele.text.strip() for ele in cols]
#         data.append([ele for ele in cols if ele])

#     # 每個月抓資料間隔 3 秒
#     time.sleep(3)

# # 篩選出所需的數據
# header = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
# data = data[0:-1]
# data = [[datetime.datetime.strptime(ele[0], '%b %d, %Y').strftime('%Y/%m/%d'), ele[1], ele[2], ele[3], ele[4], ele[5], ele[6]] if len(ele) == 7 else [] for ele in data]
# data = [ele for ele in data if ele]
# # 將資料根據日期排序
# data = sorted(data, key=lambda x: datetime.datetime.strptime(x[0], '%Y/%m/%d'))

# print(data)

# # 將數據存儲到 CSV 文件中
# with open('123.csv', mode='w', encoding='big5', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(header)
#     writer.writerows(data)

# end_time = time.time()

# print(f"程式執行時間為 {end_time - start_time} 秒")



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
