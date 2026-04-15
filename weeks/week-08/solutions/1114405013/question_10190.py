import sys


def merged_covered_length(intervals, width):
    """計算所有雨傘在馬路上的覆蓋聯集長度。"""
    clipped = []

    for left, right in intervals:
        # 雨傘只會在馬路範圍 [0, width] 內產生遮雨效果。
        l = max(0.0, min(float(width), float(left)))
        r = max(0.0, min(float(width), float(right)))
        if r > l:
            clipped.append((l, r))

    if not clipped:
        return 0.0

    # 先依左端點排序，再做區間合併。
    clipped.sort()

    total = 0.0
    cur_l, cur_r = clipped[0]
    for l, r in clipped[1:]:
        if l <= cur_r:
            # 重疊或相接，延長目前區間。
            cur_r = max(cur_r, r)
        else:
            # 不重疊，先結算前一段再開新段。
            total += cur_r - cur_l
            cur_l, cur_r = l, r

    total += cur_r - cur_l
    return total


def main() -> None:
    """QUESTION-10190 主程式。

    本版依測試需求：
    - 以輸入雨傘位置形成遮蔽區間聯集
    - 估算落到地面的雨量 = 未覆蓋長度 * T * V
    - 輸出固定到小數點後兩位
    """
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    it = iter(tokens)
    n = int(next(it))
    w = float(next(it))
    t = float(next(it))
    v_rain = float(next(it))

    intervals = []
    for _ in range(n):
        x = float(next(it))
        length = float(next(it))
        _speed = float(next(it))

        # 一把雨傘可視為 [x, x+length] 的遮蔽區間。
        intervals.append((x, x + length))

    covered = merged_covered_length(intervals, w)
    ground = max(0.0, w - covered)
    volume = ground * t * v_rain

    print(f"{volume:.2f}")


if __name__ == "__main__":
    main()
