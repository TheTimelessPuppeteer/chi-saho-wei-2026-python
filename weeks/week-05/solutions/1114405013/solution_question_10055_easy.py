"""Question 10055 簡單版（_easy）

這份是「好記憶」版本，重點放在直觀與手打友善：

1) 用陣列記錄每個函數目前狀態（增=0、減=1）
2) 操作 1（反轉）直接做 state[i] ^= 1
3) 操作 2（查詢）對區間 [L, R] 加總後取奇偶

數學關係：
- 區間內減函數數量為偶數 -> 複合結果是增函數（輸出 0）
- 區間內減函數數量為奇數 -> 複合結果是減函數（輸出 1）

注意：
- 這是 easy 版，查詢時用切片加總，時間複雜度較高。
- 若要應對超大資料，建議使用 Fenwick Tree 版本。
"""


def process_queries(n, queries):
    """處理操作並回傳所有查詢結果（0/1）。

    參數：
    - n: 函數數量（f_1 ~ f_n）
    - queries: 操作序列
      - (1, i)       : 反轉第 i 個函數
      - (2, L, R)    : 查詢區間 [L, R] 的複合函數增減性

    回傳：
    - 所有操作 2 的結果列表（元素只會是 0 或 1）
    """
    # state[i] = 0 表示 f_i 是增函數；state[i] = 1 表示 f_i 是減函數
    # 由於題目索引從 1 開始，state[0] 保留不用，避免索引換算。
    state = [0] * (n + 1)

    # results 只收集查詢操作（op=2）的答案
    results = []

    for query in queries:
        op = query[0]

        if op == 1:
            # 反轉指定函數：0 <-> 1
            # XOR 1 是最短、最好記的寫法。
            i = query[1]
            state[i] ^= 1
        else:
            # 區間 [L, R] 內「減函數個數」的奇偶決定答案：
            # 奇數 -> 1（減函數），偶數 -> 0（增函數）
            _, left, right = query

            # 切片加總是 easy 版最直觀的作法
            parity = sum(state[left : right + 1]) % 2
            results.append(parity)

    return results


def solve():
    """讀取題目輸入並輸出查詢結果。

    輸入格式：
    - 第一行：N Q
    - 接著 Q 行：
      - 1 i
      - 2 L R

    輸出格式：
    - 每個查詢操作（2 L R）輸出一行 0 或 1
    """
    import sys

    # 用 split() 直接拿所有 token，可忽略換行位置差異
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    # 讀取 N（函數數量）與 Q（操作數）
    n = data[0]
    q = data[1]

    # idx 追蹤目前解析到哪個 token
    idx = 2
    queries = []

    for _ in range(q):
        # 先讀操作種類 op（1 或 2）
        op = data[idx]
        idx += 1

        if op == 1:
            # 操作 1：只需要一個參數 i
            i = data[idx]
            idx += 1
            queries.append((1, i))
        else:
            # 操作 2：需要兩個參數 L、R
            left = data[idx]
            right = data[idx + 1]
            idx += 2
            queries.append((2, left, right))

    # 計算並輸出所有查詢結果（每筆一行）
    outputs = process_queries(n, queries)
    sys.stdout.write("\n".join(map(str, outputs)))


if __name__ == "__main__":
    solve()
