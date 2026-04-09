"""UVA 10062 對應作業解答。

根據每個位置前方有多少頭較小編號的乳牛，
重建整個隊伍的原始排列。
"""

from __future__ import annotations

import sys


class FenwickTree:
    """支援前綴和與第 k 小可用編號查詢。"""

    def __init__(self, size: int) -> None:
        self.size = size
        self.tree = [0] * (size + 1)

    def add(self, index: int, delta: int) -> None:
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def prefix_sum(self, index: int) -> int:
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total

    def find_kth(self, kth: int) -> int:
        """找出目前第 kth 小的可用編號。"""
        index = 0
        bit = 1
        while bit << 1 <= self.size:
            bit <<= 1

        while bit > 0:
            next_index = index + bit
            if next_index <= self.size and self.tree[next_index] < kth:
                kth -= self.tree[next_index]
                index = next_index
            bit >>= 1

        return index + 1


def reconstruct_order(smaller_counts: list[int]) -> list[int]:
    """由每個位置前方較小編號的數量重建排列。"""
    size = len(smaller_counts) + 1
    counts = [0] + smaller_counts
    answer = [0] * size

    fenwick = FenwickTree(size)
    for number in range(1, size + 1):
        fenwick.add(number, 1)

    for index in range(size - 1, -1, -1):
        kth = counts[index] + 1
        answer[index] = fenwick.find_kth(kth)
        fenwick.add(answer[index], -1)

    return answer


def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return

    size = int(data[0])
    smaller_counts = [int(value) for value in data[1 : 1 + size - 1]]
    answer = reconstruct_order(smaller_counts)
    sys.stdout.write("\n".join(str(value) for value in answer))


if __name__ == "__main__":
    solve()
