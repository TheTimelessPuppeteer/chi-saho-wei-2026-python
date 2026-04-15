import math
import sys


EARTH_RADIUS = 6440.0


def compute_arc_and_chord(s: float, a: float, unit: str) -> tuple[float, float]:
    """根據題意計算弧長與弦長。"""
    radius = EARTH_RADIUS + s

    # 單位轉換：min -> degree
    if unit == "min":
        a = a / 60.0

    # 取較小圓心角（<=180 度）
    if a > 180.0:
        a = 360.0 - a

    rad = math.radians(a)
    arc = radius * rad
    chord = 2.0 * radius * math.sin(rad / 2.0)
    return arc, chord


def main() -> None:
    """UVA 10221 主程式。

    輸入多組資料直到 EOF，每行格式：s a unit
    輸出：弧長與弦長，皆保留小數點後六位。
    """
    out_lines = []

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        s_str, a_str, unit = line.split()
        s = float(s_str)
        a = float(a_str)

        arc, chord = compute_arc_and_chord(s, a, unit)
        out_lines.append(f"{arc:.6f} {chord:.6f}")

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()
