import math
import sys


def main() -> None:

    ans = []

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        s_str, a_str, unit = line.split()
        s = float(s_str)
        a = float(a_str)

        r = 6440.0 + s

        if unit == "min":
            a = a / 60.0

        if a > 180.0:
            a = 360.0 - a

        rad = math.radians(a)

        arc = r * rad
        chord = 2.0 * r * math.sin(rad / 2.0)

        ans.append(f"{arc:.6f} {chord:.6f}")

    print("\n".join(ans))


if __name__ == "__main__":
    main()