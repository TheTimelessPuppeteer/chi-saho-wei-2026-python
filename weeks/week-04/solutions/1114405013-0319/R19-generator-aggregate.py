# R19. 轉換+聚合：生成器表達式（1.19）

# 生成器表達式可以用於聚合操作，節省記憶體且效能良好

# 範例1: 計算平方和
# sum(x * x for x in nums) 使用生成器表達式計算每個數字的平方然後求和
nums = [1, 2, 3]
square_sum = sum(x * x for x in nums)
print(f"平方和: {square_sum}")  # 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14

# 範例2: 將 tuple 元素轉字串並用逗號連接
# ','.join(str(x) for x in s) 先將每個元素轉成字串，再用逗號連接
s = ('ACME', 50, 123.45)
joined_str = ','.join(str(x) for x in s)
print(f"連接字串: {joined_str}")

# 範例3: 從投資組合中找最小股份數量
# min(s['shares'] for s in portfolio) 使用生成器取出所有股份數量，找最小值
portfolio = [
    {'name': 'AOL', 'shares': 20},
    {'name': 'YHOO', 'shares': 75}
]
min_shares = min(s['shares'] for s in portfolio)
print(f"最小股份: {min_shares}")

# 範例4: 使用 key 參數找完整記錄
# min(portfolio, key=lambda s: s['shares']) 找股份數量最小的完整記錄
min_stock = min(portfolio, key=lambda s: s['shares'])
print(f"股份最少的股票: {min_stock}")

# 其他聚合函式示範
print(f"\n--- 其他聚合操作 ---")
print(f"總股份數: {sum(s['shares'] for s in portfolio)}")
print(f"平均股份: {sum(s['shares'] for s in portfolio) / len(portfolio)}")
print(f"最大股份: {max(s['shares'] for s in portfolio)}")
print(f"股份數量列表: {list(s['shares'] for s in portfolio)}")

# 生成器 vs 列表的效能比較
print(f"\n--- 生成器 vs 列表 ---")
import sys

# 如果用列表推導式，會建立完整列表
list_squares = [x * x for x in range(1000)]
print(f"列表推導式記憶體使用: {sys.getsizeof(list_squares)} bytes")

# 生成器只在需要時計算
gen_squares = (x * x for x in range(1000))
print(f"生成器表達式記憶體使用: {sys.getsizeof(gen_squares)} bytes")

# 但結果相同
print(f"列表結果: {sum(list_squares)}")
print(f"生成器結果: {sum(gen_squares)}")

print(f"\n--- 生成器表達式優勢 ---")
print("1. 節省記憶體（不建立中間列表）")
print("2. 適合大型資料處理")
print("3. 可以直接傳給聚合函式")
print("4. 支援鏈式操作")

