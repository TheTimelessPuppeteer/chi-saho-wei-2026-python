import sys


def solve_field(grid, n, m):
    """計算單一地雷圖的輸出內容。"""
    result = []

    # 八方向偏移量（上、下、左、右、四個斜角）。
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    for r in range(n):
        row_chars = []
        for c in range(m):
            if grid[r][c] == "*":
                # 地雷格維持星號。
                row_chars.append("*")
                continue

            # 空白格要統計周圍 8 格有幾個地雷。
            mine_count = 0
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == "*":
                    mine_count += 1

            row_chars.append(str(mine_count))

        result.append("".join(row_chars))

    return result


def main() -> None:
    """UVA 10189 Minesweeper 主程式。

    輸入多組資料，每組以 n m 開頭，遇到 0 0 結束。
    輸出格式需包含 `Field #X:`，且組與組之間要空一行。
    """
    lines = iter(sys.stdin.read().splitlines())

    field_no = 1
    outputs = []

    for line in lines:
        line = line.strip()
        if not line:
            # 略過輸入中的空白行。
            continue

        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break

        grid = []
        for _ in range(n):
            # 每行保留原始字元，題目保證長度為 m。
            grid.append(next(lines).rstrip("\n"))

        solved = solve_field(grid, n, m)

        block = [f"Field #{field_no}:"]
        block.extend(solved)
        outputs.append("\n".join(block))
        field_no += 1

    # 題目要求各組輸出之間空一行。
    sys.stdout.write("\n\n".join(outputs))


if __name__ == "__main__":
    main()
