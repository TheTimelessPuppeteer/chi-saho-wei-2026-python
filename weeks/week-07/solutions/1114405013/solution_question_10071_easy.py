"""Question 10071 easy 版解答（效能權重 65%）。

使用「三數和 + 兩數和」的分解方式：
1. 先統計所有 a+b+c 的和出現次數
2. 再統計所有 d+e 的和出現次數
3. 對每個 f，累加 abc_count[f - de_sum] * de_count[de_sum]

時間複雜度約 O(N^3)，比六重迴圈好記又有效率。
"""

import sys


def count_six_tuples(values):
    """計算滿足 a+b+c+d+e=f 的六元組數量。"""
    abc_count = {}
    for a in values:
        for b in values:
            for c in values:
                total = a + b + c
                abc_count[total] = abc_count.get(total, 0) + 1

    de_count = {}
    for d in values:
        for e in values:
            total = d + e
            de_count[total] = de_count.get(total, 0) + 1

    count = 0
    for f in values:
        for de_sum, de_times in de_count.items():
            count += de_times * abc_count.get(f - de_sum, 0)

    return count


def solve():
    """讀取輸入、計算答案並輸出。"""
    data = sys.stdin.read().strip().split()
    if not data:
        return

    size = int(data[0])
    values = [int(value) for value in data[1 : 1 + size]]
    sys.stdout.write(str(count_six_tuples(values)))


if __name__ == "__main__":
    solve()
