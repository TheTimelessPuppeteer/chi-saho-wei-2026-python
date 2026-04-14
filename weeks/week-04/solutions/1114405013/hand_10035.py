import sys


def carry_count_from_strings(a: str, b: str) -> int:

    ra = a[::-1]
    rb = b[::-1]

    length = max(len(ra), len(rb))
    ra = ra.ljust(length, "0")
    rb = rb.ljust(length, "0")

    carry = 0
    count = 0

    for i in range(length):
        d1 = ord(ra[i]) - ord("0")
        d2 = ord(rb[i]) - ord("0")
        s = d1 + d2 + carry

        if s >= 10:
            count += 1
            carry = 1
        else:
            carry = 0

    return count


def format_result(count: int) -> str:
    if count == 0:
        return "No carry operation."
    if count == 1:
        return "1 carry operation."
    return f"{count} carry operations."


def main() -> None:
    out = []

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        a, b = line.split()

        if a == "0" and b == "0":
            break

        out.append(format_result(carry_count_from_strings(a, b)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()