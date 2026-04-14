import sys


def carry_count_from_strings(a: str, b: str) -> int:
    """計算兩個非負整數字串相加時的進位次數。

    好記口訣：
    1) 反轉字串（從個位開始）
    2) 補零到同長
    3) 逐位相加並更新 carry
    4) 累加 carry 出現次數

    為什麼用「字串法」：
    - 不需要 `%10`、`//10`，對初學者更直觀。
    - 可直接處理前導 0（例如 `0001`），不會影響正確性。
    - 只要照著直式加法流程實作，幾乎不會背錯。
    """

    # 反轉後索引 0 就是個位數，方便由低位往高位處理。
    ra = a[::-1]
    rb = b[::-1]

    # 位數不同時，短的補 0 才能逐位對齊相加。
    length = max(len(ra), len(rb))
    ra = ra.ljust(length, "0")
    rb = rb.ljust(length, "0")

    # carry: 前一位是否有進位（0 或 1）
    # count: 目前累積的進位次數
    carry = 0
    count = 0

    # 逐位處理（i=0 是個位，i=1 是十位，...）
    for i in range(length):
        # 字元轉數字：'0'~'9' -> 0~9
        d1 = ord(ra[i]) - ord("0")
        d2 = ord(rb[i]) - ord("0")

        # 這一位的總和 = 左位數 + 右位數 + 前一次進位
        s = d1 + d2 + carry

        # 只要 >= 10，代表這一位發生一次進位。
        if s >= 10:
            count += 1
            carry = 1
        else:
            carry = 0

    return count


def format_result(count: int) -> str:
    """依題目規範回傳對應句型。

    注意英文複數：
    - 0: No carry operation.
    - 1: 1 carry operation.
    - >=2: N carry operations.
    """
    if count == 0:
        return "No carry operation."
    if count == 1:
        return "1 carry operation."
    return f"{count} carry operations."


def main() -> None:
    """UVA 10035 簡易版主程式。

    輸入：每行兩個整數，遇到 `0 0` 結束。
    輸出：每組資料輸出進位次數描述。
    """
    out = []

    # UVA 常見輸入型態：未知筆數，一行一組，直到 EOF。
    for line in sys.stdin:
        # 去除前後空白，方便處理「多空白、空行」情況。
        line = line.strip()
        if not line:
            continue

        # 每行應該有兩個整數字串。
        a, b = line.split()

        # 終止條件：0 0 不輸出，直接結束。
        if a == "0" and b == "0":
            break

        # 先算進位次數，再轉成題目指定句型。
        out.append(format_result(carry_count_from_strings(a, b)))

    # 統一輸出，避免每次 print 的格式細節差異。
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
