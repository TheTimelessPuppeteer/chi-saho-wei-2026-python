# U10. zip 為何只能用一次（1.8）

# zip() 回傳的是迭代器，不是列表
# 迭代器只能遍歷一次，遍歷完就耗盡了

prices = {'A': 2.0, 'B': 1.0, 'C': 3.0}
print(f"價格字典: {prices}")

# 建立 zip 物件
z = zip(prices.values(), prices.keys())
print(f"zip 物件: {z}")
print(f"zip 物件型別: {type(z)}")

# 第一次使用：正常運作
print("\n--- 第一次使用 zip ---")
min_result = min(z)
print(f"min(z) = {min_result}")

# 第二次使用：失敗，因為迭代器已耗盡
print("\n--- 第二次使用 zip ---")
try:
    max_result = max(z)
    print(f"max(z) = {max_result}")
except ValueError as e:
    print(f"ValueError: {e}")
    print("因為 zip 迭代器已經被消耗完了！")

# 如何正確重複使用？
print("\n--- 正確的重複使用方法 ---")

# 方法1: 每次都重新建立 zip
print("方法1: 重新建立 zip")
z1 = zip(prices.values(), prices.keys())
print(f"min: {min(z1)}")
z2 = zip(prices.values(), prices.keys())
print(f"max: {max(z2)}")

# 方法2: 轉成列表儲存
print("\n方法2: 轉成列表")
z_list = list(zip(prices.values(), prices.keys()))
print(f"zip 列表: {z_list}")
print(f"min: {min(z_list)}")
print(f"max: {max(z_list)}")
print(f"再次使用: min={min(z_list)}, max={max(z_list)}")

# 方法3: 同時計算（推薦）
print("\n方法3: 同時計算所有需要的結果")
z_new = zip(prices.values(), prices.keys())
values = list(z_new)  # 一次性消耗並儲存
print(f"所有值: {values}")
print(f"min: {min(values)}")
print(f"max: {max(values)}")

# 為什麼 zip 是迭代器？
print("\n--- 為什麼 zip 是迭代器？ ---")
print("1. 節省記憶體：不需一次建立完整列表")
print("2. 支援無限序列：可以處理無限長的迭代器")
print("3. 鏈式操作：可以直接傳給其他函式")
print("4. 符合 Python 慣例：多數內建函式回傳迭代器")

# 實際應用場景
print("\n--- 實際應用場景 ---")

# 場景1: 大資料處理
print("場景1: 大資料處理")
large_values = range(1000000)  # 模擬大資料
large_keys = range(1000000)

# 使用 zip 迭代器，不會佔用大量記憶體
z_large = zip(large_values, large_keys)
first_5 = []
for i, pair in enumerate(z_large):
    if i >= 5:
        break
    first_5.append(pair)
print(f"大資料前 5 組: {first_5}")

# 場景2: 鏈式操作
print("\n場景2: 鏈式操作")
data = [1, 2, 3, 4, 5]
keys = ['a', 'b', 'c', 'd', 'e']

# zip -> filter -> dict：一氣呵成
result = dict(zip(keys, data))
print(f"鍵值配對結果: {result}")

# 場景3: 矩陣轉置
print("\n場景3: 矩陣轉置")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = list(zip(*matrix))
print(f"原始矩陣: {matrix}")
print(f"轉置後: {transposed}")

# 注意事項
print("\n--- 注意事項 ---")
print("1. zip 物件只能迭代一次")
print("2. 如果需要多次使用，轉成 list 或 tuple")
print("3. zip 會在最短序列耗盡時停止")
print("4. 空 zip 物件的行為：list(zip()) = []")
print("5. zip(*zip_obj) 可以解包，但只能用一次")

