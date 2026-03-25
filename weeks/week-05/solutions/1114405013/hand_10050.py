def count_lost_days(n, hartals):
    lost_days = set()

    for h in hartals:
        for day in range(h, n + 1, h):
            if day % 7 in (6, 0):
                continue
            lost_days.add(day)

    return len(lost_days)


def solve():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    t = data[0]
    i = 1
    out = []

    for _ in range(t):
        n = data[i]
        i += 1

        p = data[i]
        i += 1

        hs = data[i : i + p]
        i += p

        out.append(str(count_lost_days(n, hs)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()