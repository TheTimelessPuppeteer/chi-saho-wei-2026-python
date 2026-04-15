# U3. deque(maxlen=N) 為何能保留最後 N 筆（1.3）

# deque 是雙端隊列，maxlen 參數讓它成為固定大小的循環隊列
# 當超過 maxlen 時，舊的元素會自動被移除，只保留最新的 N 個元素

from collections import deque

# 建立 maxlen=3 的 deque
q = deque(maxlen=3)
print(f"初始 deque: {list(q)}")

# 加入元素，當超過 maxlen 時會自動移除舊元素
for i in [1, 2, 3, 4, 5]:
    q.append(i)
    print(f"加入 {i} 後: {list(q)}")

print(f"\n最終結果: {list(q)}")  # 只剩 [3, 4, 5]

# deque maxlen 的特性
print("\n--- deque maxlen 特性 ---")
print(f"maxlen 屬性: {q.maxlen}")
print(f"目前長度: {len(q)}")
print("當 append 時，如果長度超過 maxlen，會自動移除最左邊的元素")


# 比較：沒有 maxlen 的 deque
print("\n--- 比較：無 maxlen 的 deque ---")
unlimited = deque()
for i in [1, 2, 3, 4, 5]:
    unlimited.append(i)
print(f"無 maxlen deque: {list(unlimited)}")  # 保留所有元素

# 從左端加入的行為
print("\n--- 從左端加入 (appendleft) ---")
q2 = deque(maxlen=3)
for i in [1, 2, 3, 4]:
    q2.appendleft(i)
    print(f"appendleft {i}: {list(q2)}")

# maxlen 的應用場景
print("\n--- maxlen 應用場景 ---")
print("1. 保留最近的 N 個日誌")
print("2. 滑動窗口計算")
print("3. 最近使用記錄 (LRU)")
print("4. 訊息隊列限制")

# 實際應用範例：保留最近 5 個溫度讀值
print("\n--- 實際應用：溫度監控 ---")
temperatures = deque(maxlen=5)

# 模擬連續讀取溫度
for temp in [23.5, 24.1, 23.8, 24.3, 23.9, 24.5, 24.2]:
    temperatures.append(temp)
    print(f"最新溫度: {temp}°C, 最近 5 筆: {list(temperatures)}")

print(f"\n平均溫度 (最近 5 筆): {sum(temperatures)/len(temperatures):.1f}°C")

# 注意事項
print("\n--- 注意事項 ---")
print("1. maxlen 設定後不能改變")
print("2. 超出 maxlen 時，舊元素從左端移除")
print("3. appendleft 也會觸發 maxlen 限制")
print("4. maxlen=None 表示無限制（預設）")

