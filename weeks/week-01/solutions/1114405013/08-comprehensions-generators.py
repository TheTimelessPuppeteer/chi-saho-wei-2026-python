# 8 容器操作與推導式

# 8.1 列表推導式（List Comprehension）
nums = [1, -2, 3, 0, 5]
positive_squares = [x * x for x in nums if x > 0]
print('positive_squares =', positive_squares)
# 輸出: positive_squares = [1, 9, 25]

# 8.2 字典推導式（Dictionary Comprehension）
scores = {'Alice': 85, 'Bob': 72, 'Carol': 90}
passed = {name: score for name, score in scores.items() if score >= 80}
print('passed =', passed)
# 輸出: passed = {'Alice': 85, 'Carol': 90}

# 8.3 集合推導式（Set Comprehension）
words = ['apple', 'banana', 'apple', 'cherry']
unique_lengths = {len(w) for w in words}
print('unique_lengths =', unique_lengths)
# 輸出: unique_lengths = {5, 6}

# 8.4 生成器表達式（Generator Expression）
nums = [1, 2, 3, 4]
squares = (x * x for x in nums)
print('squares =', squares)
print('list(squares) =', list(squares))
# 輸出: list(squares) = [1, 4, 9, 16]

# 8.5 聚合運算示範
nums = [1, 2, 3, 4]
total = sum(x * x for x in nums)
print('total =', total)
# 輸出: total = 30
