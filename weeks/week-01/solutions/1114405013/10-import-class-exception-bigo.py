# 10 模組、類別、例外與 Big-O（最低門檻）範例
# 本檔案展示模組導入、類別定義、例外處理和 Big-O 概念

print("=" * 60)
print("10. 模組、類別、例外與 Big-O（最低門檻）")
print("=" * 60)

# ============================================================
# 1. 模組導入和使用
# ============================================================
print("\n1. 模組導入 - collections.deque")
print("-" * 60)

from collections import deque

q = deque(maxlen=2)
q.append(1)
q.append(2)
q.append(3)  # 自動丟掉最舊

print(f"建立 deque(maxlen=2)")
print(f"依序加入: 1, 2, 3")
print(f"結果（最多保留 2 個元素）: {list(q)}")
print("# 說明：deque 提供高效的首尾操作，maxlen 限制長度")

# ============================================================
# 2. 類別和物件
# ============================================================
print("\n2. 類別定義和物件創建")
print("-" * 60)

class User:
    def __init__(self, user_id):
        self.user_id = user_id

u = User(42)
uid = u.user_id

print(f"定義 User 類別")
print(f"建立 User 物件，user_id = 42")
print(f"訪問物件屬性 u.user_id = {uid}")
print("# 說明：__init__ 是初始化方法，self 代表物件本身")

# ============================================================
# 3. 例外處理
# ============================================================
print("\n3. 例外處理 - try/except")
print("-" * 60)

def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

test_values = [42, "hello", "123", 3.14]
print(f"測試函式 is_int() 的結果：")
for val in test_values:
    result = is_int(val)
    print(f"  is_int({repr(val):8}) = {result}")
print("# 說明：try 嘗試執行，except 捕捉特定例外")

# ============================================================
# 4. Big-O 時間複雜度概念
# ============================================================
print("\n4. Big-O 時間複雜度提示")
print("-" * 60)

print("常見操作的時間複雜度（Big-O）：")
print("  list.append()    → O(1)   （平均情況，均攤）")
print("  list 切片        → O(N)   （取決於切片長度）")
print("  list.insert(0)   → O(N)   （需要移動其他元素）")
print("  dict 查詢        → O(1)   （平均情況）")
print("  list 查詢        → O(N)   （需要逐一檢查）")
print("# 說明：Big-O 描述算法效能如何隨資料量擴展")

# ============================================================
# 5. 綜合示例
# ============================================================
print("\n5. 綜合應用範例")
print("-" * 60)

from collections import deque

class Task:
    def __init__(self, task_id, priority):
        self.task_id = task_id
        self.priority = priority
    
    def __repr__(self):
        return f"Task({self.task_id}, priority={self.priority})"

# 建立任務佇列
task_queue = deque(maxlen=5)
tasks = [Task(1, 3), Task(2, 1), Task(3, 2)]

for task in tasks:
    task_queue.append(task)

print(f"任務佇列: {list(task_queue)}")

# 找出優先級最高的任務（優先級數值最小）
highest_priority = min(tasks, key=lambda t: t.priority)
print(f"優先級最高的任務: {highest_priority}")

# 測試是否能轉換為整數
test_inputs = ["1", "abc", "99"]
print(f"輸入驗證結果:")
for inp in test_inputs:
    valid = is_int(inp)
    print(f"  '{inp}' 是整數: {valid}")

print("\n" + "=" * 60)
print("範例執行完成")
print("=" * 60)
