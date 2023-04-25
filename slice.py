# import pandas as pd

# # 讀取原始csv檔案
# df = pd.read_csv('GSPC.csv')

# # 把日期欄位轉換成datetime型別
# df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d')

# # 分割成兩份，按照你所需要的日期區間
# df1 = df[(df['Date'] >= '2022-04-13') & (df['Date'] <= '2023-04-13')]
# df2 = df[(df['Date'] >= '1927-12-31') & (df['Date'] <= '2022-04-12')]

# # 把日期欄位轉換回字串格式，以便寫入csv檔案
# df1['Date'] = df1['Date'].dt.strftime('%Y/%m/%d')
# df2['Date'] = df2['Date'].dt.strftime('%Y/%m/%d')

# # 寫入兩個不同的csv檔案
# df1.to_csv('GSPC_test.csv', index=False)
# df2.to_csv('GSPC_train.csv', index=False)

import pandas as pd

# 讀取原始csv檔案
df = pd.read_csv('GSPC.csv')

# 把日期欄位轉換成datetime型別
df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d')

# 分割成兩份，按照你所需要的日期區間
df1 = df[(df['Date'] >= '2022-04-13') & (df['Date'] <= '2023-04-13')]
df2 = df[(df['Date'] >= '1927-12-31') & (df['Date'] <= '2022-04-12')]

# 轉換數字類型
for col in df1.columns[1:]:
    if pd.api.types.is_numeric_dtype(df1[col]):
        df1[col] = df1[col].astype(float)

for col in df2.columns[1:]:
    if pd.api.types.is_numeric_dtype(df2[col]):
        df2[col] = df2[col].astype(float)

# 把日期欄位轉換回字串格式，以便寫入csv檔案
df1['Date'] = df1['Date'].dt.strftime('%Y/%m/%d')
df2['Date'] = df2['Date'].dt.strftime('%Y/%m/%d')

# 寫入兩個不同的csv檔案
df1.to_csv('GSPC_test.csv', index=False)
df2.to_csv('GSPC_train.csv', index=False)
