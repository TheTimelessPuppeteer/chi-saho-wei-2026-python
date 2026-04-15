import sys


# 這題輸入量可能很大，使用 sys.stdin.read() 一次讀完整份輸入會比較快。
# 讀進來後用 split() 依空白切開，再全部轉成 int，
# 後面就能像讀陣列一樣，用索引依序取資料。
nums = list(map(int, sys.stdin.read().split()))

# 如果完全沒有輸入，直接結束程式，避免後面索引存取發生錯誤。
if not nums:
    sys.exit(0)

# 第一行有兩個數字：
# N = 函數 f1..fN 的數量
# Q = 接下來操作（更新/查詢）的總筆數
n = nums[0]
q = nums[1]

# 讀取指標 i，代表「下一個要讀的數字位置」。
# nums[0], nums[1] 已讀過，所以從 2 開始。
i = 2

# Fenwick Tree（BIT）儲存的是「某位置是否被翻轉奇數次」。
# 0 代表偶數次（含 0 次）-> 狀態等於原本（增函數）
# 1 代表奇數次 -> 狀態被翻轉（減函數）
# 我們只關心奇偶，因此用 XOR 最自然。
bit = [0] * (n + 1)


def add(pos: int, val: int) -> None:
    """在 Fenwick Tree 的 pos 位置做 XOR 更新。"""

    # Fenwick Tree 的標準單點更新：一路跳到受影響的父節點。
    while pos <= n:
        bit[pos] ^= val
        pos += pos & -pos


def prefix_xor(pos: int) -> int:
    """回傳區間 [1, pos] 的 XOR。"""

    # Fenwick Tree 的前綴查詢：一路往上累積節點值。
    s = 0
    while pos > 0:
        s ^= bit[pos]
        pos -= pos & -pos
    return s


# 收集所有查詢（v=2）的答案。
out = []

for _ in range(q):
    # 每筆操作第一個數字是 v：
    # v=1 -> 單點翻轉
    # v=2 -> 區間查詢
    v = nums[i]
    i += 1

    if v == 1:
        # 操作 1：翻轉第 x 個函數的增減性。
        # 翻轉可視為 0/1 切換，因此等價於 XOR 1。
        x = nums[i]
        i += 1
        add(x, 1)
    else:
        # 操作 2：查詢 [l, r] 複合後是增或減。
        l = nums[i]
        r = nums[i + 1]
        i += 2

        # [l, r] 區間的「翻轉奇偶」可用前綴 XOR 算出：
        # parity = prefix(r) XOR prefix(l-1)
        # parity = 0 -> 區間內減函數個數為偶數 -> 最終為增函數
        # parity = 1 -> 區間內減函數個數為奇數 -> 最終為減函數
        ans = prefix_xor(r) ^ prefix_xor(l - 1)
        out.append(str(ans))


# 依題目格式，每筆查詢答案輸出一行。
print("\n".join(out))
