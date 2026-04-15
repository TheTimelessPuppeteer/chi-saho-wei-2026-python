import math
import sys


def min_b_plus_c(a: int) -> int:
    """計算滿足題式時，最小的 b + c。

    由
        arctan(1/a) = arctan(1/b) + arctan(1/c)
    可推導為
        (b - a)(c - a) = a^2 + 1

    設 n = a^2 + 1，令 d = b - a，則 d 必為 n 的正因數，且
        c - a = n / d
    因此
        b + c = 2a + d + n/d

    要讓 d + n/d 最小，d 應盡量接近 sqrt(n)。
    """
    n = a * a + 1
    root = math.isqrt(n)

    # 從 sqrt(n) 往下找第一個可整除的因數，
    # 該因數對應的 d + n/d 會最小。
    for d in range(root, 0, -1):
        if n % d == 0:
            q = n // d
            return 2 * a + d + q

    # 理論上不會到這裡（d=1 一定可整除）。
    return 2 * a + 1 + n


def main() -> None:
    """QUESTION-10193 主程式。"""
    data = sys.stdin.read().split()
    if not data:
        return

    a = int(data[0])
    print(min_b_plus_c(a))


if __name__ == "__main__":
    main()
