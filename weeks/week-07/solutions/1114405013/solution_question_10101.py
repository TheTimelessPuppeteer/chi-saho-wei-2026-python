"""Question 10101 解答。

從輸入的一條七段顯示器等式中，嘗試「只移動一根木棒」讓等式成立。
若找得到任一合法解就輸出該等式（含 #），否則輸出 No。
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

# 觀念說明：
# - 每個數字對應一組七段顯示器 segment（a~g）。
# - 「移動一根木棒」等價於：
#   1) 從某處拿掉一根（remove 1 segment）
#   2) 在某處補上一根（add 1 segment）
# - 可以在同一個數字內完成（先拿後補），也可以跨兩個數字完成。


def eval_side(text):
    """計算僅含 +、- 與整數的表達式值。

    範例：
    - "12-3+4" -> 13
    - "-10+7"  -> -3

    此函式不處理括號，因為題目已保證不會出現。
    """
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
    """檢查等式是否成立（左值是否等於右值）。"""
    if expr.count("=") != 1:
        return False
    left, right = expr.split("=")
    return eval_side(left) == eval_side(right)


def build_same_digit_moves():
    """建立「同一個數字內部移動一根」的轉換表。

    條件：
    - 從 src 轉到 dst
    - src 少一根、dst 多一根（都在同一個數字內完成）
    - 用集合差看，必須同時滿足：
      len(src - dst) == 1 且 len(dst - src) == 1
    """
    moves = {d: [] for d in SEGMENTS}
    for src in SEGMENTS:
        src_set = SEGMENTS[src]
        for dst in SEGMENTS:
            if src == dst:
                continue
            dst_set = SEGMENTS[dst]
            removed = src_set - dst_set
            added = dst_set - src_set
            if len(removed) == 1 and len(added) == 1:
                moves[src].append(dst)
    return moves


def build_cross_digit_moves():
    """建立跨數字搬移一根木棒時的轉換表。

    回傳兩張表：
    - lose_one[d]: 數字 d 在「拿掉一根」後可變成哪些數字
    - gain_one[d]: 數字 d 在「補上一根」後可變成哪些數字

    這樣在嘗試跨數字搬移時，
    可以快速枚舉來源位與目標位的合法替換。
    """
    lose_one = {d: [] for d in SEGMENTS}
    gain_one = {d: [] for d in SEGMENTS}

    for src in SEGMENTS:
        src_set = SEGMENTS[src]
        for dst in SEGMENTS:
            if src == dst:
                continue
            dst_set = SEGMENTS[dst]
            removed = src_set - dst_set
            added = dst_set - src_set

            # 來源數字：只能少一根，不可多一根。
            if len(removed) == 1 and len(added) == 0:
                lose_one[src].append(dst)

            # 目標數字：只能多一根，不可少一根。
            if len(removed) == 0 and len(added) == 1:
                gain_one[src].append(dst)

    return lose_one, gain_one


SAME_DIGIT_MOVES = build_same_digit_moves()
LOSE_ONE_MOVES, GAIN_ONE_MOVES = build_cross_digit_moves()


def find_solution(original):
    """找到任一合法解，找不到回傳 None。

    搜尋順序：
    1. 先試同位數字內部移動（只改一個數字）
    2. 再試跨兩個數字移動（一個數字少一根，另一個數字多一根）

    只要找到第一個合法等式就直接回傳。
    """
    chars = list(original)
    digit_positions = [i for i, ch in enumerate(chars) if ch.isdigit()]

    # 1) 先嘗試同一個數字內部搬一根：
    #    只改動一個數字，其他字元保持不變。
    for i in digit_positions:
        src_digit = chars[i]
        for dst_digit in SAME_DIGIT_MOVES[src_digit]:
            candidate = chars[:]
            candidate[i] = dst_digit
            expr = "".join(candidate)
            if is_true_equation(expr):
                return expr

    # 2) 再嘗試跨兩個數字搬移：
    #    i 位置拿掉一根，j 位置補上一根。
    for i in digit_positions:
        src_digit = chars[i]
        for src_new in LOSE_ONE_MOVES[src_digit]:
            for j in digit_positions:
                if i == j:
                    continue
                dst_digit = chars[j]
                for dst_new in GAIN_ONE_MOVES[dst_digit]:
                    candidate = chars[:]
                    candidate[i] = src_new
                    candidate[j] = dst_new
                    expr = "".join(candidate)
                    if is_true_equation(expr):
                        return expr

    return None


def solve():
    """讀取輸入、尋找可行解並輸出。"""
    raw = sys.stdin.read()
    if not raw:
        return

    # 只取第一個 # 之前（含 #），其後文字忽略。
    pos = raw.find("#")
    if pos == -1:
        print("No")
        return

    # 輸入可能在 # 後有雜訊，依題意要忽略。
    expr_with_hash = raw[: pos + 1].strip()
    expr = expr_with_hash[:-1]

    answer = find_solution(expr)
    if answer is None:
        print("No")
    else:
        print(answer + "#")


if __name__ == "__main__":
    solve()
