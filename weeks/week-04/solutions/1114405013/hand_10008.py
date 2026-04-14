import sys


def main() -> None:
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    n = int(lines[0].strip())
    texts = lines[1 : 1 + n]

    cnt = [0] * 26

    for line in texts:
        for ch in line:
            up = ch.upper()

            if "A" <= up <= "Z":
                idx = ord(up) - ord("A")
                cnt[idx] += 1

    items = []
    for i in range(26):
        if cnt[i] > 0:
            letter = chr(ord("A") + i)
            items.append((letter, cnt[i]))

    items.sort(key=lambda x: (-x[1], x[0]))

    for letter, freq in items:
        print(f"{letter} {freq}")


if __name__ == "__main__":
    main()