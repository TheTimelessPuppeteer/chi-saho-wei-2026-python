import sys


def main() -> None:

    text = sys.stdin.read().strip()
    if not text:
        return

    a = int(text)
    n = a * a + 1

    best = None

    d = 1
    while d * d <= n:
        if n % d == 0:
            q = n // d
            candidate = 2 * a + d + q
            if best is None or candidate < best:
                best = candidate
        d += 1

    print(best)


if __name__ == "__main__":
    main()