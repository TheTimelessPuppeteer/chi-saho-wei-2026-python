import sys


def main() -> None:
    """UVA 10019 超好記版本。

    口訣：
    - 一行讀一組
    - 拆成兩個整數
    - 印出絕對差值 abs(a - b)
    """

    # 直接逐行讀 stdin，可自然支援「讀到 EOF」的題型。
    for line in sys.stdin:
        # 去掉前後空白；若是空行就跳過。
        line = line.strip()
        if not line:
            continue

        # 每行應有兩個整數（順序不固定）。
        a, b = map(int, line.split())

        # 題目要正差值，所以使用絕對值。
        print(abs(a - b))


if __name__ == "__main__":
    main()
