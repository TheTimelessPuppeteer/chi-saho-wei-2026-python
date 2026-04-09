import sys


def find_group_size_easy(s, d):
    current_group = s
    covered_days = 0

    while covered_days < d:
        covered_days += current_group
        if covered_days >= d:
            return current_group
        current_group += 1

    return current_group


def solve():
    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        s, d = map(int, line.split())
        out.append(str(find_group_size_easy(s, d)))

    if out:
        sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()