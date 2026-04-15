import sys


def main() -> None:
    """UVA 10222 easy 版（超好記）。

    題意：
    - 鍵盤輸入時每個字元都「向右偏了 3 鍵」。
    - 因此解碼時要把每個可映射字元「往左找 3 鍵」。

    口訣：
    1) 準備四排鍵盤字串
    2) 建立右字元 -> 左三格字元 的字典
    3) 逐字掃描輸入，能轉就轉，不能轉就原樣保留

    詳細說明：
    - 題目的「右偏 3 鍵」代表：輸入字元其實是正確字元在鍵盤上右邊第 3 個。
    - 所以解碼要把每個字元往左找 3 格。
    - 例如：
      - 'r' 左移 3 格是 'e'
      - '7' 左移 3 格是 '4'
    - 空白與換行不屬於鍵盤映射表，必須保留不變。
    - 為了讓大小寫輸入可用：
      - 查表時先轉小寫
      - 若原字元是大寫字母，輸出再轉回大寫
    """

    # 標準 QWERTY 鍵盤（題目給定）。
    # 注意這裡是「可被移動映射」的字元集合。
    rows = [
        "`1234567890-=",
        "qwertyuiop[]\\",
        "asdfghjkl;'",
        "zxcvbnm,./",
    ]

    # mapping[ch] = 解碼後字元（左移三格）
    # 例如在第二排：row[3]=='r' 對應 row[0]=='q'。
    mapping = {}
    for row in rows:
        # i 從 3 開始，因為要對應到 i-3。
        for i in range(3, len(row)):
            mapping[row[i]] = row[i - 3]

    # 讀取整段輸入（可多行、可含空白）。
    # 題目是整段文字解碼，因此不能只讀一行。
    text = sys.stdin.read()
    out = []

    # 逐字元處理，保持原本換行與空格位置。
    for ch in text:
        low = ch.lower()

        if low in mapping:
            decoded = mapping[low]

            # 若輸入是大寫字母，輸出保持大寫，
            # 其餘符號/數字則直接用 decoded。
            if ch.isupper():
                out.append(decoded.upper())
            else:
                out.append(decoded)
        else:
            # 空白、換行等不在映射表中的字元原樣輸出。
            out.append(ch)

    # 把解碼後字元串回字串輸出。
    sys.stdout.write("".join(out))


if __name__ == "__main__":
    main()
