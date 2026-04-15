# U03. 字串格式化效能與陷阱（2.14–2.20）
# 本範例示範三個字串處理的效能與陷阱：
# 1. join 方法比 + 運算子更高效
# 2. format_map 如何處理缺失的鍵
# 3. bytes 物件索引的行為差異

import timeit

# ── join 效能優於 + （2.14）──────────────────────────
parts = [f"item{i}" for i in range(1000)]
# 建立一個包含 1000 個字串的列表，用於測試串接效能。

def bad_concat():
    s = ""
    for p in parts:
        s += p  # 每次 += 都會建立新的字串物件，導致 O(n²) 的時間複雜度
    return s

def good_join():
    return "".join(parts)  # join 一次分配足夠的記憶體，O(n) 時間複雜度

# 使用 timeit 測量效能，執行 500 次
t1 = timeit.timeit(bad_concat, number=500)
t2 = timeit.timeit(good_join, number=500)
print(f"+串接: {t1:.3f}s  join: {t2:.3f}s")
# join 通常快得多，因為它避免了重複建立字串。

# ── format_map 處理缺失鍵（2.15）─────────────────────
class SafeSub(dict):
    # 自定義 dict 子類，繼承 dict 並覆寫 __missing__ 方法
    def __missing__(self, key: str) -> str:
        # 當鍵不存在時，返回保留原始佔位符的字串，而非拋出 KeyError
        return "{" + key + "}"

name = "Guido"
s = "{name} has {n} messages."
# 字串中有 {name} 和 {n} 兩個佔位符，但 n 不存在於變數中。
print(s.format_map(SafeSub(vars())))  # 'Guido has {n} messages.'（n 不存在也不報錯）
# SafeSub(vars()) 將全域變數字典包裝，缺失鍵時保留 {key} 格式。

# ── bytes 索引回傳整數（2.20）────────────────────────
a = "Hello"  # 字串
b = b"Hello"  # bytes 物件
print(a[0])  # 'H'（字元）
print(b[0])  # 72（整數 = ord('H')）
# bytes 索引返回對應字元的 ASCII 整數值，而非字元本身。

# bytes 不能直接 format，需先格式化再 encode
# 先用 format 格式化字串，再 encode 成 bytes
print("{:10s} {:5d}".format("ACME", 100).encode("ascii"))
# b'ACME            100'
# 這是處理 bytes 格式化的正確方式。
