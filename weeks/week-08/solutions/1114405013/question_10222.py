import sys


ROWS = [
    "`1234567890-=",
    "qwertyuiop[]\\",
    "asdfghjkl;'",
    "zxcvbnm,./",
]


def build_mapping() -> dict[str, str]:
    """建立「向左移三鍵」的解碼映射表。"""
    mapping = {}
    for row in ROWS:
        for i in range(3, len(row)):
            mapping[row[i]] = row[i - 3]
    return mapping


def decode_text(text: str, mapping: dict[str, str]) -> str:
    """依映射表解碼整段文字（含多行）。"""
    out = []
    for ch in text:
        low = ch.lower()
        if low in mapping:
            decoded = mapping[low]
            # 若輸入是大寫字母，輸出也維持大寫。
            out.append(decoded.upper() if ch.isupper() else decoded)
        else:
            # 空白、換行等不在映射表中的字元直接保留。
            out.append(ch)
    return "".join(out)


def main() -> None:
    """UVA 10222 主程式。"""
    text = sys.stdin.read()
    mapping = build_mapping()
    sys.stdout.write(decode_text(text, mapping))


if __name__ == "__main__":
    main()
