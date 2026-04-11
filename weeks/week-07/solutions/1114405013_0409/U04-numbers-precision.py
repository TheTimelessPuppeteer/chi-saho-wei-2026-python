# U04. 數字精度的陷阱與選擇（3.1–3.7）
# 本範例示範數字處理中的常見陷阱和選擇：
# 1. round() 使用銀行家捨入（四捨六入五取偶）
# 2. NaN 值無法用 == 比較
# 3. float 和 Decimal 的精度與效能差異

import math
import timeit
from decimal import Decimal, ROUND_HALF_UP

# ── 銀行家捨入（3.1）─────────────────────────────────
# Python 的 round() 函數使用「銀行家捨入」規則：四捨六入五取偶。
# 當小數部分為 0.5 時，會捨入到最近的偶數，而非傳統的四捨五入。
print(round(0.5))  # 0（不是 1！因為 0 是偶數）
print(round(2.5))  # 2（不是 3！因為 2 是偶數）
print(round(3.5))  # 4（3.5 捨入到最近的偶數 4）

# 若需要傳統的四捨五入（總是向上捨入），可以使用 Decimal 模組。
def trad_round(x: float, n: int = 0) -> Decimal:
    # 將 float 轉成 Decimal 字串以避免浮點誤差
    d = Decimal(str(x))
    # 根據小數位數 n 建立格式化模板
    fmt = Decimal("1") if n == 0 else Decimal("0." + "0" * n)
    # 使用 ROUND_HALF_UP 進行傳統四捨五入
    return d.quantize(fmt, rounding=ROUND_HALF_UP)

print(trad_round(0.5))  # 1（傳統四捨五入）
print(trad_round(2.5))  # 3（傳統四捨五入）

# ── NaN 無法用 == 比較（3.7）─────────────────────────
c = float("nan")  # 建立 NaN（Not a Number）值
print(c == c)  # False（NaN 甚至不等於自己！）
print(c == float("nan"))  # False（任何 NaN 都不等於任何值）
# NaN 是 IEEE 754 標準定義的特殊浮點值，表示無效或未定義的數學運算結果。
print(math.isnan(c))  # True（唯一正確的 NaN 檢測方式）

# 在資料清理中，可以使用 math.isnan() 過濾 NaN 值
data = [1.0, float("nan"), 3.0, float("nan"), 5.0]
clean = [x for x in data if not math.isnan(x)]
print(clean)  # [1.0, 3.0, 5.0]（過濾掉 NaN）

# ── float vs Decimal 選擇（3.2）──────────────────────
# float：使用 IEEE 754 雙精度浮點數，快速但有精度誤差，適合科學計算。
print(0.1 + 0.2)  # 0.30000000000000004（浮點誤差）
print(0.1 + 0.2 == 0.3)  # False（因浮點誤差而不相等）

# Decimal：提供任意精度的十進位數學，精確但較慢，適合金融計算。
print(Decimal("0.1") + Decimal("0.2"))  # 0.3（精確）
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))  # True（精確比較）

# 效能比較：Decimal 通常比 float 慢數倍
t1 = timeit.timeit(lambda: 0.1 * 999, number=100_000)
t2 = timeit.timeit(lambda: Decimal("0.1") * 999, number=100_000)
print(f"float: {t1:.3f}s  Decimal: {t2:.3f}s（Decimal 約慢 {t2 / t1:.0f} 倍）")
# 根據應用需求選擇：精度 vs 效能
