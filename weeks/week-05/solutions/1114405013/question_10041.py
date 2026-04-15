def solve(data: str) -> str:
    # 把全部輸入拆成整數串列，方便依序讀取。
    values = list(map(int, data.split()))
    if not values:
        return ""

    # 第一個數字是測試資料組數。
    t = values[0]
    # idx 代表目前讀到 values 的哪個位置。
    idx = 1
    answers = []

    for _ in range(t):
        # 每組先讀親戚人數 r，再讀 r 個門牌。
        r = values[idx]
        idx += 1

        streets = values[idx : idx + r]
        idx += r

        # 取中位數所在門牌可使絕對距離總和最小。
        streets.sort()
        vito = streets[r // 2]
        # 把每位親戚到 vito 門牌的距離加總。
        total = sum(abs(s - vito) for s in streets)
        answers.append(str(total))

    # 每組答案一行。
    return "\n".join(answers)


if __name__ == "__main__":
    import sys

    print(solve(sys.stdin.read()))
