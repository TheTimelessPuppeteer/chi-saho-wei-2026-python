# R11. 命名切片 slice（1.11）
# 本範例展示如何使用 slice 物件來給切片命名，提高程式碼的可讀性與可維護性。
# 適用於固定寬度格式的資料（如舊式文本檔案、銀行記錄等）的解析。

# 假設這是一筆固定寬度的記錄，包含股份數量和價格等資訊
# 位置 20-23 是股份數量，位置 31-37 是價格
record = '....................100 .......513.25 ..........'
print("原始記錄:", record)
print()

# 方法 1: 直接用索引（不推薦，難以理解數字的含義）
shares_direct = int(record[20:23])
price_direct = float(record[31:37])
print("直接索引方式:")
print(f"  股份數量: {shares_direct}")
print(f"  價格: {price_direct}")
print()

# 方法 2: 使用命名 slice 物件（推薦，容易理解和維護）
# slice(start, stop) 建立一個可重複使用的切片物件
SHARES = slice(20, 23)
PRICE = slice(31, 37)
print("命名 slice 物件方式:")
print(f"  SHARES = {SHARES}")
print(f"  PRICE = {PRICE}")

# 提取資料並轉換
shares = int(record[SHARES])
price = float(record[PRICE])
print(f"  record[SHARES] = '{record[SHARES]}' -> int = {shares}")
print(f"  record[PRICE] = '{record[PRICE]}' -> float = {price}")
print()

# 計算總成本
cost = shares * price
print(f"總成本 = {shares} * {price} = {cost}")
print()

# 更多示範：多個切片的應用場景
print("=== 更多示範 ===")
data = 'Name: Alice Age:  25 Score: 95.5'
print("資料:", data)

# 定義多個命名切片
NAME = slice(6, 11)
AGE = slice(18, 20)
SCORE = slice(29, 33)

print(f"姓名: {data[NAME]}")
print(f"年齡: {int(data[AGE])}")
print(f"分數: {float(data[SCORE])}")

# 理解重點：
# 1. slice(start, stop) 等同於 [start:stop]，但可以命名和重複使用
# 2. 命名切片提高程式碼的可讀性，減少 hardcoded 索引
# 3. 對固定寬度格式的資料解析特別有用
# 4. 可以在多個地方重複使用同一個 slice 物件，避免重複定義
# 5. slice 物件也支援 step 參數：slice(start, stop, step)
