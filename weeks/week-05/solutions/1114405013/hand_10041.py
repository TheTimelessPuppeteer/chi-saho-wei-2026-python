import sys


nums = list(map(int, sys.stdin.read().split()))

if not nums:
    sys.exit(0)

t = nums[0]
i = 1  
out = []

for _ in range(t):
    r = nums[i]
    i += 1

    houses = nums[i : i + r]
    i += r

    houses.sort()
    center = houses[r // 2]

    total = 0
    for x in houses:
        total += abs(x - center)

    out.append(str(total))

print("\n".join(out))