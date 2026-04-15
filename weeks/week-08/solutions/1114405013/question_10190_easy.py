import sys


def main() -> None:
    """QUESTION-10190 easy 版。

    好記口訣：
    1) 讀 N, W, T, V
    2) 把每把傘當成 [x, x+l] 區間
    3) 合併區間求總覆蓋長度
    4) 未覆蓋 * T * V，印到小數二位

    補充說明（好記重點）：
    - 本版本把每把傘視為一段遮蔽區間 [x, x+l]。
    - 先把所有區間裁切到馬路範圍 [0, W]。
    - 再做區間合併，得到「總覆蓋長度」。
    - 地面接雨長度 = W - 總覆蓋長度。
    - 雨量 = 地面接雨長度 * T * V。
    """

    # 以 split() 讀取全部 token，可容忍輸入中的多空白/換行。
    data = sys.stdin.read().split()
    if not data:
        # 沒有輸入就直接結束。
        return

    # 依序讀取第一行四個參數。
    i = 0
    n = int(data[i])
    i += 1
    w = float(data[i])
    i += 1
    t = float(data[i])
    i += 1
    v = float(data[i])
    i += 1

    segs = []
    for _ in range(n):
        # 每把傘輸入：x, l, v（此 easy 版不使用速度 v）。
        x = float(data[i])
        i += 1
        l = float(data[i])
        i += 1
        _ = data[i]  # 速度欄位此版不使用（僅保留讀入位置）
        i += 1

        # 把區間裁切到 [0, W]，避免超出馬路邊界。
        left = max(0.0, min(w, x))
        right = max(0.0, min(w, x + l))

        # 只有有效長度（right > left）的區間才納入。
        if right > left:
            segs.append((left, right))

    if not segs:
        # 沒有任何遮蔽，全部雨量都落地。
        print(f"{w * t * v:.2f}")
        return

    # 先排序，才能線性合併重疊區間。
    segs.sort()

    # covered: 最終總覆蓋長度
    # l, r: 目前正在合併的區間
    covered = 0.0
    l, r = segs[0]
    for nl, nr in segs[1:]:
        if nl <= r:
            # 有重疊（或相接），直接延長右端點。
            r = max(r, nr)
        else:
            # 不重疊，先結算前一段，再換成新段。
            covered += r - l
            l, r = nl, nr

    # 別忘了把最後一段也加進 covered。
    covered += r - l

    # 未覆蓋長度不應為負，故用 max(0.0, ...)。
    ans = max(0.0, w - covered) * t * v

    # 題目要求輸出到小數點後兩位。
    print(f"{ans:.2f}")


if __name__ == "__main__":
    main()
