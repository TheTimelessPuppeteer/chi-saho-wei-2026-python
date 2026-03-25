"""UVA 10050 簡單版（_easy）

題意精簡：
- 已知模擬天數 n 與每個政黨的罷會週期 h。
- 某政黨會在 h、2h、3h... 天罷會。
- 但每週五、週六是休假日，不算損失工作天。
- 目標是算出「實際損失的工作天數」。

好記口訣：
1) 列出每個政黨的罷會日
2) 週末（五、六）跳過
3) 用 set 去重後計數
"""


def count_lost_days(n, hartals):
    """回傳 n 天內損失的工作天數。

    參數：
    - n: 模擬天數
    - hartals: 各政黨的罷會週期列表

    回傳：
    - 損失工作天數（整數）
    """
    # 使用 set 來紀錄「發生罷會且屬於工作日」的日期。
    # 若多個政黨剛好同一天罷會，set 只會保留一份，避免重複計數。
    lost_days = set()

    # 逐一處理每個政黨的罷會週期 h
    for h in hartals:
        # range(h, n + 1, h) 代表 h、2h、3h... 直到 <= n
        for day in range(h, n + 1, h):
            # 題目規定第 1 天是星期日，所以：
            # - day % 7 == 6 -> 星期五
            # - day % 7 == 0 -> 星期六
            # 這兩天是假日，不列入損失工作天。
            if day % 7 in (6, 0):
                continue

            # 非假日且有罷會，記錄為損失工作天
            lost_days.add(day)

    # set 的元素數量就是損失工作天數
    return len(lost_days)


def solve():
    """讀取題目輸入，輸出每組損失工作天數。

    輸入格式：
    - 第 1 個整數 t：測資組數
    - 每組測資依序為：
      1) n（模擬天數）
      2) p（政黨數）
      3) 接著 p 個整數（各政黨罷會週期）

    輸出格式：
    - 每組輸出一行損失工作天數
    """
    import sys

    # 一次讀完所有輸入並切成整數，方便用索引依序解析
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    # t: 測資數量
    t = data[0]
    # i: 目前讀到 data 的哪個位置
    i = 1
    # out: 暫存每組答案，最後一次輸出
    out = []

    for _ in range(t):
        # 讀取本組天數 n
        n = data[i]
        i += 1

        # 讀取本組政黨數 p
        p = data[i]
        i += 1

        # 讀取接下來 p 個罷會週期
        hs = data[i : i + p]
        i += p

        # 計算本組答案並轉字串收集
        out.append(str(count_lost_days(n, hs)))

    # 每組答案一行輸出
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
