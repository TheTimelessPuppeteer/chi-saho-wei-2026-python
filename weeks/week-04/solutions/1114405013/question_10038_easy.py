import sys


def is_jolly_easy(seq):
    """布林陣列版 Jolly 判斷（好背版）。

    口訣：
    1) 算每個相鄰差值
    2) 在 seen[差值] 做標記
    3) 1..n-1 全部有標記就是 Jolly
    """
    n = len(seq)

    # 長度 0 或 1 時，沒有相鄰元素可比較，視為 Jolly。
    if n <= 1:
        return True

    # seen[d] 代表差值 d 是否出現過。
    # 差值只會用到 1..n-1，所以開 n 格最方便（0 不用）。
    seen = [False] * n

    for i in range(1, n):
        d = abs(seq[i] - seq[i - 1])

        # 合法差值必須在 1..n-1，超出範圍可直接失敗。
        if d < 1 or d >= n:
            return False

        seen[d] = True

    # 必須每個差值 1..n-1 都出現過，缺任何一個都不是 Jolly。
    for d in range(1, n):
        if not seen[d]:
            return False

    return True


def main() -> None:
    """UVA 10038 簡易版主程式。

    輸入每行格式：
    n a1 a2 ... an
    輸出：Jolly 或 Not jolly
    """
    out = []

    # 多組測資直到 EOF。
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        nums = list(map(int, line.split()))
        n = nums[0]
        seq = nums[1 : 1 + n]

        out.append("Jolly" if is_jolly_easy(seq) else "Not jolly")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
