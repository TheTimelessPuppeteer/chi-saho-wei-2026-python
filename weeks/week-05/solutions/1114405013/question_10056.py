def win_probability(n: int, p: float, i: int) -> float:
    # p=0 代表永遠不會有人成功，指定玩家勝率必為 0。
    if p == 0.0:
        return 0.0

    # 指定玩家在某一輪勝利的機率：
    # 前 i-1 位都失敗，再由第 i 位成功 => (1-p)^(i-1) * p
    first_cycle_hit = (1.0 - p) ** (i - 1) * p

    # 一整輪（N 位玩家）都沒人成功的機率。
    all_fail_cycle = (1.0 - p) ** n

    # 幾何級數求和：
    # first_cycle_hit * (1 + all_fail_cycle + all_fail_cycle^2 + ...)
    # = first_cycle_hit / (1 - all_fail_cycle)
    return first_cycle_hit / (1.0 - all_fail_cycle)


def solve(data: str) -> str:
    lines = data.strip().splitlines()
    if not lines:
        return ""

    s = int(lines[0].strip())
    out = []

    for idx in range(1, s + 1):
        n_str, p_str, i_str = lines[idx].split()
        n = int(n_str)
        p = float(p_str)
        i = int(i_str)

        ans = win_probability(n, p, i)
        out.append(f"{ans:.4f}")

    return "\n".join(out)


if __name__ == "__main__":
    import sys

    print(solve(sys.stdin.read()))
