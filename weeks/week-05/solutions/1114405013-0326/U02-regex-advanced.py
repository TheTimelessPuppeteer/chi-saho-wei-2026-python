# U02. 正則表達式進階技巧（2.4–2.6）
# 本範例示範三個進階正則表達式技巧：
# 1. 預編譯正則式以提升效能
# 2. 使用 sub 方法的回呼函數進行複雜替換
# 3. 保持大小寫一致的替換

import re
import timeit
from calendar import month_abbr

# ── 預編譯效能（2.4）──────────────────────────────────
text = "Today is 11/27/2012. PyCon starts 3/13/2013."
# 預編譯正則式可以避免重複編譯，提升效能。
# 這裡的正則式匹配日期格式：月/日/年，每個部分都是數字。
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")

# 定義兩個函數：一個使用模組級別的 re.findall，一個使用預編譯的 datepat.findall
def using_module():
    # 每次呼叫都會重新編譯正則式
    return re.findall(r"(\d+)/(\d+)/(\d+)", text)

def using_compiled():
    # 使用預編譯的正則式物件，無需重複編譯
    return datepat.findall(text)

# 使用 timeit 測量效能，執行 50,000 次
t1 = timeit.timeit(using_module, number=50_000)
t2 = timeit.timeit(using_compiled, number=50_000)
print(f"直接呼叫: {t1:.3f}s  預編譯: {t2:.3f}s")
# 預編譯通常會更快，因為編譯只發生一次。

# ── sub 回呼函數（2.5）────────────────────────────────
# sub 方法可以接受回呼函數作為替換參數，允許進行複雜的替換邏輯。
def change_date(m: re.Match) -> str:
    # 回呼函數接收匹配物件 m
    # m.group(1) 是月份，m.group(2) 是日期，m.group(3) 是年份
    mon_name = month_abbr[int(m.group(1))]  # 將月份數字轉成英文縮寫
    # 返回格式化的字串：日 月 年
    return f"{m.group(2)} {mon_name} {m.group(3)}"

# 使用 sub 方法，將匹配到的日期替換為格式化的字串
print(datepat.sub(change_date, text))
# 'Today is 27 Nov 2012. PyCon starts 13 Mar 2013.'
# 這展示了如何使用回呼函數進行動態替換。

# ── 保持大小寫一致的替換（2.6）───────────────────────
# 這個技巧確保替換後的字串保持與原始匹配字串相同的大小寫格式。
def matchcase(word: str):
    # 內部函數 replace 作為 sub 的回呼函數
    def replace(m: re.Match) -> str:
        t = m.group()  # 獲取匹配的字串
        if t.isupper():
            # 如果匹配字串全大寫，返回替換字全大寫
            return word.upper()
        if t.islower():
            # 如果匹配字串全小寫，返回替換字全小寫
            return word.lower()
        if t[0].isupper():
            # 如果匹配字串首字母大寫，返回替換字首字母大寫
            return word.capitalize()
        # 其他情況，返回原始替換字
        return word
    # 返回內部函數作為回呼函數
    return replace

# 測試字串，包含不同大小寫的 "python"
s = "UPPER PYTHON, lower python, Mixed Python"
# 使用 sub 進行替換，忽略大小寫匹配，但使用 matchcase 保持大小寫一致
print(re.sub("python", matchcase("snake"), s, flags=re.IGNORECASE))
# 'UPPER SNAKE, lower snake, Mixed Snake'
# 替換後的大小寫與原始匹配字串一致。
