import sys


def is_consistent(weighings, fake_coin, fake_delta):
    for left, right, result in weighings:
        diff = 0

        for coin in left:
            if coin == fake_coin:
                diff += fake_delta

        for coin in right:
            if coin == fake_coin:
                diff -= fake_delta

        if result == "=" and diff != 0:
            return False
        if result == "<" and diff >= 0:
            return False
        if result == ">" and diff <= 0:
            return False

    return True


def solve(tokens):
    idx = 0
    case_count = int(tokens[idx])
    idx += 1

    answers = []

    for _ in range(case_count):
        n = int(tokens[idx])
        idx += 1
        k = int(tokens[idx])
        idx += 1

        weighings = []
        for _ in range(k):
            p = int(tokens[idx])
            idx += 1

            left = [int(tokens[idx + i]) for i in range(p)]
            idx += p

            right = [int(tokens[idx + i]) for i in range(p)]
            idx += p

            result = tokens[idx]
            idx += 1

            weighings.append((left, right, result))

        possible_coins = []

        for coin in range(1, n + 1):
            heavier_ok = is_consistent(weighings, coin, 1)
            lighter_ok = is_consistent(weighings, coin, -1)

            if heavier_ok or lighter_ok:
                possible_coins.append(coin)

        if len(possible_coins) == 1:
            answers.append(str(possible_coins[0]))
        else:
            answers.append("0")

    return "\n\n".join(answers)


def main():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    print(solve(tokens))


if __name__ == "__main__":
    main()
