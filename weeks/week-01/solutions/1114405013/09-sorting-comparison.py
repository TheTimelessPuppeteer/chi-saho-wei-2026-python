from operator import itemgetter
from itertools import groupby

# 9 比較、排序與 key 函式

# 1. 基本比較
print('a < b:', 'a' < 'b')
print('(1, 2) < (1, 3):', (1, 2) < (1, 3))
print('(1, 2) < (2, 0):', (1, 2) < (2, 0))
# tuple 比較是逐元素比較，先比第一個，再比第二個。

# 2. sorted() 搭配 key
products = [
    {'name': 'apple', 'price': 120},
    {'name': 'banana', 'price': 80},
    {'name': 'cherry', 'price': 150},
]
sorted_by_price = sorted(products, key=lambda x: x['price'])
print('sorted_by_price =', sorted_by_price)
# 輸出: 依照 price 由小到大排序

# 3. min() / max() 搭配 key
cheapest = min(products, key=itemgetter('price'))
most_expensive = max(products, key=itemgetter('price'))
print('cheapest =', cheapest)
print('most_expensive =', most_expensive)
# 使用 itemgetter 可以更快取出字典欄位做比較

# 4. Top-N 範例
scores = [
    {'name': 'Alice', 'score': 88},
    {'name': 'Bob', 'score': 95},
    {'name': 'Carol', 'score': 82},
    {'name': 'David', 'score': 91},
]
top2 = sorted(scores, key=lambda x: x['score'], reverse=True)[:2]
print('top2 =', top2)
# 取最高兩名，先反向排序再取前兩個

# 5. dict 排序範例
grades = {'Alice': 85, 'Bob': 79, 'Carol': 92}
sorted_by_name = sorted(grades.items())
sorted_by_score = sorted(grades.items(), key=lambda item: item[1])
print('sorted_by_name =', sorted_by_name)
print('sorted_by_score =', sorted_by_score)
# 字典本身無序，sorted(grades.items()) 可以把項目轉成 tuple 列表排序

# 6. 自訂物件排序範例
class Item:
    def __init__(self, uid, price):
        self.uid = uid
        self.price = price
    def __repr__(self):
        return f"Item(uid={self.uid!r}, price={self.price!r})"

items = [Item('b', 50), Item('a', 100), Item('c', 75)]
sorted_items = sorted(items, key=lambda x: x.price)
print('sorted_items =', sorted_items)
# 透過 key 可以對 object 屬性排序

# 7. 進階排序：多欄位排序
records = [
    {'priority': 1, 'index': 2, 'task': 'clean'},
    {'priority': 1, 'index': 1, 'task': 'cook'},
    {'priority': 2, 'index': 1, 'task': 'sleep'},
]
# 使用 tuple 可以同時排序 priority 與 index
sorted_records = sorted(records, key=lambda x: (x['priority'], x['index']))
print('sorted_records =', sorted_records)
# 當 key 回傳 tuple 時，會依 tuple 的順序比較

# 8. groupby 前置排序
people = [
    {'name': 'Alice', 'city': 'Taipei'},
    {'name': 'Bob', 'city': 'Kaohsiung'},
    {'name': 'Carol', 'city': 'Taipei'},
    {'name': 'David', 'city': 'Taichung'},
]
people_sorted = sorted(people, key=itemgetter('city'))
for city, group in groupby(people_sorted, key=itemgetter('city')):
    print('city =', city, 'members =', list(group))
# groupby 使用前必須先排序，否則相同 key 會被分成多組
