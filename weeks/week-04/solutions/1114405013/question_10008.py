import sys
from collections import Counter


def main() -> None:
    # 一次讀入全部輸入並保留成「逐行」資料。
    # 這樣可以正確處理題目提到的空白行（空字串行）。
    rows = sys.stdin.read().splitlines()
    if not rows:
        # 沒有輸入時直接結束，避免後續存取 rows[0] 失敗。
        return

    # 第一行是要分析的行數 n；後面取前 n 行作為密文內容。
    # 若輸入行數比 n 多，超出部分依題意不需要處理。
    n = int(rows[0].strip())
    texts = rows[1 : 1 + n]

    # 統計英文字母出現次數：
    # - 不分大小寫，先轉成大寫再累加
    # - 只統計 A~Z，其餘字元（數字、符號、空白）全部忽略
    counts = Counter()
    for line in texts:
        for ch in line:
            up = ch.upper()
            if "A" <= up <= "Z":
                counts[up] += 1

    # 排序規則（題目核心）：
    # 1. 先比出現次數：高者在前（降序）
    # 2. 若次數相同：按字母序 A~Z（升序）
    # 因此 key 寫成 (-次數, 字母)。
    items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

    # 依題目格式輸出，每行為：
    # <大寫字母><空白><次數>
    # 例如：A 12
    for letter, freq in items:
        print(f"{letter} {freq}")


if __name__ == "__main__":
    main()
