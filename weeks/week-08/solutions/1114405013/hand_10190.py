import sys


def main() -> None:
    data = sys.stdin.read().split()
    if not data:
        return

    i = 0
    n = int(data[i])
    i += 1
    w = float(data[i])
    i += 1
    t = float(data[i])
    i += 1
    v = float(data[i])
    i += 1

    segs = []
    for _ in range(n):
        x = float(data[i])
        i += 1
        l = float(data[i])
        i += 1
        _ = data[i]
        i += 1

        left = max(0.0, min(w, x))
        right = max(0.0, min(w, x + l))
        if right > left:
            segs.append((left, right))

    if not segs:
        print(f"{w * t * v:.2f}")
        return

    segs.sort()
    covered = 0.0
    l, r = segs[0]
    for nl, nr in segs[1:]:
        if nl <= r:
            r = max(r, nr)
        else:
            covered += r - l
            l, r = nl, nr
    covered += r - l

    ans = max(0.0, w - covered) * t * v
    print(f"{ans:.2f}")


if __name__ == "__main__":
    main()
