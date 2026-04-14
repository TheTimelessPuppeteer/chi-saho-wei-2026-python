import sys


def is_consistent(weighings, fake_coin, fake_delta):
    """檢查假設（某硬幣為假，且偏重/偏輕）是否符合全部秤重結果。"""
    for left, right, result in weighings:
        # diff > 0 代表「左盤較重」；diff < 0 代表「右盤較重」。
        # 真幣不影響差值，只有假幣會依偏重(+1)或偏輕(-1)改變差值。
        diff = 0

        for coin in left:
            if coin == fake_coin:
                diff += fake_delta

        for coin in right:
            if coin == fake_coin:
                diff -= fake_delta

        # 把本次差值對照題目給的秤重符號，任何一次不符就可排除此假設。
        if result == "=" and diff != 0:
            return False
        if result == "<" and diff >= 0:
            return False
        if result == ">" and diff <= 0:
            return False

    return True


def solve(tokens):
    # 由於輸入中可能穿插空白列，先切成 token 後可用固定格式依序解析。
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
            # 每顆硬幣都要測兩種情況：偏重、偏輕。
            heavier_ok = is_consistent(weighings, coin, 1)
            lighter_ok = is_consistent(weighings, coin, -1)

            if heavier_ok or lighter_ok:
                possible_coins.append(coin)

        # 題意要求「能唯一判定」才輸出編號，否則輸出 0。
        if len(possible_coins) == 1:
            answers.append(str(possible_coins[0]))
        else:
            answers.append("0")

    # 不同測資答案間要有一個空白列。
    return "\n\n".join(answers)


def main():
    # 以 split() 讀取全部 token，可自然忽略題目輸入中的空白列。
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    print(solve(tokens))


if __name__ == "__main__":
    main()
