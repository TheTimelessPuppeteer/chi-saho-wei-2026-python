import sys


SEGMENTS = {
    "0": {"a", "b", "c", "d", "e", "f"},
    "1": {"b", "c"},
    "2": {"a", "b", "d", "e", "g"},
    "3": {"a", "b", "c", "d", "g"},
    "4": {"b", "c", "f", "g"},
    "5": {"a", "c", "d", "f", "g"},
    "6": {"a", "c", "d", "e", "f", "g"},
    "7": {"a", "b", "c"},
    "8": {"a", "b", "c", "d", "e", "f", "g"},
    "9": {"a", "b", "c", "d", "f", "g"},
}


def eval_side(text):
    i = 0
    sign = 1
    total = 0

    if i < len(text) and text[i] == "-":
        sign = -1
        i += 1

    while i < len(text):
        start = i
        while i < len(text) and text[i].isdigit():
            i += 1
        if start == i:
            raise ValueError("invalid number")

        total += sign * int(text[start:i])

        if i >= len(text):
            break

        if text[i] == "+":
            sign = 1
        elif text[i] == "-":
            sign = -1
        else:
            raise ValueError("invalid operator")
        i += 1

    return total


def is_true_equation(expr):
    if expr.count("=") != 1:
        return False
    left, right = expr.split("=")
    return eval_side(left) == eval_side(right)


def segment_diff(src_digit, dst_digit):
    src = SEGMENTS[src_digit]
    dst = SEGMENTS[dst_digit]
    removed = len(src - dst)
    added = len(dst - src)
    return removed, added


def find_solution(expr):

    chars = list(expr)
    digit_positions = [i for i, ch in enumerate(chars) if ch.isdigit()]
    digits = list(SEGMENTS.keys())

    for i in digit_positions:
        old = chars[i]
        for new in digits:
            if new == old:
                continue
            removed, added = segment_diff(old, new)
            if removed == 1 and added == 1:
                candidate = chars[:]
                candidate[i] = new
                candidate_expr = "".join(candidate)
                if is_true_equation(candidate_expr):
                    return candidate_expr

    for i in digit_positions:
        old_i = chars[i]
        for new_i in digits:
            if new_i == old_i:
                continue
            rem_i, add_i = segment_diff(old_i, new_i)
            if not (rem_i == 1 and add_i == 0):
                continue

            for j in digit_positions:
                if i == j:
                    continue
                old_j = chars[j]
                for new_j in digits:
                    if new_j == old_j:
                        continue
                    rem_j, add_j = segment_diff(old_j, new_j)
                    if not (rem_j == 0 and add_j == 1):
                        continue

                    candidate = chars[:]
                    candidate[i] = new_i
                    candidate[j] = new_j
                    candidate_expr = "".join(candidate)
                    if is_true_equation(candidate_expr):
                        return candidate_expr

    return None


def solve():
    raw = sys.stdin.read()
    if not raw:
        return

    pos = raw.find("#")
    if pos == -1:
        print("No")
        return

    expr = raw[:pos].strip()
    answer = find_solution(expr)

    if answer is None:
        print("No")
    else:
        print(answer + "#")


if __name__ == "__main__":
    solve()
