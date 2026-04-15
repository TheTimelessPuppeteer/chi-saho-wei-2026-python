# R06. 特殊數值：無窮大、NaN、分數、隨機（3.7–3.11）
# float inf/nan / fractions.Fraction / random

import math
import random
from fractions import Fraction

# ── 3.7 無窮大與 NaN ──────────────────────────────────
# inf 與 -inf 表示正、負無窮大；NaN 表示非數值
positive_inf = float("inf")
negative_inf = float("-inf")
not_a_number = float("nan")
print(positive_inf, negative_inf, not_a_number)  # inf -inf nan

# 判斷是否為無限大或 NaN
print(math.isinf(positive_inf))  # True
print(math.isinf(negative_inf))  # True
print(math.isnan(not_a_number))  # True

# 無窮大的運算規則
print(positive_inf + 45, 10 / positive_inf)  # inf 0.0
print(positive_inf - positive_inf, positive_inf + negative_inf)  # nan nan（未定義）

# NaN 的比較結果特別：NaN 不等於任何值，包括自己
print(not_a_number == not_a_number)  # False
print(not_a_number != not_a_number)  # True

# ── 3.8 分數運算 ──────────────────────────────────────
# Fraction 可以精確表示分數，避免浮點數誤差
p = Fraction(5, 4)
q = Fraction(7, 16)
r = p * q
print(p + q)  # 27/16
print(r)  # 35/64
print(r.numerator, r.denominator)  # 35 64
print(float(r))  # 0.546875

# limit_denominator 用於將分數簡化成最接近的分母
print(r.limit_denominator(8))  # 4/7

# 由浮點數轉換成 Fraction，避免直接使用 float 文字造成誤差
print(Fraction("3.75"))  # 15/4
print(Fraction(*(3.75).as_integer_ratio()))  # 15/4

# 也可以從整數與分母直接建立
print(Fraction(10, 6))  # 5/3，自動約分

# ── 3.11 隨機選擇 ─────────────────────────────────────
values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))  # 隨機選一個元素
print(random.sample(values, 3))  # 取 3 個不重複樣本

# shuffle 會直接修改原始列表順序
random.shuffle(values)
print(values)  # 打亂後的序列

# randint 產生包含端點的整數範圍
print(random.randint(0, 10))  # 0~10 的整數

# seed 可以指定隨機數種子，使結果可重現
random.seed(42)
print(random.random())  # 0~1 之間的浮點數
