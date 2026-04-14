import sys


def main() -> None:

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        a, b = map(int, line.split())

        print(abs(a - b))


if __name__ == "__main__":
    main()