# U2. 星號解包為何能處理「不定長」且結果固定是 list（1.2）

# 星號 (*) 在解包時用於收集剩餘的元素，無論剩餘元素有多少個
# 收集到的結果永遠是 list 型別，即使沒有元素也是空 list

# 範例1: 基本星號解包
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phones = record

print(f"原始 record: {record}")
print(f"name = {name}")
print(f"email = {email}")
print(f"phones = {phones}")  # phones 永遠是 list
print(f"phones 型別: {type(phones)}")

# 範例2: 沒有剩餘元素時
print("\n--- 沒有剩餘元素 ---")
short_record = ('Alice', 'alice@example.com')
name2, email2, *phones2 = short_record
print(f"short_record: {short_record}")
print(f"phones2 = {phones2}")  # 仍是空 list []
print(f"phones2 型別: {type(phones2)}")

# 範例3: 星號在中間位置
print("\n--- 星號在中間 ---")
data = ['ACME', 50, 91.1, 45.23, 78.09]
*trailing, current = data
print(f"data: {data}")
print(f"*trailing, current 解包結果:")
print(f"trailing = {trailing}")
print(f"current = {current}")

# 範例4: 多個星號（Python 3.11+）
print("\n--- 多個星號解包 ---")
try:
    items = [1, 2, 3, 4, 5, 6]
    first, *middle, last = items
    print(f"items: {items}")
    print(f"first = {first}, middle = {middle}, last = {last}")
except SyntaxError as e:
    print(f"多個星號在舊版 Python 中不支援: {e}")

# 星號解包的應用場景
print("\n--- 星號解包的應用場景 ---")
print("1. 處理不定長度序列: name, *args = data")
print("2. 函式參數收集: def func(*args):")
print("3. 列表合併: [*list1, *list2]")
print("4. 字典合併: {**dict1, **dict2}")

# 實際應用範例
print("\n--- 實際應用範例 ---")

# 分割路徑
def split_path(path):
    *dirs, filename = path.split('/')
    return dirs, filename

path = "/usr/local/bin/python"
dirs, filename = split_path(path)
print(f"路徑: {path}")
print(f"目錄: {dirs}")
print(f"檔案: {filename}")

# 處理成績單
scores = [85, 92, 78, 96, 88]
first, second, *others = sorted(scores, reverse=True)
print(f"\n成績: {scores}")
print(f"最高分: {first}, 第二高: {second}, 其他: {others}")

print("\n--- 星號解包的特性 ---")
print("1. 收集剩餘元素為 list")
print("2. 即使沒有元素也是 []")
print("3. 可以出現在任何位置")
print("4. 一個序列只能有一個 *")

