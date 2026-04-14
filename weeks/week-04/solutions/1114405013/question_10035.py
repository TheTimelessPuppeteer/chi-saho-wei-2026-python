import sys


def format_carry_result(count: int) -> str:
    """依題目要求把進位次數轉成對應英文句型。"""
    if count == 0:
        return "No carry operation."
    if count == 1:
        return "1 carry operation."
    return f"{count} carry operations."


def count_carry(a: int, b: int) -> int:
    """計算兩個整數相加時總共產生幾次進位。"""
    carry = 0
    count = 0

    # 從個位數開始逐位相加，直到兩數都處理完畢。
    while a > 0 or b > 0:
        digit_sum = (a % 10) + (b % 10) + carry
        if digit_sum >= 10:
            count += 1
            carry = 1
        else:
            carry = 0

        a //= 10
        b //= 10

    return count


def main() -> None:
    """UVA 10035 主程式。

    輸入格式：每行兩個非負整數，遇到 `0 0` 代表結束。
    輸出格式：每筆資料輸出進位次數描述句。
    """

    output_lines = []

    # 題目是逐行輸入直到終止條件，因此用 for line in sys.stdin 最直覺。
    for line in sys.stdin:
        line = line.strip()
        if not line:
            # 空行直接跳過，避免 split 後資料不足。
            continue

        a_str, b_str = line.split()
        a = int(a_str)
        b = int(b_str)

        # 終止條件：0 0 不輸出，直接結束整體處理。
        if a == 0 and b == 0:
            break

        output_lines.append(format_carry_result(count_carry(a, b)))

    sys.stdout.write("\n".join(output_lines))


if __name__ == "__main__":
    main()
