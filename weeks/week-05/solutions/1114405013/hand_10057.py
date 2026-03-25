def analyze_numbers(values):
    values.sort()
    n = len(values)

    low = values[(n - 1) // 2]
    high = values[n // 2]

    a = low

    count = sum(1 for x in values if low <= x <= high)

    ways = high - low + 1

    return a, count, ways


def solve():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    i = 0
    out = []

    while i < len(data):
        n = data[i]
        i += 1

        numbers = data[i : i + n]
        i += n

        a, count, ways = analyze_numbers(numbers)
        out.append(f"{a} {count} {ways}")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
