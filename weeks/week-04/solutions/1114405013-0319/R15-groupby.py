# R15. 分組 groupby（1.15）

# 匯入必要的模組
from itertools import groupby  # groupby 用於將連續的相同元素分組
from operator import itemgetter  # itemgetter 用於從字典或物件中取出特定欄位

# 範例資料：模擬一些記錄，每個記錄有日期和地址
# 這是一個列表，包含多個字典，每個字典代表一筆記錄
rows = [
    {'date': '07/01/2012', 'address': 'Taipei'},
    {'date': '07/02/2012', 'address': 'Kaohsiung'},
    {'date': '07/01/2012', 'address': 'Taichung'},
    {'date': '07/03/2012', 'address': 'Tainan'},
    {'date': '07/02/2012', 'address': 'Taipei'},
]

# 必須先排序，因為 groupby 要求資料是排序過的
# key=itemgetter('date') 表示以 'date' 欄位作為排序依據
rows.sort(key=itemgetter('date'))

# 印出分組結果的標題
print("分組結果：")

# 使用 groupby 進行分組
# groupby(rows, key=itemgetter('date')) 會根據 'date' 欄位將連續相同日期的記錄分組
# 回傳 (group_key, group_items) 的迭代器
for date, items in groupby(rows, key=itemgetter('date')):
    # 印出當前分組的日期
    print(f"日期: {date}")

    # items 是該日期下的所有記錄（生成器）
    # 逐一取出並印出地址
    for item in items:
        print(f"  - {item['address']}")

    # 空行分隔各組，讓輸出更易讀
    print()


