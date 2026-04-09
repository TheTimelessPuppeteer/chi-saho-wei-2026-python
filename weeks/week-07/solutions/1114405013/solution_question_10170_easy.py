"""Question 10170 easy 版解答。

這版刻意用最直觀、最好記的寫法：
- 從 S 人團開始，累加每團住宿天數
- 當累加天數第一次 >= D 時，當前團人數就是答案

題目情境對應：
- S 人團會連續住 S 天
- 下一團人數 +1，會住更多天
- 所以我們只要依序把每團「貢獻的天數」加起來，
  累加到第 D 天時，就知道當天是哪個團在住
"""

import sys


def find_group_size_easy(s, d):
    """用直觀迴圈找第 d 天的旅行團人數。

    參數：
    - s: 第一個旅行團的人數
    - d: 要查詢的第 d 天

    回傳：
    - 第 d 天正在入住的旅行團人數
    """

    # current_group 代表「目前正在處理哪一團」。
    current_group = s

    # covered_days 代表「前面已經被這些旅行團覆蓋了幾天」。
    covered_days = 0

    # 只要還沒覆蓋到第 d 天，就繼續往下一團推進。
    while covered_days < d:
        # 目前這一團會再多覆蓋 current_group 天。
        covered_days += current_group

        # 如果累加後已經包含第 d 天，答案就是 current_group。
        if covered_days >= d:
            return current_group

        # 否則換下一團（人數 +1）。
        current_group += 1

    # 理論上 while 內會 return，這裡保留作為防呆回傳。
    return current_group


def solve():
    """逐行讀取 (S, D) 並輸出答案。

    輸入到 EOF 結束，所以用 for line in sys.stdin 逐行處理。
    """
    out = []

    # 題目可能有多筆測資，每行一組 S、D。
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        # 解析一筆查詢。
        s, d = map(int, line.split())

        # 計算答案後先存起來，最後一次性輸出。
        out.append(str(find_group_size_easy(s, d)))

    # 若有結果，就用換行連接輸出。
    if out:
        sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    # 讓檔案可直接作為程式執行。
    solve()
