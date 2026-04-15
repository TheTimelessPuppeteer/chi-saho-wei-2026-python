import sys


nums = list(map(int, sys.stdin.read().split()))

if not nums:
    sys.exit(0)

n = nums[0]
q = nums[1]

i = 2

bit = [0] * (n + 1)


def add(pos: int, val: int) -> None:
    """把位置 pos 的值做 XOR 更新。"""
    while pos <= n:
        bit[pos] ^= val
        pos += pos & -pos


def prefix_xor(pos: int) -> int:
    """計算 1..pos 的 XOR。"""
    s = 0
    while pos > 0:
        s ^= bit[pos]
        pos -= pos & -pos
    return s


out = []

for _ in range(q):
    v = nums[i]
    i += 1

    if v == 1:
        x = nums[i]
        i += 1
        add(x, 1)
    else:
        l = nums[i]
        r = nums[i + 1]
        i += 2

        ans = prefix_xor(r) ^ prefix_xor(l - 1)
        out.append(str(ans))


print("\n".join(out))