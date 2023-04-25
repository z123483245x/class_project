import csv

with open('GSPC_train.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader) # 讀取header
    for row in reader:
        # 每一列資料的型態都是字串(str)，可以使用 type() 函數檢查資料型態
        print([type(val) for val in row])