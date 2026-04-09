import sys


def count_six_tuples(values):
    abc_count = {}
    for a in values:
        for b in values:
            for c in values:
                total = a + b + c
                abc_count[total] = abc_count.get(total, 0) + 1

    de_count = {}
    for d in values:
        for e in values:
            total = d + e
            de_count[total] = de_count.get(total, 0) + 1

    count = 0
    for f in values:
        for de_sum, de_times in de_count.items():
            count += de_times * abc_count.get(f - de_sum, 0)

    return count


def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    size = int(data[0])
    values = [int(value) for value in data[1 : 1 + size]]
    sys.stdout.write(str(count_six_tuples(values)))


if __name__ == "__main__":
    solve()