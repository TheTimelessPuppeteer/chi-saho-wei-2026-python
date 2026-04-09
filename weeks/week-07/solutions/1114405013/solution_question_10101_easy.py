"""Question 10101 easy 版解答。

這版主打「容易記憶」：
1. 不預先建轉換表
2. 直接用七段顯示器集合差，判斷是否為「移動一根木棒」
3. 先試同一位數字內部移動，再試跨兩位數字移動

題目限制重點：
- 只能移動「數字」的木棒，不能改動 +、-、=
- 輸入以 # 結尾，# 後面可能有雜訊，要忽略
- 只要找到任一合法答案即可
"""

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
    """計算只含 +、-、整數的表達式值。

    這裡不使用 eval，而是手動解析，避免安全問題，
    並確保與題目語法一致。
    """
    i = 0
    sign = 1
    total = 0

    if i < len(text) and text[i] == "-":
        sign = -1
        i += 1

    # 逐段讀取「數字 + 運算符 + 數字 ...」
    while i < len(text):
        start = i
        while i < len(text) and text[i].isdigit():
            i += 1
        if start == i:
            raise ValueError("invalid number")

        # 依照目前 sign 累加此段整數。
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
    """檢查等式是否成立。"""
    if expr.count("=") != 1:
        return False
    left, right = expr.split("=")
    return eval_side(left) == eval_side(right)


def segment_diff(src_digit, dst_digit):
    """回傳 src->dst 的 (拿掉幾根, 補上幾根)。

    例如：
    - 3 -> 2 可能是拿掉 c、補上 e，結果 (1, 1)
    - 8 -> 9 只需要拿掉 e，結果 (1, 0)
    - 1 -> 7 只需要補上 a，結果 (0, 1)
    """
    src = SEGMENTS[src_digit]
    dst = SEGMENTS[dst_digit]
    removed = len(src - dst)
    added = len(dst - src)
    return removed, added


def find_solution(expr):
    """找到任一合法答案，找不到回傳 None。

    搜尋策略（好記版本）：
    1) 先試「同一位」完成移動（remove=1, add=1）
    2) 再試「跨兩位」移動：
       - 來源位：remove=1, add=0
       - 目標位：remove=0, add=1

    每次產生候選式後，只要等式成立就立即回傳。
    """
    chars = list(expr)
    digit_positions = [i for i, ch in enumerate(chars) if ch.isdigit()]
    digits = list(SEGMENTS.keys())

    # 1) 同一位數字內部移動：該位要同時「拿 1、補 1」。
    #    這代表木棒在同一個數字內換位置。
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

    # 2) 跨兩位移動：
    #    來源位「拿 1 不補」，目標位「補 1 不拿」。
    #    這代表把木棒從某個數字搬到另一個數字。
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
    """讀取輸入並輸出答案。"""
    raw = sys.stdin.read()
    if not raw:
        return

    # 題目保證用 # 結尾，且 # 後可能有無關字元。
    # 所以只取第一個 # 之前的內容來處理。
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
