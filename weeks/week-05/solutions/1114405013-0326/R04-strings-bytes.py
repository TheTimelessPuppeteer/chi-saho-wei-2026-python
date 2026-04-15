# R04. 位元組字串操作（2.20）
# bytes / bytearray 支援大部分字串方法，但有幾個重要差異

import re

# bytes 是不可變資料，類似 immutable 的字節序列
data = b"Hello World"
print(data[0:5])  # b'Hello'，切片結果仍然是 bytes
print(data.startswith(b"Hello"))  # True，startswith 也支援 bytes
print(data.split())  # [b'Hello', b'World']，split 會依空白分割 bytes
print(data.replace(b"Hello", b"Hello Cruel"))  # b'Hello Cruel World'，replace 也支援 bytes

# 正則表達式也必須使用 bytes 模式
raw = b"FOO:BAR,SPAM"
print(re.split(rb"[:,]", raw))  # [b'FOO', b'BAR', b'SPAM']，前綴 r 表示 raw string

# 差異 1：bytes 索引回傳整數，而字串回傳字元
s = "Hello"
b = b"Hello"
print(s[0])  # 'H'（字元）
print(b[0])  # 72（整數，即 ord('H')）

# 差異 2：不能直接對 bytes 使用 format()，需先格式化成 str 再 encode
formatted = "{:10s} {:10d}".format("ACME", 100).encode("ascii")
print(formatted)  # b'ACME            100'

# bytes 與 str 之間的轉換
text = "中文測試"
encoded = text.encode("utf-8")  # 將字串編碼成 bytes
print(encoded)  # b'...'
decoded = encoded.decode("utf-8")  # 將 bytes 解碼回字串
print(decoded)

# bytearray 是可變的 bytes 類型，可以就地修改
mutable = bytearray(b"Hello")
mutable[0] = ord("h")  # 修改第一個位元組
print(mutable)  # bytearray(b'hello')
print(bytes(mutable))  # 轉換回不可變 bytes
