# R3. deque 保留最後 N 筆（1.3）
# deque 是雙端隊列 (double-ended queue)，可從兩端插入或刪除。
# 這裡示範兩個常見用途：
# 1. 使用 maxlen 讓 deque 自動丟掉最舊元素
# 2. 基本的 append/appendleft/pop/popleft 操作

from collections import deque

# 使用 maxlen 限制長度為 3，維持最近三筆資料
q = deque(maxlen=3)
print("初始 q", q)
q.append(1); q.append(2); q.append(3)
print("加入 1,2,3 ->", q)
q.append(4)  # 自動丟掉最舊的 1
print("加 4 後 (maxlen=3), 最舊的 1 被移除 ->", q)

# 若沒有設定 maxlen，deque 可以在兩端靈活操作
q = deque()
print("新 deque", q)
q.append(1); q.appendleft(2)
print("append(1) 和 appendleft(2) ->", q)
print("pop() 回傳並移除尾端：", q.pop(), "剩下", q)
q.append(3); q.appendleft(4)
print("再添 3 和 4 ->", q)
print("popleft() 回傳並移除頭端：", q.popleft(), "剩下", q)

# 註解總結：
# - deque 可視作 list 的高效雙端操作版，頭尾操作 O(1)。
# - maxlen 參數會自動在 append 時丟棄舊元素，適合實作固定長度的緩衝。
# - appendleft 與 popleft 允許從前面新增/刪除。
# - q.pop() 跟 list 的 pop() 類似，但 deque 不支援索引。

