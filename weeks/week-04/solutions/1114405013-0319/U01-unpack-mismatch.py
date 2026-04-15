# U1. 解包失敗的原因：變數數量 ≠ 元素數量（1.1）

# 解包（unpacking）是將序列的元素分配給多個變數
# 但當變數數量與元素數量不匹配時會發生 ValueError

# 範例資料：一個包含 2 個元素的 tuple
p = (4, 5)
print(f"tuple p = {p}，元素數量 = {len(p)}")

# 正確的解包：變數數量等於元素數量
x, y = p
print(f"正確解包: x = {x}, y = {y}")

# 錯誤的解包：變數數量多於元素數量
print("\n--- 錯誤示範：變數太多 ---")
try:
    x, y, z = p  # 變數 3 個，但元素只有 2 個
except ValueError as e:
    print(f"ValueError: {e}")
    print("原因：變數數量 (3) > 元素數量 (2)")

# 另一種錯誤：變數數量少於元素數量
print("\n--- 錯誤示範：變數太少 ---")
try:
    x, = p  # 變數 1 個，但元素有 2 個
except ValueError as e:
    print(f"ValueError: {e}")
    print("原因：變數數量 (1) < 元素數量 (2)")


# 正確的處理方式
print("\n--- 正確的處理方式 ---")

# 方法1: 使用 * 來處理剩餘元素
q = (1, 2, 3, 4, 5)
a, b, *rest = q  # rest 會收集剩餘的元素
print(f"使用 *: a={a}, b={b}, rest={rest}")

# 方法2: 只取需要的元素，忽略剩餘的
first, second = q[:2]  # 使用切片只取前兩個
print(f"使用切片: first={first}, second={second}")

# 方法3: 如果確定元素數量，可以直接解包
r = (10, 20)
m, n = r
print(f"確定數量解包: m={m}, n={n}")

# 解包的應用場景
print("\n--- 解包的應用場景 ---")
print("1. 交換變數值: a, b = b, a")
print("2. 函式回傳多值: x, y = func()")
print("3. 迭代時解包: for x, y in pairs:")
print("4. 處理不定長度序列: first, *rest = items")

# 常見錯誤避免
print("\n--- 常見錯誤避免 ---")
print("1. 檢查序列長度: if len(seq) == expected:")
print("2. 使用 * 處理剩餘: x, *rest = seq")
print("3. 使用切片: x, y = seq[:2]")
print("4. 提供預設值: x, y = seq + (default1, default2)")

