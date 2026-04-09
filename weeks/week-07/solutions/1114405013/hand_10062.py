import sys


def reconstruct_order(smaller_counts):
    size = len(smaller_counts) + 1
    counts = [0] + list(smaller_counts)

    answer = [0] * size
    available = list(range(1, size + 1))
    for index in range(size - 1, -1, -1):
        answer[index] = available.pop(counts[index])

    return answer


def solve():

    data = sys.stdin.read().strip().split()
    if not data:
        return

    size = int(data[0])

    smaller_counts = [int(value) for value in data[1 : 1 + size - 1]]

    answer = reconstruct_order(smaller_counts)

    sys.stdout.write("\n".join(str(value) for value in answer))


if __name__ == "__main__":
    solve()
