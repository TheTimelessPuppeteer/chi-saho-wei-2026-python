# U5. 優先佇列為何要加 index（1.5）

# 在 Python 中實現優先隊列時，如果優先級相同，heapq 會比較 tuple 的下一個元素
# 如果下一個元素是自訂物件且不支援比較運算子，會發生 TypeError
# 解決方法：在優先級和物件之間插入一個唯一索引

import heapq

class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Item('{self.name}')"

# 錯誤示範：不加索引
print("--- 錯誤示範：不加索引 ---")
pq_bad = []
try:
    heapq.heappush(pq_bad, (-1, Item('a')))  # 優先級 -1（越高越優先）
    heapq.heappush(pq_bad, (-1, Item('b')))  # 同優先級，會嘗試比較 Item
    print("沒有錯誤？這不太對...")
except TypeError as e:
    print(f"TypeError: {e}")
    print("原因：同優先級時 heapq 會比較 Item 物件，但 Item 沒有定義 < 運算子")

# 正確方法：加索引避免比較物件
print("\n--- 正確方法：加索引 ---")
pq = []
idx = 0  # 唯一索引

# 推入元素：(優先級, 索引, 物件)
heapq.heappush(pq, (-1, idx, Item('a')))
idx += 1
heapq.heappush(pq, (-1, idx, Item('b')))
idx += 1
heapq.heappush(pq, (-2, idx, Item('c')))  # 更高優先級（-2 < -1）
idx += 1

print("優先隊列內容:", pq)

# 彈出元素（按優先級順序）
print("\n--- 彈出順序 ---")
while pq:
    priority, index, item = heapq.heappop(pq)
    print(f"彈出: 優先級={-priority}, 索引={index}, 項目={item}")

# 為什麼需要索引？
print("\n--- 為什麼需要索引？ ---")
print("1. 當優先級相同時，避免比較自訂物件")
print("2. 索引提供穩定的排序順序")
print("3. 確保同優先級元素的 FIFO 順序")
print("4. 物件可能沒有自然排序，或排序很慢")

# 實際應用範例：任務調度
print("\n--- 實際應用：任務調度 ---")

class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __repr__(self):
        return f"Task('{self.name}', priority={self.priority})"

task_queue = []
task_id = 0

# 新增任務
tasks = [
    ("寫報告", 2),
    ("開會", 1),
    ("回信", 3),
    ("訂餐", 2),
]

for name, priority in tasks:
    heapq.heappush(task_queue, (priority, task_id, Task(name, priority)))
    task_id += 1

print("任務隊列:")
for priority, tid, task in task_queue:
    print(f"  優先級 {priority}: {task}")

print("\n執行順序:")
while task_queue:
    priority, tid, task = heapq.heappop(task_queue)
    print(f"執行: {task} (任務ID: {tid})")

# 注意事項
print("\n--- 注意事項 ---")
print("1. 優先級越小越優先（常用負數表示）")
print("2. 索引必須唯一且遞增")
print("3. tuple 順序：(優先級, 索引, 資料)")
print("4. 適合處理大量資料的優先排序")

