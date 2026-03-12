# R5. 優先佇列 PriorityQueue（1.5）
# 建立一個「最大」優先佇列（highest priority 先出）。
# Python 的 heapq 本身是小根堆，因此我們將 priority 取負。

import heapq

class PriorityQueue:
    def __init__(self):
        # _queue 存放元組 (優先度, 索引, 項目)
        # 優先度為負值以模擬最大堆。
        # 索引用來保持相同優先度時的 FIFO 行為。
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # 呼叫時輸入實際項目與優先度
        # 把 (-priority, index, item) 推進 heap
        heapq.heappush(self._queue, (-priority, self._index, item))
        print(f"push: item={item}, priority={priority}, stored=({-priority},{self._index},{item})")
        self._index += 1

    def pop(self):
        # pop 出最小的 tuple，對應實際最大 priority
        popped = heapq.heappop(self._queue)
        print(f"pop returns tuple {popped}")
        return popped[-1]

# 以下示範用法：
if __name__ == '__main__':
    pq = PriorityQueue()
    pq.push('task1', priority=1)
    pq.push('task2', priority=5)
    pq.push('task3', priority=3)
    pq.push('task4', priority=5)
    print("pop ->", pq.pop())
    print("pop ->", pq.pop())
    print("pop ->", pq.pop())

# 理解重點：
# 1. 優先佇列根據 priority 排序，高數值優先。
# 2. 因為 heapq 只有小根堆，我們用 -priority 變成小值優先。
# 3. index 確保相同 priority 時先插入者先出。
# 4. push/pop 均為 O(log n) 操作。

