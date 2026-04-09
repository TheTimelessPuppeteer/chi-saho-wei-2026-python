"""Question 10170 解答。

給定 S 與 D，找出第 D 天入住旅行團的人數。
旅行團人數依序為 S, S+1, S+2, ...，且 k 人團住 k 天。

思路：
1. 如果目前考慮到 n 人團，總共覆蓋的天數是：S + (S+1) + ... + n
2. 我們要找最小 n，使這個總和 >= D
3. 因為總和隨 n 單調遞增，所以可用二分搜尋
"""

import sys


def days_sum(s, n):
    """回傳從 s 到 n 的總天數（等差級數和）。

    公式：
    - 項數 count = n - s + 1
    - 總和 = (首項 + 末項) * 項數 / 2
    """
    count = n - s + 1
    return (s + n) * count // 2


def find_group_size(s, d):
    """找最小 n 使 sum(s..n) >= d。

    也就是：第 d 天對應到 n 人團。
    """
    lo = s
    hi = s

    # 先把上界 hi 擴到足夠大，確保答案一定落在 [lo, hi]。
    # 用倍增法可在對數次數內找到上界。
    while days_sum(s, hi) < d:
        hi *= 2

    # 二分搜尋最小可行 n：
    # - 若 sum(s..mid) 已經 >= d，答案在左半邊（含 mid）
    # - 否則答案在右半邊
    while lo < hi:
        mid = (lo + hi) // 2
        if days_sum(s, mid) >= d:
            hi = mid
        else:
            lo = mid + 1

    return lo


def solve():
    """逐行讀入 (S, D)，逐行輸出答案。"""
    out = []

    # 題目輸入直到 EOF，適合直接迭代 sys.stdin。
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        s, d = map(int, line.split())
        out.append(str(find_group_size(s, d)))

    # 若有資料，最後一次性輸出，避免多次 I/O。
    if out:
        sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    # 讓此檔案可以直接當作競賽程式執行。
    solve()
