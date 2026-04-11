# Remember（記憶）- 迭代器基礎概念
# 本範例介紹 Python 迭代器的核心概念：
# 迭代器協議、可迭代物件、迭代器物件的區別，以及如何實作自訂迭代器。

# 1. 迭代器協議的核心方法
# Python 的迭代器協議基於兩個魔術方法：__iter__ 和 __next__
# __iter__ 返回迭代器物件，__next__ 返回下一個元素或擲出 StopIteration
items = [1, 2, 3]

# iter() 呼叫物件的 __iter__() 方法，返回迭代器
it = iter(items)
print(f"迭代器: {it}")  # 顯示迭代器物件，通常是 <list_iterator object>

# next() 呼叫迭代器的 __next__() 方法，取得下一個元素
print(f"第一個: {next(it)}")  # 1
print(f"第二個: {next(it)}")  # 2
print(f"第三個: {next(it)}")  # 3

# 當沒有更多元素時，__next__() 會擲出 StopIteration 例外
try:
    next(it)
except StopIteration:
    print("迭代結束!")  # 迭代完成

# 2. 常見可迭代物件
# 可迭代物件是實作了 __iter__() 方法的物件，可以用於 for 迴圈或 iter()
print("\n--- 常見可迭代物件 ---")

# 列表：實作了 __iter__，返回 list_iterator
print(f"列表 iter: {iter([1, 2, 3])}")

# 字串：實作了 __iter__，返回 str_iterator
print(f"字串 iter: {iter('abc')}")

# 字典：實作了 __iter__，返回 dict_keyiterator（預設迭代鍵）
print(f"字典 iter: {iter({'a': 1, 'b': 2})}")

# 檔案：實作了 __iter__，逐行迭代
import io

f = io.StringIO("line1\nline2\nline3")  # 模擬檔案物件
print(f"檔案 iter: {iter(f)}")  # 返回檔案迭代器


# 3. 自訂可迭代物件
# 要建立自訂可迭代物件，需要實作 __iter__() 方法
# __iter__() 應該返回一個迭代器物件（實作 __next__()）
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        # 返回迭代器實例，每次呼叫都會建立新的迭代器
        return CountDownIterator(self.start)


class CountDownIterator:
    def __init__(self, start):
        self.current = start

    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # 沒有更多元素時擲出 StopIteration
        self.current -= 1
        return self.current + 1  # 返回當前值，然後遞減


print("\n--- 自訂迭代器 ---")
for i in CountDown(3):
    print(i, end=" ")  # 3 2 1
# CountDown 是可迭代物件，CountDownIterator 是迭代器

# 4. 迭代器 vs 可迭代物件
# 重要區別：可迭代物件有 __iter__，迭代器同時有 __iter__ 和 __next__
print("\n\n--- 迭代器 vs 可迭代物件 ---")

# 列表是可迭代物件（有 __iter__），但不是迭代器（沒有 __next__）
my_list = [1, 2, 3]
print(f"列表: 可迭代物件 ✓, 迭代器 ✗")

# 列表的 iter() 返回迭代器（有 __next__）
my_iter = iter(my_list)
print(f"iter(列表): 可迭代物件 ✗, 迭代器 ✓")

# 迭代器本身也是可迭代物件（有 __iter__，返回自己）
print(f"迭代器: 可迭代物件 ✓ (有__iter__), 迭代器 ✓ (有__next__)")

# 5. StopIteration 例外
# StopIteration 是迭代器協議的一部分，用來表示迭代結束
print("\n--- StopIteration 用法 ---")


# 手動遍歷（章節 4.1 風格）
# 這是 for 迴圈背後的運作方式
def manual_iter(items):
    it = iter(items)  # 取得迭代器
    while True:
        try:
            item = next(it)  # 嘗試取得下一個元素
            print(f"取得: {item}")
        except StopIteration:
            break  # 迭代結束，跳出迴圈


manual_iter(["a", "b", "c"])


# 使用預設值的版本
# next() 可以接受第二個參數作為預設值，當迭代結束時返回預設值
def manual_iter_default(items):
    it = iter(items)
    while True:
        item = next(it, None)  # 如果迭代結束，返回 None
        if item is None:
            break
        print(f"取得: {item}")


print("\n使用預設值:")
manual_iter_default(["a", "b", "c"])
# 這種方式避免了例外處理，更簡潔
