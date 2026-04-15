# R20. ChainMap 合併映射（1.20）

# ChainMap 用於合併多個字典，當鍵重複時優先取前面的字典

from collections import ChainMap

# 建立兩個字典
a = {'x': 1, 'z': 3}  # 第一個字典
b = {'y': 2, 'z': 4}  # 第二個字典，注意 'z' 鍵重複

# 建立 ChainMap，a 在前，b 在後
# ChainMap(a, b) 會先從 a 找鍵，如果找不到再從 b 找
c = ChainMap(a, b)

print("字典 a:", a)
print("字典 b:", b)
print("ChainMap c:", dict(c))  # 轉成字典顯示

# 存取鍵值
print(f"c['x'] = {c['x']}")  # x 只在 a 中存在
print(f"c['y'] = {c['y']}")  # y 只在 b 中存在
print(f"c['z'] = {c['z']}")  # z 在 a 和 b 中都存在，優先取 a 的值 (3)

# ChainMap 的特性
print(f"\n--- ChainMap 特性 ---")
print(f"所有鍵: {list(c.keys())}")
print(f"所有值: {list(c.values())}")
print(f"鍵值對: {list(c.items())}")

# 修改操作（會影響原始字典）
c['x'] = 10  # 修改會影響到 a
print(f"修改後 a: {a}")
print(f"修改後 c['x']: {c['x']}")

# 新增鍵（會加到第一個字典）
c['w'] = 5  # 新增會加到 a
print(f"新增後 a: {a}")
print(f"新增後 c['w']: {c['w']}")

# 多個字典的 ChainMap
print(f"\n--- 多個字典合併 ---")
d = {'m': 100}
combined = ChainMap(a, b, d)
print("三個字典合併:", dict(combined))
print(f"combined['m'] = {combined['m']}")

# ChainMap 的應用場景
print(f"\n--- 應用場景 ---")
print("1. 合併多個配置字典（優先順序）")
print("2. 實現作用域鏈（類似巢狀變數查找）")
print("3. 提供預設值（最後一個字典作為預設）")

# 與 dict.update() 的比較
print(f"\n--- 與 dict.update() 比較 ---")
merged = {}
merged.update(b)  # 先更新 b
merged.update(a)  # 再更新 a，會覆蓋 b 的鍵
print("dict.update() 合併:", merged)
print("ChainMap 保持原始字典不變:", dict(c))

