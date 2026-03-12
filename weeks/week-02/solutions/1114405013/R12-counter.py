# R12. Counter 統計 + most_common（1.12）
# Counter 是 collections 模組中的一個強大工具，用於統計可雜湊物件的出現次數。
# 它繼承自 dict，所以可以進行所有字典操作，還提供額外的統計方法。

from collections import Counter

# 基本使用：統計單字出現次數
words = ['look', 'into', 'my', 'eyes', 'look']
print("原始單字列表:", words)

# 建立 Counter 物件，自動統計每個元素的出現次數
word_counts = Counter(words)
print("Counter 統計結果:", word_counts)
print("類型:", type(word_counts))
print()

# most_common(n) 回傳出現次數最多的 n 個元素（以 tuple 列表形式）
top3 = word_counts.most_common(3)
print("出現次數最多的 3 個單字:", top3)
print()

# update() 方法可以更新計數，接受可迭代物件
print("更新前:", word_counts)
word_counts.update(['eyes', 'eyes'])
print("更新後（新增兩個 'eyes'）:", word_counts)
print()

# 更多示範：數字統計
print("=== 數字統計示範 ===")
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
num_counts = Counter(numbers)
print("數字列表:", numbers)
print("統計結果:", num_counts)
print("最常見的 2 個數字:", num_counts.most_common(2))
print()

# 示範字典操作（因為 Counter 繼承自 dict）
print("=== 字典操作示範 ===")
print("Counter 作為字典使用:")
print("word_counts['look']:", word_counts['look'])
print("word_counts['not_exist']:", word_counts['not_exist'])  # 預設為 0
print("所有鍵:", list(word_counts.keys()))
print("所有值:", list(word_counts.values()))
print("所有項目:", list(word_counts.items()))
print()

# 示範運算
print("=== Counter 運算示範 ===")
c1 = Counter(['a', 'b', 'c', 'a'])
c2 = Counter(['a', 'b', 'b', 'd'])
print("c1:", c1)
print("c2:", c2)
print("c1 + c2 (合併):", c1 + c2)
print("c1 - c2 (差集):", c1 - c2)
print("c1 & c2 (交集):", c1 & c2)
print("c1 | c2 (聯集):", c1 | c2)

# 理解重點：
# 1. Counter 自動統計可雜湊物件的出現次數
# 2. most_common(n) 快速取得前 n 名
# 3. update() 可以累加新資料的統計
# 4. 支援所有字典操作，還能進行集合運算（+ - & |）
# 5. 適合用於文字分析、資料統計、投票計數等場景
