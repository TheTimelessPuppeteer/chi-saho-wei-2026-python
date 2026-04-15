# U9. groupby 為何一定要先 sort（1.15）

# groupby 只能將「連續相同」的元素分組
# 如果資料沒有排序，同值的元素可能分散在不同位置，導致分組錯誤

from itertools import groupby
from operator import itemgetter

# 範例資料：故意打亂順序
rows = [
    {'date': '07/02/2012', 'x': 1},
    {'date': '07/01/2012', 'x': 2},
    {'date': '07/02/2012', 'x': 3},
]

print("原始資料（未排序）:")
for row in rows:
    print(f"  {row}")

# 錯誤示範：未排序就 groupby
print("\n--- 錯誤：未排序就 groupby ---")
print("groupby 只看「連續」相同元素，07/02 被分成兩組:")
groups_wrong = []
for date, group in groupby(rows, key=itemgetter('date')):
    group_list = list(group)
    groups_wrong.append((date, group_list))
    print(f"  日期 {date}: {len(group_list)} 筆資料")

# 正確方法：先排序再 groupby
print("\n--- 正確：先排序再 groupby ---")
rows_sorted = sorted(rows, key=itemgetter('date'))  # 建立排序後的複本
print("排序後的資料:")
for row in rows_sorted:
    print(f"  {row}")

print("\n排序後的正確分組:")
groups_correct = []
for date, group in groupby(rows_sorted, key=itemgetter('date')):
    group_list = list(group)
    groups_correct.append((date, group_list))
    print(f"  日期 {date}: {len(group_list)} 筆資料")

# 比較結果
print("\n--- 比較結果 ---")
print("未排序分組數量:", len(groups_wrong))
print("正確分組數量:", len(groups_correct))
print("未排序的 07/02 被錯誤分成:", [g[0] for g in groups_wrong if '07/02' in g[0]])

# 為什麼需要排序？
print("\n--- 為什麼 groupby 需要排序？ ---")
print("1. groupby 只能看到「連續」相同元素")
print("2. 未排序時，同值元素可能分散")
print("3. 排序確保同值元素聚在一起")
print("4. 這是 groupby 的基本假設")

# 實際應用範例
print("\n--- 實際應用：日誌分析 ---")

# 模擬網站訪問日誌
logs = [
    {'date': '2023-01-03', 'user': 'Alice', 'page': '/home'},
    {'date': '2023-01-01', 'user': 'Bob', 'page': '/about'},
    {'date': '2023-01-02', 'user': 'Charlie', 'page': '/contact'},
    {'date': '2023-01-03', 'user': 'David', 'page': '/products'},
    {'date': '2023-01-01', 'user': 'Eve', 'page': '/home'},
    {'date': '2023-01-02', 'user': 'Frank', 'page': '/about'},
]

print("網站訪問日誌:")
for log in logs:
    print(f"  {log['date']}: {log['user']} 訪問 {log['page']}")

# 正確的按日期分組統計
logs_sorted = sorted(logs, key=itemgetter('date'))
print("\n按日期分組統計:")
for date, day_logs in groupby(logs_sorted, key=itemgetter('date')):
    visits = list(day_logs)
    print(f"  {date}: {len(visits)} 次訪問")

# 進階：按日期和頁面雙重分組
print("\n按日期和頁面分組:")
current_date = None
for date, day_logs in groupby(logs_sorted, key=itemgetter('date')):
    if current_date != date:
        print(f"\n  日期 {date}:")
        current_date = date

    # 對當天的日誌再按頁面分組
    day_list = list(day_logs)
    for page, page_logs in groupby(sorted(day_list, key=itemgetter('page')), key=itemgetter('page')):
        page_visits = list(page_logs)
        print(f"    {page}: {len(page_visits)} 次")

# 注意事項
print("\n--- 注意事項 ---")
print("1. groupby 前一定要排序")
print("2. key 函式決定分組依據")
print("3. group 物件只能迭代一次")
print("4. 如果資料已經排序，可以直接 groupby")
print("5. 對於大資料，考慮是否真的需要分組")

