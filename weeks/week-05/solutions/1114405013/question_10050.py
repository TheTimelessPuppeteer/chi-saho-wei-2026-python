def solve(data: str) -> str:
    # 將所有輸入拆成整數，方便用索引依序讀取。
    nums = list(map(int, data.split()))
    if not nums:
        return ""

    # 第一個數字是測資組數。
    t = nums[0]
    i = 1
    answers = []

    for _ in range(t):
        # 讀取本組要模擬的天數 N。
        n = nums[i]
        i += 1

        # 讀取政黨數 P。
        p = nums[i]
        i += 1

        # 用集合記錄已經損失的「工作日」，可自動去除重複天數。
        lost_days = set()

        # 逐一處理每個政黨的罷會參數 h。
        for _ in range(p):
            h = nums[i]
            i += 1

            # 該政黨會在 h, 2h, 3h, ... 天罷會。
            day = h
            while day <= n:
                # 依題意：第 1 天是星期天。
                # day % 7 == 6 -> 星期五（假日，不算）
                # day % 7 == 0 -> 星期六（假日，不算）
                weekday = day % 7
                if weekday not in (6, 0):
                    lost_days.add(day)
                day += h

        answers.append(str(len(lost_days)))

    # 每組測資輸出一行答案。
    return "\n".join(answers)


if __name__ == "__main__":
    import sys

    print(solve(sys.stdin.read()))
