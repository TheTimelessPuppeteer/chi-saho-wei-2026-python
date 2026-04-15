# U8. 字典最值為何常用 zip(values, keys)（1.8）

# 在字典中找最值時，經常需要同時取得值和對應的鍵
# zip(values, keys) 可以將值和鍵配對，讓 min/max 函式能正確比較

prices = {'A': 2.0, 'B': 1.0, 'C': 3.0, 'D': 1.5}
print(f"價格字典: {prices}")

# 方法1: min(prices) - 只得到鍵的最小值（字母序）
min_key = min(prices)
print(f"鍵的最小值 (字母序): '{min_key}'")

# 方法2: min(prices.values()) - 只得到值的最小值，不知道是哪個鍵
min_value = min(prices.values())
print(f"值的最小值: {min_value} (但不知道是哪個鍵)")

# 方法3: min(zip(prices.values(), prices.keys())) - 同時得到值和鍵
min_pair = min(zip(prices.values(), prices.keys()))
print(f"最小值和對應鍵: 值={min_pair[0]}, 鍵='{min_pair[1]}'")

# 為什麼要用 zip(values, keys) 而不是 zip(keys, values)？
print("\n--- 為什麼用 zip(values, keys) ---")
print("因為我們想根據「值」來比較，但回傳「鍵值對」")
print("zip(values, keys) 讓第一個元素是值（用來比較），第二個是鍵（用來識別）")

# 比較不同的 zip 順序
print("\n--- 比較不同 zip 順序 ---")
pair_vk = min(zip(prices.values(), prices.keys()))  # 值在前，鍵在後
pair_kv = min(zip(prices.keys(), prices.values()))   # 鍵在前，值在後

print(f"zip(values, keys): {pair_vk} - 根據值比較")
print(f"zip(keys, values): {pair_kv} - 根據鍵比較")

# 使用 key 參數的現代方法
print("\n--- 使用 key 參數的現代方法 ---")

# 找值最小的項目
min_by_value = min(prices.items(), key=lambda x: x[1])
print(f"值最小的項目: {min_by_value}")

# 找鍵最小的項目
min_by_key = min(prices.items(), key=lambda x: x[0])
print(f"鍵最小的項目: {min_by_key}")

# zip 方法 vs key 方法的比較
print("\n--- zip vs key 方法比較 ---")
print("zip 方法:")
print("  + 直觀：min(zip(values, keys)) 直接給值和鍵")
print("  + 適用於簡單情況")
print("  - 需要記住順序：zip(values, keys)")

print("\nkey 方法:")
print("  + 靈活：可以用複雜的 key 函式")
print("  + 直接得到 (key, value) 元組")
print("  - 語法稍複雜：key=lambda x: x[1]")

# 實際應用場景
print("\n--- 實際應用場景 ---")

# 學生成績範例
scores = {'Alice': 95, 'Bob': 87, 'Charlie': 92, 'David': 87}
print(f"學生成績: {scores}")

# 找最高分學生
top_student = max(zip(scores.values(), scores.keys()))
print(f"最高分: {top_student[0]} 分，學生: {top_student[1]}")

# 找最低分學生
bottom_student = min(zip(scores.values(), scores.keys()))
print(f"最低分: {bottom_student[0]} 分，學生: {bottom_student[1]}")

# 處理同分情況
print("\n--- 處理同分情況 ---")
# 同分時，zip 會比較第二個元素（鍵），確保穩定排序
same_scores = {'Zoe': 85, 'Amy': 85, 'Ben': 85}
sorted_by_score = sorted(zip(same_scores.values(), same_scores.keys()))
print(f"同分排序結果: {sorted_by_score}")
print("同分時按鍵的字母序排序")

# 注意事項
print("\n--- 注意事項 ---")
print("1. zip() 建立的是迭代器，耗盡後不能重用")
print("2. 如果只需要鍵，可以用 min(d, key=d.get)")
print("3. 如果只需要值，用 min(d.values()) 或 min(d.items(), key=itemgetter(1))")
print("4. zip(values, keys) 的順序很重要：值用來比較，鍵用來識別")

