import sys


# 讀入整份輸入並用空白切開，再全部轉成整數。
# 輸入格式如下：
# 第一個數字是測資組數 t。
# 每組資料是：r（親戚數）+ r 個門牌號碼。
nums = list(map(int, sys.stdin.read().split()))

# 如果完全沒有輸入，直接結束程式。
if not nums:
    sys.exit(0)

# t: 總共有幾組測試資料。
t = nums[0]

# i: 讀取指標，代表目前處理到 nums 的哪個位置。
# 因為 nums[0] 已經是 t，所以從 1 開始。
i = 1

# out: 收集每組答案，最後一次輸出。
out = []

for _ in range(t):
    # 先讀出這組的親戚數量 r。
    r = nums[i]
    i += 1

    # 依照 r 讀出這組的所有門牌號碼。
    houses = nums[i : i + r]
    i += r

    # 先排序，再取中間位置（中位數）當作 Vito 的住址。
    # 原因：在一維座標上，中位數能讓絕對距離總和最小。
    houses.sort()
    center = houses[r // 2]

    # 計算所有親戚到 center 的距離總和。
    # 距離定義為絕對值 |x - center|。
    total = 0
    for x in houses:
        total += abs(x - center)

    # 將這組答案先轉字串存起來，方便最後用換行輸出。
    out.append(str(total))

# 所有測資處理完後，每組答案輸出一行。
print("\n".join(out))
