"""Question 10093 解答。

題意重點：
1. 地圖是 N x M，`P` 可放炮兵、`H` 不可放。
2. 兩支炮兵不能互相攻擊。
3. 攻擊規則可簡化為：
   - 同一列：左右距離 1 或 2 都衝突
   - 同一欄：上下距離 1 或 2 都衝突

解法概念：
- 由於 M <= 10，很適合用「位元狀態」表示一整列的放置情況。
- 再用 DP 逐列轉移，狀態只需記住前一列與前二列，
  因為垂直衝突只會影響到距離 1 與 2 的列。
"""

import sys


def generate_row_states(width):
    """產生單列可行狀態（忽略地形）。

    一個整數 state 的二進位表示代表該列各欄是否放炮兵：
    - bit = 1 表示該欄放炮兵
    - bit = 0 表示不放

    本函式只先處理「同一列內部」衝突，
    所以會過濾掉含有距離 1 或 2 衝突的 state。
    """
    states = []
    for state in range(1 << width):
        # 同一列中，左右相鄰與隔一格都會互相攻擊。
        if state & (state << 1):
            continue
        if state & (state << 2):
            continue
        states.append(state)
    return states


def max_artillery(grid):
    """回傳可放置的最大炮兵數量。

    DP 狀態定義：
    - dp[(prev1, prev2)] = 已處理到目前列時，
      其中前一列狀態為 prev1、前二列狀態為 prev2 的最大炮兵數。
    """
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    # 所有「單列內部不衝突」的候選狀態。
    all_states = generate_row_states(cols)

    # 每個狀態含有幾支炮兵，先預算好避免重複計算。
    bit_count = {state: state.bit_count() for state in all_states}

    # plain_masks[r]：第 r 列可放置位置（P 為 1，H 為 0）
    plain_masks = []
    for row in grid:
        mask = 0
        for c, ch in enumerate(row):
            if ch == "P":
                mask |= 1 << c
        plain_masks.append(mask)

    # 每一列在地形限制下的可行狀態。
    # 也就是：這列為 H 的欄位一定不能出現在 state 中。
    row_states = []
    for r in range(rows):
        valid = []
        for state in all_states:
            if state & ~plain_masks[r]:
                continue
            valid.append(state)
        row_states.append(valid)

    # 初始時，前一列與前二列都視為空列（狀態 0），
    # 最大值為 0。
    dp = {(0, 0): 0}

    for r in range(rows):
        next_dp = {}
        for (prev1, prev2), value in dp.items():
            for cur in row_states[r]:
                # 垂直距離 1 與 2 不能同欄同時放。
                # cur 與 prev1 衝突 -> 距離 1
                # cur 與 prev2 衝突 -> 距離 2
                if cur & prev1:
                    continue
                if cur & prev2:
                    continue

                # 處理完本列後，下一輪的前一列會變成 cur，
                # 下一輪的前二列會變成現在的 prev1。
                key = (cur, prev1)
                candidate = value + bit_count[cur]
                if candidate > next_dp.get(key, -1):
                    next_dp[key] = candidate

        dp = next_dp

    return max(dp.values()) if dp else 0


def solve():
    """讀取輸入並輸出最大可部署數。"""
    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    start = 2
    grid = data[start : start + n]

    # 防呆：若輸入行長不足，仍以目前讀到內容處理。
    grid = [row[:m] for row in grid]

    print(max_artillery(grid))


if __name__ == "__main__":
    solve()
