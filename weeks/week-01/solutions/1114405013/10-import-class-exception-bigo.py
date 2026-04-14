# 10 模組、類別、例外與 Big-O

# 1. import 基礎
from collections import deque, namedtuple
from heapq import heappush, heappop, nlargest
from operator import attrgetter

print('--- import 範例 ---')

# deque 提供 O(1) 的左右端插入與刪除
dq = deque([2, 3, 4])
dq.appendleft(1)
dq.append(5)
print('deque =', dq)
print('popleft =', dq.popleft())
print('deque after popleft =', dq)
# deque 的 appendleft / popleft 是 O(1)，適合做雙端隊列

# namedtuple 與 class 的比較
User = namedtuple('User', ['user_id', 'name'])
user = User(user_id=101, name='Alice')
print('namedtuple user.user_id =', user.user_id)

class UserClass:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
    def __repr__(self):
        return f'UserClass(user_id={self.user_id!r}, name={self.name!r})'

user_obj = UserClass(102, 'Bob')
print('class user_obj.user_id =', user_obj.user_id)
print('class user_obj =', user_obj)
# class 可用於封裝資料與行為，同時方便直接存取屬性

# 2. heapq / PriorityQueue 範例
print('\n--- heapq / priority queue 範例 ---')
heap = []
heappush(heap, (2, 'task B'))
heappush(heap, (1, 'task A'))
heappush(heap, (3, 'task C'))
print('heap =', heap)
print('pop 最優先任務 =', heappop(heap))
# 透過 tuple 先比較 priority，再比較 item；tuple 本身可排序

# 3. min / max / nlargest 搭配 key
products = [
    {'uid': 'p1', 'price': 120},
    {'uid': 'p2', 'price': 80},
    {'uid': 'p3', 'price': 150},
]
cheapest = min(products, key=attrgetter('price')) if False else min(products, key=lambda x: x['price'])
most_expensive = max(products, key=lambda x: x['price'])
print('cheapest =', cheapest)
print('most_expensive =', most_expensive)
print('top 2 highest price =', nlargest(2, products, key=lambda x: x['price']))
# nlargest 在 k 比較小時效率比排序整個列表更好

# 4. 例外處理（try / except）
print('\n--- 例外處理範例 ---')
values = ['10', 'abc', '42', '3.14', '0']

def safe_int(val):
    try:
        return int(val)
    except ValueError:
        return None

int_values = [safe_int(v) for v in values if safe_int(v) is not None]
print('int_values =', int_values)
# 使用 try/except 過濾不能轉換為 int 的值，避免程式直接中斷

# 5. filter(is_int, values) 的示意
print('\n--- filter 與例外搭配 ---')

def is_int_string(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

valid_ints = list(filter(is_int_string, values))
print('valid_ints =', valid_ints)
# filter 會保留可以成功轉成 int 的字串

# 6. 基本 Big-O 觀念
print('\n--- Big-O 觀念 ---')
print('deque appendleft / popleft: O(1)')
print('list append / pop(end): O(1)')
print('heap push / pop: O(log N)')
print('sorted(list): O(N log N)')
print('nlargest(k, iterable): O(N log k)')
# 這些複雜度是用來比較資料結構與演算法效能的基礎
