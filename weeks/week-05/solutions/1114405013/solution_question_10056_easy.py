"""UVA 10056 簡單版（_easy）

題意（白話）：
- 有 n 位玩家，依序 1 -> 2 -> ... -> n 輪流嘗試。
- 每位玩家每次嘗試成功機率都一樣，都是 p。
- 只要有人成功，遊戲立刻結束。
- 問：第 i 位玩家「最終成為贏家」的機率是多少？

好記口訣（閉式公式）：
前面都失敗 * 自己成功 / 一輪至少有人成功

公式：
P(i) = ((1 - p)^(i - 1) * p) / (1 - (1 - p)^n)

這份 _easy 版本重點是：
- 程式最短
- 步驟最直覺
- 適合考前快速背誦
"""


def win_probability(n, p, i):
    """回傳第 i 位玩家最終獲勝機率。

    參數：
    - n: 玩家總數
    - p: 單次嘗試成功機率
    - i: 玩家編號（從 1 開始）

    計算概念：
    1) 第 i 位在某一輪成功：前 i-1 位失敗，自己成功
       => (1-p)^(i-1) * p
    2) 一整輪沒人成功機率：
       => (1-p)^n
    3) 第 i 位可能在第 1 輪、第 2 輪... 才成功，形成等比級數
       最後可化成閉式解。
    """
    # p=0 代表永遠不會成功，所有玩家勝率都是 0
    if p == 0.0:
        return 0.0

    # q: 單次嘗試失敗機率
    q = 1.0 - p

    # 分子：第 i 位在「某一輪」成功的機率
    numerator = (q ** (i - 1)) * p

    # 分母：一整輪「至少有一人成功」的機率
    denominator = 1.0 - (q**n)

    # 閉式解（等比級數總和）
    return numerator / denominator


def solve():
    """讀取輸入並輸出每組答案（四位小數）。

    輸入格式：
    - 第一個整數 t：測試資料筆數
    - 接著每筆資料 3 個值：n、p、i

    輸出格式：
    - 每筆結果輸出一行
    - 固定格式到小數點後四位
    """
    import sys

    # 一次讀完輸入後切成 token，可避免換行格式差異造成解析困難
    data = sys.stdin.read().split()
    if not data:
        return

    # t: 測資筆數
    t = int(data[0])

    # idx: 目前讀到的 token 位置
    idx = 1

    # 暫存每筆答案，最後一次輸出
    out = []

    for _ in range(t):
        # 每組資料為 n, p, i
        n = int(data[idx])
        p = float(data[idx + 1])
        i = int(data[idx + 2])
        idx += 3

        # 題目要求輸出四位小數
        out.append(f"{win_probability(n, p, i):.4f}")

    # 各組答案換行輸出
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
