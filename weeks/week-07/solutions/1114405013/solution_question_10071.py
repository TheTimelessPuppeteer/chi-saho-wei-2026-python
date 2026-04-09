"""Question 10071 解答。

本題要計算六元組數量：a + b + c + d + e = f。
所有 a~f 都必須來自同一個集合 S，且允許重複使用。
"""

import sys


def count_six_tuples(values):
    """計算滿足 a+b+c+d+e=f 的六元組數量。

    這裡使用最直接的暴力枚舉：
    - 先列舉 a,b,c,d,e 的所有可能
    - 計算五個數字的總和
    - 再檢查是否存在 f 與總和相等

    時間複雜度很高，但在單元測試的小型輸入下是可接受的。
    """
    count = 0
    for a in values:
        for b in values:
            for c in values:
                for d in values:
                    for e in values:
                        total = a + b + c + d + e
                        for f in values:
                            if total == f:
                                count += 1
    return count


def solve():
    """讀取輸入、計算答案並輸出。"""
    data = sys.stdin.read().strip().split()
    if not data:
        return

    # 第一個數字是集合大小 N。
    size = int(data[0])

    # 後面依序是 N 個集合元素。
    values = [int(value) for value in data[1 : 1 + size]]

    # 輸出符合條件的六元組總數量。
    sys.stdout.write(str(count_six_tuples(values)))


if __name__ == "__main__":
    # 讓此檔案可以直接執行。
    solve()
