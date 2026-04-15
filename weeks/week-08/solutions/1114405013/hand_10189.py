import sys


def solve_one(grid):
    n = len(grid)
    m = len(grid[0]) if n else 0
    out = []

    for r in range(n):
        row = []
        for c in range(m):
            if grid[r][c] == "*":
                row.append("*")
                continue

            cnt = 0
            for nr in range(max(0, r - 1), min(n, r + 2)):
                for nc in range(max(0, c - 1), min(m, c + 2)):
                    if nr == r and nc == c:
                        continue
                    if grid[nr][nc] == "*":
                        cnt += 1
            row.append(str(cnt))
        out.append("".join(row))

    return out


def main() -> None:
    lines = [ln.strip() for ln in sys.stdin.read().splitlines() if ln.strip()]
    i = 0
    field_no = 1
    blocks = []

    while i < len(lines):
        n, m = map(int, lines[i].split())
        i += 1
        if n == 0 and m == 0:
            break

        grid = lines[i : i + n]
        i += n

        solved = solve_one(grid)
        block = [f"Field #{field_no}:"] + solved
        blocks.append("\n".join(block))
        field_no += 1

    sys.stdout.write("\n\n".join(blocks))


if __name__ == "__main__":
    main()