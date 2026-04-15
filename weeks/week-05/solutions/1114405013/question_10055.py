class FenwickXor:
    """Fenwick Tree（Binary Indexed Tree），這裡用 XOR 做前綴運算。"""

    def __init__(self, n: int) -> None:
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx: int, val: int) -> None:
        # 單點更新：把位置 idx 與 val 做 XOR。
        while idx <= self.n:
            self.bit[idx] ^= val
            idx += idx & -idx

    def prefix_xor(self, idx: int) -> int:
        # 查詢 1..idx 的 XOR。
        res = 0
        while idx > 0:
            res ^= self.bit[idx]
            idx -= idx & -idx
        return res

    def range_xor(self, left: int, right: int) -> int:
        # 區間 XOR = prefix(right) XOR prefix(left-1)
        return self.prefix_xor(right) ^ self.prefix_xor(left - 1)


def solve(data: str) -> str:
    # 以空白切開輸入，全部轉成整數後用索引依序讀取。
    nums = list(map(int, data.split()))
    if not nums:
        return ""

    n = nums[0]
    q = nums[1]
    i = 2

    # 初始時所有函數都是增函數（狀態 0）。
    # 若翻轉一次就變成 1（減函數），再翻轉一次回到 0。
    # 因此用 XOR（0/1）非常適合表示狀態。
    fw = FenwickXor(n)

    out = []
    for _ in range(q):
        v = nums[i]
        i += 1

        if v == 1:
            # 操作 1：翻轉第 x 個函數狀態（等同 XOR 1）。
            x = nums[i]
            i += 1
            fw.add(x, 1)
        else:
            # 操作 2：查詢 [l, r] 區間函數複合後的增減性。
            l = nums[i]
            r = nums[i + 1]
            i += 2

            # 區間內減函數數量「奇數」-> 最終為減函數（輸出 1）
            # 區間內減函數數量「偶數」-> 最終為增函數（輸出 0）
            out.append(str(fw.range_xor(l, r)))

    return "\n".join(out)


if __name__ == "__main__":
    import sys

    print(solve(sys.stdin.read()))
