def min_total_distance(addresses):
    arr = sorted(addresses)
    mid = arr[len(arr) // 2]
    return sum(abs(x - mid) for x in arr)


def solve():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        r = data[idx]
        idx += 1
        houses = data[idx : idx + r]
        idx += r
        out.append(str(min_total_distance(houses)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
