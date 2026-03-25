"""UVA 10057 簡單版（_easy）

好記重點：
1) 先排序
2) 中位數區間是 [low, high]
3) 答案直接是：
   - a = low
   - count = 有幾個原始數值落在 [low, high]
   - ways = high - low + 1
"""


def analyze_numbers(values):
    """回傳 (a, count, ways)。"""
    values.sort()
    n = len(values)

    # 中位數區間的左右端點
    low = values[(n - 1) // 2]
    high = values[n // 2]

    # 最小可行 A
    a = low

    # 原始資料中，落在最優區間 [low, high] 的數量
    count = sum(1 for x in values if low <= x <= high)

    # 可行 A 的整數個數
    ways = high - low + 1

    return a, count, ways


def solve():
    """讀取多組資料並輸出每組 a count ways。"""
    import sys

    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    i = 0
    out = []

    # UVA 10057 的輸入是：反覆出現 n，後面接 n 個數字，直到 EOF
    while i < len(data):
        n = data[i]
        i += 1

        numbers = data[i : i + n]
        i += n

        a, count, ways = analyze_numbers(numbers)
        out.append(f"{a} {count} {ways}")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
