# R17. 字典子集（1.17）

# 原始價格字典，包含不同股票的價格
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55}

# 方法1: 根據值過濾 - 建立價格大於200的股票子集
# 使用字典推導式：{k: v for k, v in prices.items() if v > 200}
# 這會過濾出價格超過200的股票
p1 = {k: v for k, v in prices.items() if v > 200}
print("價格 > 200 的股票:", p1)

# 方法2: 根據鍵過濾 - 建立特定科技股的子集
# 定義要篩選的股票名稱集合
tech_names = {'AAPL', 'IBM'}
# 使用字典推導式：{k: v for k, v in prices.items() if k in tech_names}
# 這會過濾出鍵在 tech_names 集合中的項目
p2 = {k: v for k, v in prices.items() if k in tech_names}
print("科技股子集:", p2)

# 其他常見的字典子集建立方法
print("\n--- 其他字典子集方法 ---")

# 使用 dict() 建構函式配合條件
p3 = dict((k, v) for k, v in prices.items() if v < 100)
print("價格 < 100 的股票（使用 dict()）:", p3)

# 根據多個條件過濾
expensive_tech = {k: v for k, v in prices.items() if k in tech_names and v > 500}
print("價格 > 500 的科技股:", expensive_tech)

# 使用 filter 函式（較不直觀）
def price_over_200(item):
    return item[1] > 200  # item 是 (key, value) tuple

p4 = dict(filter(price_over_200, prices.items()))
print("價格 > 200 的股票（使用 filter）:", p4)

print("\n--- 字典推導式的優勢 ---")
print("1. 語法簡潔，易讀")
print("2. 直接建立新字典，不修改原字典")
print("3. 可以靈活設定過濾條件")
print("4. 支援鍵和值的條件過濾")

