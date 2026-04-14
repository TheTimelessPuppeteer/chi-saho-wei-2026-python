import sys


def is_jolly(sequence):
    """判斷一個整數序列是否為 Jolly Jumper。"""
    n = len(sequence)

    # n=0 或 n=1 時，相鄰差值集合為空，依定義可視為 Jolly。
    if n <= 1:
        return True

    diffs = set()

    # 計算相鄰兩數絕對差值。
    for i in range(n - 1):
        d = abs(sequence[i] - sequence[i + 1])

        # 合法差值範圍必須在 1..n-1。
        # 若超出範圍可直接判定 Not jolly。
        if d < 1 or d > n - 1:
            return False

        diffs.add(d)

    # 若是 Jolly，差值應恰好覆蓋 1..n-1。
    # 使用 set 後，重複差值不會增加元素數量，
    # 因此只要元素數量不是 n-1 就代表有缺漏或重複。
    return len(diffs) == n - 1


def main() -> None:
    """UVA 10038 主程式。

    輸入是多行直到 EOF；每行格式為：
    n a1 a2 ... an
    輸出每行對應 `Jolly` 或 `Not jolly`。
    """
    out_lines = []

    for line in sys.stdin:
        line = line.strip()
        if not line:
            # 空行直接跳過，避免 split 後資料不足。
            continue

        nums = list(map(int, line.split()))
        n = nums[0]
        sequence = nums[1 : 1 + n]

        out_lines.append("Jolly" if is_jolly(sequence) else "Not jolly")

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()
