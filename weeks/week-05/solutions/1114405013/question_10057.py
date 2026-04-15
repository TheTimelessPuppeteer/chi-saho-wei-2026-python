from bisect import bisect_left, bisect_right


def solve(data: str) -> str:
    # 題目是多組測資直到 EOF，因此直接把所有整數讀成陣列後逐組解析。
    nums = list(map(int, data.split()))
    out = []
    i = 0

    while i < len(nums):
        # 每組第一個數字是 n，代表接下來有 n 個整數。
        n = nums[i]
        i += 1

        values = nums[i : i + n]
        i += n

        values.sort()

        # 最小化 |Xi-A| 總和時，A 必位於中位數區間 [low, high]。
        low = values[(n - 1) // 2]
        high = values[n // 2]

        # 第二欄：資料中有多少個 Xi 落在 [low, high]。
        left = bisect_left(values, low)
        right = bisect_right(values, high)
        count = right - left

        # 第三欄：可行的整數 A 有幾個（含端點）。
        ways = high - low + 1

        out.append(f"{low} {count} {ways}")

    return "\n".join(out)


if __name__ == "__main__":
    import sys

    print(solve(sys.stdin.read()))
