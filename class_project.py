import requests
import csv

url = 'https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY'
params = {
    'stockNo': '2330',
    'response': 'json'
}

response = requests.get(url, params=params)
data = response.json()['data']
start_date = '20120301'
end_date = '20230301'

with open('data.csv', mode='w', encoding='big5', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['日期', '成交股數', '成交金額', '開盤價', '最高價',
                    '最低價', '收盤價', '漲跌價差', '成交筆數'])
    date = start_date
    while date <= end_date:
        params['date'] = date
        response = requests.get(url, params=params)
        data = response.json()['data']
        for row in data:
            writer.writerow(row)
        # Move to next month
        year = int(date[:4])
        month = int(date[4:6])
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1
        date = f'{year:04d}{month:02d}01'