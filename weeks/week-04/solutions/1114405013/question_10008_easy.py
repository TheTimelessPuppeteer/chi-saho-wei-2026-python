import sys


def main() -> None:
    """UVA 10008 簡易好記版。

    寫法重點：
    1) 用長度 26 的陣列記錄 A~Z 次數
    2) 逐字掃描，遇到英文字母就轉大寫後累加
    3) 最後依「次數降序、字母升序」排序輸出

    為什麼這版更好記：
    - 不需要 `Counter` 或進階資料結構
    - 核心只靠兩個字元轉換公式
      - `ord(up) - ord("A")`：把字母轉成 0~25 索引
      - `chr(ord("A") + i)`：把 0~25 索引轉回字母
    - 流程固定：讀取 -> 累加 -> 整理 -> 排序 -> 輸出
    """

    # `splitlines()` 會保留「一行一行」的概念，
    # 包含空行（空字串），符合題目輸入型態。
    lines = sys.stdin.read().splitlines()
    if not lines:
        # 沒有任何輸入就直接結束。
        return

    # 第一行是 n，代表後面有幾行要分析。
    # 只取前 n 行，若有額外內容不納入統計。
    n = int(lines[0].strip())
    texts = lines[1 : 1 + n]

    # 固定長度 26 的計數陣列：
    # cnt[0] 對應 A，cnt[1] 對應 B，...，cnt[25] 對應 Z。
    cnt = [0] * 26

    # 逐行、逐字元掃描。
    for line in texts:
        for ch in line:
            # 先轉大寫，讓 'a' 與 'A' 視為同一個字母。
            up = ch.upper()

            # 只統計英文字母 A~Z：
            # - 數字（0~9）
            # - 標點符號（!@#$...）
            # - 空白與其他字元
            # 全部都直接忽略。
            if "A" <= up <= "Z":
                # 例：'A'->0, 'B'->1, ..., 'Z'->25
                idx = ord(up) - ord("A")
                cnt[idx] += 1

    # 將陣列整理成可排序的 (字母, 次數) 清單，
    # 並且只保留「次數 > 0」的字母。
    items = []
    for i in range(26):
        if cnt[i] > 0:
            letter = chr(ord("A") + i)
            items.append((letter, cnt[i]))

    # 排序規則（題目要求）：
    # 1. 次數由大到小  -> 用負號 `-x[1]` 做降序
    # 2. 同次數比字母  -> 用 `x[0]` 做升序
    items.sort(key=lambda x: (-x[1], x[0]))

    # 依格式輸出：<大寫字母><空白><次數>
    # 例如：A 12
    for letter, freq in items:
        print(f"{letter} {freq}")


if __name__ == "__main__":
    main()
