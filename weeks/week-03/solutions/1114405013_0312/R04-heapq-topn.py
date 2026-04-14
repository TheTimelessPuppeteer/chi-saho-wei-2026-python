# R4. heapq 取 Top-N（1.4）
# heapq 模組實現了小根堆，可以快速取得前幾大或前幾小的元素。
# 下面示範 nlargest、nsmallest 與手動轉 heap 的操作。

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print("原始 nums:", nums)
# 取出最大的三個數字
top3 = heapq.nlargest(3, nums)
print("最大三個值 ->", top3)
# 取出最小的三個數字
bottom3 = heapq.nsmallest(3, nums)
print("最小三個值 ->", bottom3)

# 當元素是字典時，可以用 key 參數指定比較依據。
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'GOOG', 'shares': 200, 'price': 200.0},
]
cheapest = heapq.nsmallest(1, portfolio, key=lambda s: s['price'])
print("最便宜的股票 ->", cheapest)

# heapify 將列表原地轉換為 heap 結構
heap = list(nums)
print("複製 nums 後的列表", heap)
heapq.heapify(heap)
print("heapify 後的內容 (heap 頂在 index 0):", heap)
# heappop 會移除並回傳最小元素
minval = heapq.heappop(heap)
print("heappop 取出最小值", minval)
print("pop 後的 heap", heap)

# 解說要點：
# - heapq.nlargest/nsmallest 內部使用 heap，只需 O(N log k) 而非排序 O(N log N)。
# - 如果使用 key，程式會對每個元素計算 key() 再比較。
# - heapify 是 O(N) 的操作，可用在需要持續彈出最小值時。
# - heappop 只適用於最小元素；若要最大，須將值取負或使用 nlargest。

