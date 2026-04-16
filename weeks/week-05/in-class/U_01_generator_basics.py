# Understand（理解）- 生成器概念
# 生成器是使用 yield 的函式，會回傳一個可迭代且懶惰產生元素的物件。
# 它只會在需要時才計算下一個元素，適合處理大量資料或無限序列。


def frange(start, stop, step):
    # 模擬 range() 的浮點版，逐步產生從 start 到 stop 的值
    x = start
    while x < stop:
        yield x
        x += step


result = list(frange(0, 2, 0.5))
print(f"frange(0, 2, 0.5): {result}")


def countdown(n):
    # yield 會暫停函式執行並回傳值，下一次呼叫 next() 時從暫停點繼續
    print(f"Starting countdown from {n}")
    while n > 0:
        yield n
        n -= 1
    print("Done!")


print("\n--- 建立生成器 ---")
c = countdown(3)
print(f"生成器物件: {c}")

print("\n--- 逐步迭代 ---")
print(f"next(c): {next(c)}")
print(f"next(c): {next(c)}")
print(f"next(c): {next(c)}")

try:
    next(c)
except StopIteration:
    # 當生成器耗盡時，next() 會丟出 StopIteration
    print("StopIteration!")


def fibonacci():
    # 無限 Fibonacci 序列生成器，使用 yield 依序產生數值
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print("\n--- Fibonacci 生成器 ---")
fib = fibonacci()
for i in range(10):
    print(next(fib), end=" ")
print()


def chain_iter(*iterables):
    # yield from 用來簡化迭代子生成器或序列
    for it in iterables:
        yield from it


print("\n--- yield from 用法 ---")
result = list(chain_iter([1, 2], [3, 4], [5, 6]))
print(f"chain_iter: {result}")


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __iter__(self):
        # 讓 Node 物件本身可迭代
        return iter(self.children)

    def depth_first(self):
        # 以生成器遞迴實作深度優先搜尋
        yield self
        for child in self:
            yield from child.depth_first()


print("\n--- 樹的深度優先遍歷 ---")
root = Node(0)
root.add_child(Node(1))
root.add_child(Node(2))
root.children[0].add_child(Node(3))
root.children[0].add_child(Node(4))

for node in root.depth_first():
    print(node.value, end=" ")
print()


def flatten(items):
    # 巢狀序列攤平生成器，遞迴展開所有可迭代元素
    for x in items:
        if hasattr(x, "__iter__") and not isinstance(x, str):
            yield from flatten(x)
        else:
            yield x


print("\n--- 巢狀序列攤平 ---")
nested = [1, [2, [3, 4]], 5]
print(f"展開: {list(flatten(nested))}")

