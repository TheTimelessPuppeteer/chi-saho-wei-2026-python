import sys


nums = list(map(int, sys.stdin.read().split()))

if not nums:
    sys.exit(0)

t = nums[0]
i = 1

ans = []

for _ in range(t):
    n = nums[i]
    i += 1

    p = nums[i]
    i += 1

    lost = set()

    for _ in range(p):
        h = nums[i]
        i += 1

        d = h
        while d <= n:
            if d % 7 != 6 and d % 7 != 0:
                lost.add(d)
            d += h

    ans.append(str(len(lost)))

print("\n".join(ans))