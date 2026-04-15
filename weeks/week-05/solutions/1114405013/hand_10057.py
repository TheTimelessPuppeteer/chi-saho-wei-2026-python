import bisect
import sys

nums = list(map(int, sys.stdin.read().split()))

i = 0
out = []

while i < len(nums):
    n = nums[i]
    i += 1

    arr = nums[i : i + n]
    i += n

    arr.sort()

    low = arr[(n - 1) // 2]
    high = arr[n // 2]

    left = bisect.bisect_left(arr, low)
    right = bisect.bisect_right(arr, high)
    count = right - left

    ways = high - low + 1

    out.append(f"{low} {count} {ways}")


print("\n".join(out))
