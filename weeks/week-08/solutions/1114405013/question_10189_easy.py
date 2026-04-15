import sys


def solve_one(grid):
    """更好記版本：逐格掃描，空白格就看 8 個鄰居。

    這個函式只處理「單一地雷圖」，不管 Field 編號。
    輸入：
    - grid: 字串陣列，每個字元是 `*`（地雷）或 `.`（空白）
    輸出：
    - 處理後的字串陣列：地雷保持 `*`，空白改成鄰雷數字
    """
    n = len(grid)
    m = len(grid[0]) if n else 0
    out = []

    # 逐格掃描整張地圖。
    for r in range(n):
        row = []
        for c in range(m):
            if grid[r][c] == "*":
                # 地雷格不需要計算，直接保留星號。
                row.append("*")
                continue

            # 對空白格計算周圍 8 格地雷數。
            cnt = 0

            # 用「框框範圍」寫法取代 8 方向陣列，
            # 比較好記：row 在 r-1..r+1，col 在 c-1..c+1。
            # max/min 用來避免超出邊界（角落/邊緣）。
            for nr in range(max(0, r - 1), min(n, r + 2)):
                for nc in range(max(0, c - 1), min(m, c + 2)):
                    # 本格自己不算鄰居。
                    if nr == r and nc == c:
                        continue
                    if grid[nr][nc] == "*":
                        cnt += 1

            # 空白格最終填入相鄰地雷數（字元形式）。
            row.append(str(cnt))
        out.append("".join(row))

    return out


def main() -> None:
    """UVA 10189 easy 版。

    口訣：
    - 讀 n,m
    - 讀地圖
    - 逐格算鄰雷
    - 依 `Field #X:` 格式輸出

    輸入是多組資料，直到遇到 `0 0` 結束。
    每組輸出之間要空一行。
    """

    # 先把所有行讀進來，並去掉純空白行。
    # 這樣可容忍輸入中夾雜空行。
    lines = [ln.strip() for ln in sys.stdin.read().splitlines() if ln.strip()]
    i = 0
    field_no = 1
    blocks = []

    while i < len(lines):
        # 每組開頭是 n m。
        n, m = map(int, lines[i].split())
        i += 1
        if n == 0 and m == 0:
            # 終止條件，不輸出這組。
            break

        # 接下來 n 行就是地圖內容。
        grid = lines[i : i + n]
        i += n

        solved = solve_one(grid)

        # 組成題目要求的區塊格式：
        # Field #k:
        # <第1行>
        # <第2行>
        block = [f"Field #{field_no}:"] + solved
        blocks.append("\n".join(block))
        field_no += 1

    # 組與組之間需空一行。
    sys.stdout.write("\n\n".join(blocks))


if __name__ == "__main__":
    main()
