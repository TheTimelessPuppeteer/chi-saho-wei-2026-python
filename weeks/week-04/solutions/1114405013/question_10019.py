import sys


def main() -> None:
    """UVA 10019（依題敘為 Hashmat 差值題）的解法。

    題目要點：
    - 每行輸入有兩個整數，代表兩方士兵數量。
    - 需要輸出兩者的「正差值」。
    - 輸入通常是多行直到 EOF，所以要逐行處理。
    """

    # 一次讀完整份輸入，使用 split() 可自動忽略多餘空白與空行。
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    out_lines = []

    # 兩個 token 為一組 (a, b)，計算絕對差值 |a - b|。
    # 題目給到接近 2^63，Python int 可直接處理大整數。
    for i in range(0, len(tokens), 2):
        a = int(tokens[i])
        b = int(tokens[i + 1])
        out_lines.append(str(abs(a - b)))

    # 每組結果各佔一行。
    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()
