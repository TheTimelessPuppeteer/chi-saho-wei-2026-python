def process_queries(n, queries):
    state = [0] * (n + 1)
    results = []

    for query in queries:
        op = query[0]

        if op == 1:
            i = query[1]
            state[i] ^= 1
        else:
            _, left, right = query
            parity = sum(state[left : right + 1]) % 2
            results.append(parity)

    return results


def solve():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    n = data[0]
    q = data[1]
    idx = 2
    queries = []

    for _ in range(q):
        op = data[idx]
        idx += 1

        if op == 1:
            i = data[idx]
            idx += 1
            queries.append((1, i))
        else:
            left = data[idx]
            right = data[idx + 1]
            idx += 2
            queries.append((2, left, right))

    outputs = process_queries(n, queries)
    sys.stdout.write("\n".join(map(str, outputs)))


if __name__ == "__main__":
    solve()
