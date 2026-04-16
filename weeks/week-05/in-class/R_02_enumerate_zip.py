# Remember（記憶）- enumerate() 和 zip()
# enumerate() 用於在迭代時同時取得索引和值
# zip() 用於將多個序列打包成元組序列

colors = ["red", "green", "blue"]

print("--- enumerate() 基本用法 ---")
# enumerate(iterable, start=0) 回傳 (index, value) 的元組
for i, color in enumerate(colors):
    print(f"{i}: {color}")

print("\n--- enumerate(start=1) ---")
# 可以指定起始索引，常用於 1-based 編號
for i, color in enumerate(colors, 1):
    print(f"第{i}個: {color}")

print("\n--- enumerate with 檔案 ---")
# 常見於處理檔案行號
lines = ["line1", "line2", "line3"]
for lineno, line in enumerate(lines, 1):
    print(f"行 {lineno}: {line}")

print("\n--- zip() 基本用法 ---")
# zip(*iterables) 將多個序列的對應元素打包成元組
names = ["Alice", "Bob", "Carol"]
scores = [90, 85, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

print("\n--- zip() 多個序列 ---")
# 可以同時處理多個序列
a = [1, 2, 3]
b = [10, 20, 30]
c = [100, 200, 300]
for x, y, z in zip(a, b, c):
    print(f"{x} + {y} + {z} = {x + y + z}")

print("\n--- zip() 長度不同 ---")
# zip() 會以最短序列為準，忽略多餘元素
x = [1, 2]
y = ["a", "b", "c"]
print(f"list(zip(x, y)): {list(zip(x, y))}")

from itertools import zip_longest

# zip_longest() 會以最長序列為準，用 fillvalue 填充短序列
print(f"zip_longest: {list(zip_longest(x, y, fillvalue=0))}")

print("\n--- 建立字典 ---")
# 常用於從兩個列表建立字典
keys = ["name", "age", "city"]
values = ["John", "30", "NYC"]
d = dict(zip(keys, values))
print(f"dict: {d}")

print("\n--- 解包 zip() ---")
# zip() 可以用 * 解包回原本的序列
zipped = list(zip(names, scores))
print(f"zipped: {zipped}")
n, s = zip(*zipped)  # 解包
print(f"names: {list(n)}, scores: {list(s)}")

print("\n--- enumerate() 與 zip() 結合 ---")
# 同時使用 enumerate 和 zip 處理多個序列
for i, (name, score) in enumerate(zip(names, scores)):
    print(f"第{i+1}名: {name} 得分 {score}")

