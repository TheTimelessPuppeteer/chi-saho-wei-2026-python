# U4. heap 為何能高效拿 Top-N（1.4）

# heap（堆積）是一種特殊的樹狀結構，根節點永遠是最小值（最小堆）
# heapq 模組提供 heap 相關操作，能高效取得 Top-N 元素

import heapq

# 範例資料
nums = [5, 1, 9, 2]
print(f"原始列表: {nums}")

# 建立 heap：heapify 會將列表轉換為 heap 結構
h = nums[:]  # 複製一份，避免修改原始列表
heapq.heapify(h)
print(f"heapify 後: {h}")
print(f"h[0] = {h[0]} (永遠是最小值)")

# heappop 每次都會取出目前的最小值，並保持 heap 性質
print("\n--- 逐步 pop 過程 ---")
while h:
    min_val = heapq.heappop(h)
    print(f"pop 出: {min_val}, 剩餘: {h}")

# heap 的核心性質
print("\n--- heap 核心性質 ---")
print("1. h[0] 永遠是當前最小值")
print("2. heappop() 取出最小值後，heap 結構保持完整")
print("3. heapify() 將列表轉為 heap，時間複雜度 O(n)")
print("4. heappop() 時間複雜度 O(log n)")

# Top-N 的高效實現
print("\n--- Top-N 應用 ---")
data = [7, 3, 8, 1, 9, 2, 5, 4, 6]

# 方法1: nlargest - 取得最大的 N 個
top3_largest = heapq.nlargest(3, data)
print(f"最大的 3 個: {top3_largest}")

# 方法2: nsmallest - 取得最小的 N 個
top3_smallest = heapq.nsmallest(3, data)
print(f"最小的 3 個: {top3_smallest}")

# 方法3: 手動建 heap 取 Top-N（適合大量資料）
print("\n--- 手動建 heap 取 Top-N ---")
def top_n_smallest(nums, n):
    if len(nums) <= n:
        return sorted(nums)

    # 使用負數模擬 max-heap（存放最小的 n 個）
    heap = [-x for x in nums[:n]]  # 取前 n 個，負數化
    heapq.heapify(heap)

    for num in nums[n:]:
        if -num > heap[0]:  # 如果 -num > heap[0]，表示 num < -heap[0]（更小）
            heapq.heapreplace(heap, -num)

    # 轉回正數並排序
    return sorted([-x for x in heap])

result = top_n_smallest(data, 3)
print(f"手動實現最小的 3 個: {result}")

# heap vs 排序的效能比較
print("\n--- heap vs 排序效能 ---")
large_data = list(range(1000, 0, -1))  # 1000 個元素，倒序

# 使用 heap 取 Top-10
import time
start = time.time()
top10_heap = heapq.nsmallest(10, large_data)
heap_time = time.time() - start

# 使用排序取 Top-10
start = time.time()
top10_sort = sorted(large_data)[:10]
sort_time = time.time() - start

print(f"heap nlargest: {heap_time:.6f} 秒")
print(f"排序後取前: {sort_time:.6f} 秒")
print(f"heap 約快 {sort_time/heap_time:.1f} 倍")

print("\n--- heap 的應用場景 ---")
print("1. 優先隊列實現")
print("2. Top-K 問題")
print("3. 中位數維護")
print("4. 事件調度")
print("5. 記憶體受限的排序")

