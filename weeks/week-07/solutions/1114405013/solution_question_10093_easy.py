"""Question 10093 easy 版解答。

這版重點是「好理解、好記憶」：
1. 先把每一列可放炮兵的狀態列舉出來
2. 再用逐列 DP 累加最大值
3. DP 只記前一列與前二列，因為垂直攻擊只影響距離 1 與 2
"""

import sys


def build_row_states(cols):
    """建立單列內部不衝突的所有狀態。"""
    states = []
    for state in range(1 << cols):
        # 同列水平距離 1 與 2 不可同時有炮兵。
        if state & (state << 1):
            continue
        if state & (state << 2):
            continue
        states.append(state)
    return states


def solve_grid(grid):
    """計算整張地圖最多可部署的炮兵數量。"""
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    all_states = build_row_states(cols)
    state_guns = {s: s.bit_count() for s in all_states}

    # 把每一列的平原位置轉成 bitmask，P=1, H=0。
    plain_masks = []
    for row in grid:
        mask = 0
        for c, ch in enumerate(row):
            if ch == "P":
                mask |= 1 << c
        plain_masks.append(mask)

    # 過濾出每一列在地形限制下可用的狀態。
    valid_row_states = []
    for r in range(rows):
        candidates = []
        for state in all_states:
            if state & ~plain_masks[r]:
                continue
            candidates.append(state)
        valid_row_states.append(candidates)

    # dp[(prev1, prev2)] = 到目前列為止的最大炮兵數。
    # prev1: 前一列狀態
    # prev2: 前二列狀態
    dp = {(0, 0): 0}

    for r in range(rows):
        new_dp = {}
        for (prev1, prev2), best in dp.items():
            for cur in valid_row_states[r]:
                # 垂直距離 1/2 的同欄位都不能同時放。
                if cur & prev1:
                    continue
                if cur & prev2:
                    continue

                key = (cur, prev1)
                value = best + state_guns[cur]
                if value > new_dp.get(key, -1):
                    new_dp[key] = value
        dp = new_dp

    return max(dp.values()) if dp else 0


def solve():
    """讀取輸入並輸出答案。"""
    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    grid = data[2 : 2 + n]
    grid = [row[:m] for row in grid]

    print(solve_grid(grid))


if __name__ == "__main__":
    solve()
