# R8. 字典運算：min/max/sorted + zip（1.8）
# 示範如何在字典上進行 min/max/sorted 運算。
# 字典本身沒有順序，但我們可以用 zip 將鍵值配對，然後操作。

prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}
print("原始字典:", prices)

# 使用 zip 將值與鍵配對，然後找最小值
# zip(prices.values(), prices.keys()) 會產生 [(45.23, 'ACME'), (612.78, 'AAPL'), (10.75, 'FB')]
# min 會比較第一個元素（價格），回傳最小的 tuple
min_price = min(zip(prices.values(), prices.keys()))
print("最低價格 (zip 方式):", min_price)

# 同理，找最大價格
max_price = max(zip(prices.values(), prices.keys()))
print("最高價格 (zip 方式):", max_price)

# 排序所有價格
sorted_prices = sorted(zip(prices.values(), prices.keys()))
print("價格排序 (zip 方式):", sorted_prices)

# 另一種方式：直接在鍵上操作，用 key 函數指定比較依據
# min(prices, key=lambda k: prices[k]) 會比較 prices[k] 的值，回傳鍵
min_key = min(prices, key=lambda k: prices[k])
print("最低價格的鍵:", min_key, "價格:", prices[min_key])

# 理解重點：
# - zip(values, keys) 將值與鍵配對成 tuple，方便比較。
# - min/max/sorted 預設比較 tuple 的第一個元素（價格）。
# - key=lambda k: prices[k] 讓 min 在鍵上操作，但比較的是值。
# - 這種技巧適用於字典的鍵值操作，無需額外轉換。
