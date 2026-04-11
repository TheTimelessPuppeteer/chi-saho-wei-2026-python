# U01. 字串分割與匹配的陷阱（2.1–2.11）
# 本範例示範三個常見陷阱：
# 1. re.split 中捕獲分組會保留分隔符
# 2. startswith 的參數若是多選集，必須使用 tuple
# 3. strip 只會刪除開頭與結尾的空白，不會處理字串中間的空白

import re

# ── 捕獲分組保留分隔符（2.1）─────────────────────────
line = "asdf fjdk; afed, fjek,asdf, foo"
# re.split 在正則式中如果包含捕獲分組，用來分割的分隔符會被保留下來。
# 這個例子中，分隔的條件是分號、逗號或空白字元，後面可接零個空白。
fields = re.split(r"(;|,|\s)\s*", line)
# fields 的內容會是 ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']
# 偶數索引位置是分割後的實際值，奇數索引位置是分隔符。
values = fields[::2]  # 取得索引 0,2,4... 的實際文字值
delimiters = fields[1::2] + [""]
# 將分隔符補上空字串，避免最後一個值後面沒有分隔符時丟失內容。
rebuilt = "".join(v + d for v, d in zip(values, delimiters))
# 用 zip 將值與對應的分隔符配對，再組回原始字串。
print(rebuilt)  # 'asdf fjdk;afed,fjek,asdf,foo'
# 注意：re.split 的捕獲分組機制會保留分隔符，這是常見的陷阱。

# ── startswith 必須傳 tuple（2.2）────────────────────
url = "http://www.python.org"
choices = ["http:", "ftp:"]
# startswith 如果傳入 sequence，必須是 tuple 而不能是 list。
# 傳入 list 會引發 TypeError，因此這裡先示範錯誤情況。
try:
    url.startswith(choices)  # type: ignore[arg-type]
except TypeError as e:
    print(f"TypeError: {e}")  # 不能傳 list！
# 正確做法：將清單轉成 tuple，或直接使用 tuple 常量。
print(url.startswith(tuple(choices)))  # True（轉成 tuple 才行）

# ── strip 只處理頭尾，不處理中間（2.11）──────────────
s = "  hello     world  "
# strip 只會去除字串左右兩端的空白，字串中間多餘的空白不受影響。
print(repr(s.strip()))  # 'hello     world'（中間多餘空白還在）
# replace(" ", "") 會移除字串中所有空白，包括詞與詞之間必要的空白。
print(repr(s.replace(" ", "")))  # 'helloworld'（過頭，連詞間空白也消）
# 如果希望把中間連續空白收斂為單一空白，可以先 strip，再用正則取代。
print(repr(re.sub(r"\s+", " ", s.strip())))  # 'hello world'（正確）

# 生成器逐行清理（高效，不預載入記憶體）
lines = ["  apple  \n", "  banana  \n"]
# 這裡用 generator expression 逐一 strip 每行內容，避免先建立新的列表。
for line in (l.strip() for l in lines):
    print(line)
