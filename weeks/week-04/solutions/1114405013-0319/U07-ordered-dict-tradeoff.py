# U7. OrderedDict 的取捨：保序但更吃記憶體（1.7）

# OrderedDict 會記住鍵值對的插入順序，但需要額外的記憶體來維護這個順序
# 從 Python 3.7+ 開始，普通 dict 也保持插入順序，但 OrderedDict 仍有其特殊用途

from collections import OrderedDict
import sys

# 建立 OrderedDict
print("--- OrderedDict 基本操作 ---")
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['baz'] = 3

print(f"OrderedDict 內容: {d}")
print(f"鍵的順序: {list(d.keys())}")
print(f"值的順序: {list(d.values())}")

# 比較：普通 dict（Python 3.7+ 也保持順序）
print("\n--- 比較普通 dict ---")
normal_dict = {'foo': 1, 'bar': 2, 'baz': 3}
print(f"普通 dict 內容: {normal_dict}")
print(f"鍵的順序: {list(normal_dict.keys())}")

# 記憶體使用比較
print("\n--- 記憶體使用比較 ---")
od = OrderedDict.fromkeys(range(1000))
nd = dict.fromkeys(range(1000))

od_size = sys.getsizeof(od)
nd_size = sys.getsizeof(nd)

print(f"OrderedDict (1000 鍵): {od_size} bytes")
print(f"普通 dict (1000 鍵): {nd_size} bytes")
print(f"OrderedDict 多用: {od_size - nd_size} bytes ({(od_size/nd_size - 1)*100:.1f}%)")

# OrderedDict 的特殊方法
print("\n--- OrderedDict 特殊方法 ---")

# move_to_end(): 將鍵移到最後
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(f"原始順序: {list(od.keys())}")
od.move_to_end('a')  # 將 'a' 移到最後
print(f"移動 'a' 到最後: {list(od.keys())}")

# popitem(last=True/False): 從最後或最前彈出
last_item = od.popitem(last=True)   # 預設從最後彈出
print(f"從最後彈出: {last_item}, 剩餘: {list(od.keys())}")

first_item = od.popitem(last=False)  # 從最前彈出
print(f"從最前彈出: {first_item}, 剩餘: {list(od.keys())}")

# OrderedDict 的應用場景
print("\n--- OrderedDict 應用場景 ---")
print("1. 需要預測性迭代順序的快取")
print("2. 實現 LRU (Least Recently Used) 快取")
print("3. 排序後的字典操作")
print("4. JSON 序列化需要保持順序")
print("5. 比較兩個字典的順序")

# 實際應用：簡單 LRU 快取
print("\n--- 實際應用：LRU 快取 ---")

class SimpleLRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            # 存取時將鍵移到最後（最近使用）
            self.cache.move_to_end(key)
            return self.cache[key]
        return None

    def put(self, key, value):
        if key in self.cache:
            # 更新現有鍵，移到最後
            self.cache.move_to_end(key)
        else:
            # 新鍵，檢查容量
            if len(self.cache) >= self.capacity:
                # 移除最舊的（最前面的）
                self.cache.popitem(last=False)
        self.cache[key] = value

# 測試 LRU 快取
cache = SimpleLRUCache(3)
cache.put('A', 1)
cache.put('B', 2)
cache.put('C', 3)
print(f"初始快取: {list(cache.cache.keys())}")

cache.get('A')  # 存取 A，將其移到最後
print(f"存取 A 後: {list(cache.cache.keys())}")

cache.put('D', 4)  # 新增 D，B 應該被淘汰
print(f"新增 D 後: {list(cache.cache.keys())}")

# 總結
print("\n--- OrderedDict vs 普通 dict ---")
print("普通 dict (Python 3.7+):")
print("  + 記憶體效率高")
print("  + 保持插入順序")
print("  - 無法重新排序")
print("  - 沒有 move_to_end 等方法")

print("\nOrderedDict:")
print("  + 完整順序控制 (move_to_end, popitem)")
print("  + 適合實現特定資料結構")
print("  - 記憶體使用較多")
print("  - 在現代 Python 中較少需要")

