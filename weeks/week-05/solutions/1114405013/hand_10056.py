import sys


def one_case(n: int, p: float, i: int) -> float:
    if p == 0.0:
        return 0.0

    q = 1.0 - p 

    hit_in_round = (q ** (i - 1)) * p

    round_all_fail = q**n

    return hit_in_round / (1.0 - round_all_fail)


lines = sys.stdin.read().strip().splitlines()

if not lines:
    sys.exit(0)

s = int(lines[0])
out = []

for k in range(1, s + 1):
    n_str, p_str, i_str = lines[k].split()
    n = int(n_str)
    p = float(p_str)
    i = int(i_str)

    ans = one_case(n, p, i)
    out.append(f"{ans:.4f}")

print("\n".join(out))
