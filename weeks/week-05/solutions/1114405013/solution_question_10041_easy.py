"""UVA 10041 簡單版（-easy）

題目重點：
- 在同一條數線上選一個住址，讓到所有親戚門牌的距離總和最小。

好記口訣：
1) 排序
2) 取中位數
3) 加總距離

原因：
- 在一維數線上，絕對值距離總和在「中位數」位置會最小。
"""


def min_total_distance(addresses):
    """回傳最小總距離。

    參數:
    - addresses: 一組親戚門牌號碼（整數列表）

    回傳:
    - 新家到所有親戚門牌距離總和的最小值
    """
    # 防呆：若傳入空列表，距離總和視為 0
    if not addresses:
        return 0

    # 1) 先排序，方便定位中位數
    arr = sorted(addresses)

    # 2) 取中位數
    #    - 奇數筆：正中間
    #    - 偶數筆：取左中位數或右中位數都可得到相同最小值
    #      這裡用右中位數（len(arr)//2）
    mid = arr[len(arr) // 2]

    # 3) 把每位親戚到中位數的距離加總
    #    abs(x - mid) 代表門牌 x 到新家 mid 的距離
    return sum(abs(x - mid) for x in arr)


def solve():
    """讀入題目格式，輸出每組最小總距離。

    輸入格式（以整數 token 來看）：
    - 第 1 個整數：測試資料組數 t
    - 每組資料：先讀 r，再讀 r 個門牌

    輸出格式：
    - 每組答案一行
    """
    import sys

    # 用 split() 一次讀完整份輸入，不受換行位置影響
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    # t = 測試資料組數
    t = data[0]
    # idx 用來追蹤目前讀到哪個 token
    idx = 1
    # 暫存每組答案，最後再一次輸出
    out = []

    for _ in range(t):
        # 先讀本組親戚數量 r
        r = data[idx]
        idx += 1

        # 依 r 取出本組所有門牌
        houses = data[idx : idx + r]
        idx += r

        # 計算本組最小總距離並轉字串收集
        out.append(str(min_total_distance(houses)))

    # 每組答案換行輸出
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
