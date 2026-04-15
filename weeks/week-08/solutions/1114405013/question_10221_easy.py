import math
import sys


def main() -> None:
    """UVA 10221 easy 版。

    好記口訣：
    1) 半徑 r = 6440 + s
    2) 角度若是 min 先除以 60 變成 deg
    3) 若角度 > 180，改成 360-a
    4) 弧長 = r * 弧度
    5) 弦長 = 2r*sin(弧度/2)

    詳細說明：
    - 題目要的是「同一圓上兩點」之間的弧長與弦長。
    - 衛星軌道半徑不是 6440，而是 6440 + s。
    - 角度若是 min（角分），要先轉成度：degree = min / 60。
    - 圓上兩點有大小兩段弧，題目採較短那段，所以角度超過 180
      時要改成 360-a。
    - 最後把 degree 轉成 radian 才能套 trig 公式。

    公式整理：
    - r = 6440 + s
    - theta(rad) = radians(a)
    - arc = r * theta
    - chord = 2 * r * sin(theta / 2)
    """

    ans = []

    # 多組輸入直到 EOF，每行格式：s a unit
    for line in sys.stdin:
        # 去掉頭尾空白，避免 split 時受多餘空白影響。
        line = line.strip()
        if not line:
            # 空行直接跳過。
            continue

        # 解析本行三個欄位。
        s_str, a_str, unit = line.split()
        s = float(s_str)
        a = float(a_str)

        # 1) 計算衛星到地心半徑 r
        r = 6440.0 + s

        # 2) 若角度單位是角分，先轉為度
        if unit == "min":
            a = a / 60.0

        # 3) 取較小圓心角（<=180）
        if a > 180.0:
            a = 360.0 - a

        # 4) degree 轉 radian
        rad = math.radians(a)

        # 5) 依公式計算弧長與弦長
        arc = r * rad
        chord = 2.0 * r * math.sin(rad / 2.0)

        # 題目要求固定輸出到小數點後六位。
        ans.append(f"{arc:.6f} {chord:.6f}")

    # 逐行輸出各測資結果。
    print("\n".join(ans))


if __name__ == "__main__":
    main()
