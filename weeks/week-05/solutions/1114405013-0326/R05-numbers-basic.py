# R05. 數字基礎：四捨五入、進制、格式化（3.1–3.4）
# round / Decimal / format / bin / oct / hex

from decimal import Decimal, localcontext
import math

# ── 3.1 四捨五入 ──────────────────────────────────────
# round(x, n)：把 x 四捨五入到小數點後 n 位，n 為負則表示向左移動位數
print(round(1.27, 1))  # 1.3，保留 1 位小數
print(round(1.25361, 3))  # 1.254，保留 3 位小數
print(round(0.5))  # 0（銀行家捨入，取最近偶數）
print(round(2.5))  # 2，0.5 的情況會捨入到最近偶數

a = 1627731
print(round(a, -2))  # 1627700（對百位四捨五入）

# ── 3.2 精確浮點數 ────────────────────────────────────
# 浮點數運算會有表示誤差，因此通常以 Decimal 做精確十進位運算
print(4.2 + 2.1)  # 6.300000000000001（浮點誤差）
da, db = Decimal("4.2"), Decimal("2.1")
print(da + db)  # 6.3（精確結果）

# localcontext 可以臨時調整 Decimal 的精度
with localcontext() as ctx:
    ctx.prec = 3
    print(Decimal("1.3") / Decimal("1.7"))  # 0.765，結果保留 3 位有效數字

# math.fsum 針對多個浮點數相加會減少精度誤差
print(math.fsum([1.23e18, 1, -1.23e18]))  # 1.0（正確）

# ── 3.3 數字格式化 ────────────────────────────────────
# format(value, format_spec) 用於產生格式化字串
x = 1234.56789
print(format(x, "0.2f"))  # '1234.57'，固定 2 位小數
print(format(x, ">10.1f"))  # '    1234.6'，總寬度 10、1 位小數、右對齊
print(format(x, ","))  # '1,234.56789'，加入千分位逗號
print(format(x, "0,.2f"))  # '1,234.57'，千分位 + 2 位小數
print(format(x, "e"))  # '1.234568e+03'，科學記號表示法

# 也可用 f-string 進行相同格式化
print(f"{x:0.2f}")  # '1234.57'
print(f"{x:0,.2f}")  # '1,234.57'

# ── 3.4 二八十六進制 ──────────────────────────────────
# bin/oct/hex 和 int(s, base) 用於進制轉換
n = 1234
print(bin(n), oct(n), hex(n))  # 0b10011010010 0o2322 0x4d2
print(format(n, "b"), format(n, "x"))  # 10011010010 4d2，不含前綴
print(int("4d2", 16), int("2322", 8))  # 1234 1234，從不同進位字串轉回整數
