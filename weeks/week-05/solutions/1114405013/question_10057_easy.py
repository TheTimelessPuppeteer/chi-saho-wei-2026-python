import bisect
import sys


# 這題的輸入是「多組測資直到 EOF」，
# 每組格式是：先給 n，再給 n 個整數。
#
# 為了讓程式簡單好記，我們一次把所有整數讀進 nums，
# 然後用指標 i 逐組往後解析。
nums = list(map(int, sys.stdin.read().split()))

# i: 目前讀到 nums 的哪個位置。
i = 0

# out: 收集每組答案字串，最後再一次輸出。
out = []

while i < len(nums):
    # 每組第一個數字是 n，代表接下來有 n 個整數。
    n = nums[i]
    i += 1

    # 取出這組的 n 個數值。
    arr = nums[i : i + n]
    i += n

    # 先排序，因為最佳 A 會落在中位數區間，
    # 中位數相關位置必須依排序後陣列來取。
    arr.sort()

    # low / high 為中位數區間端點：
    # - n 為奇數：low == high（唯一中位數）
    # - n 為偶數：low 與 high 是中間兩個值
    # 使總距離最小的整數 A 會落在 [low, high] 之間。
    low = arr[(n - 1) // 2]
    high = arr[n // 2]

    # 第二欄要輸出「資料中有多少個 Xi 可以當作最小值解的一部分」，
    # 等價於計算有多少個 Xi 落在 [low, high]。
    #
    # bisect_left(arr, low)  : 第一個 >= low 的位置
    # bisect_right(arr, high): 第一個 > high 的位置
    # 兩者相減就是區間元素個數。
    left = bisect.bisect_left(arr, low)
    right = bisect.bisect_right(arr, high)
    count = right - left

    # 第三欄是「最小值可由幾個不同整數 A 達成」。
    # 因為 A 可在 [low, high]，且 A 必須是整數，
    # 所以個數為 high - low + 1（含端點）。
    ways = high - low + 1

    # 第一欄輸出最小可行 A（題目慣例輸出 low）。
    out.append(f"{low} {count} {ways}")


# 依序輸出所有測資答案，每組一行。
print("\n".join(out))
