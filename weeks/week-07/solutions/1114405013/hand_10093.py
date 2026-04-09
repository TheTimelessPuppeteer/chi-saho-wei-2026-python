import sys


def build_row_states(cols):
    states = []
    for state in range(1 << cols):
        if state & (state << 1):
            continue
        if state & (state << 2):
            continue
        states.append(state)
    return states


def solve_grid(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    all_states = build_row_states(cols)
    state_guns = {s: s.bit_count() for s in all_states}

    plain_masks = []
    for row in grid:
        mask = 0
        for c, ch in enumerate(row):
            if ch == "P":
                mask |= 1 << c
        plain_masks.append(mask)

    valid_row_states = []
    for r in range(rows):
        candidates = []
        for state in all_states:
            if state & ~plain_masks[r]:
                continue
            candidates.append(state)
        valid_row_states.append(candidates)

    dp = {(0, 0): 0}

    for r in range(rows):
        new_dp = {}
        for (prev1, prev2), best in dp.items():
            for cur in valid_row_states[r]:
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