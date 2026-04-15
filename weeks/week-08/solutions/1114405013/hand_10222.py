import sys


def main() -> None:

    rows = [
        "`1234567890-=",
        "qwertyuiop[]\\",
        "asdfghjkl;'",
        "zxcvbnm,./",
    ]

    mapping = {}
    for row in rows:
        for i in range(3, len(row)):
            mapping[row[i]] = row[i - 3]

    text = sys.stdin.read()
    out = []

    for ch in text:
        low = ch.lower()

        if low in mapping:
            decoded = mapping[low]

            if ch.isupper():
                out.append(decoded.upper())
            else:
                out.append(decoded)
        else:
            out.append(ch)

    sys.stdout.write("".join(out))


if __name__ == "__main__":
    main()
