# R9. 兩字典相同點：keys/items 集合運算（1.9）
# 字典的 keys() 與 items() 可以直接進行集合運算，很方便找相同、差異的鍵或項目。

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}
print("字典 a:", a)
print("字典 b:", b)

# 找兩字典都有的鍵（交集）
common_keys = a.keys() & b.keys()
print("a 和 b 都有的鍵（交集）:", common_keys)

# 找只在 a 中有，不在 b 中的鍵（差集）
only_in_a = a.keys() - b.keys()
print("只在 a 中的鍵（差集）:", only_in_a)

# 找兩字典都有的鍵值對（items 交集）
# 注意：items() 比較的是鍵值對都相同，不只是鍵
common_items = a.items() & b.items()
print("a 和 b 都有的鍵值對（items 交集）:", common_items)

# 使用集合運算過濾鍵，建立新字典
# a.keys() - {'z', 'w'} 會讓字典只保留 'x' 和 'y'
c = {k: a[k] for k in a.keys() - {'z', 'w'}}
print("過濾後的字典 c（移除 'z'）:", c)

# 詳細說明：
# - a.keys() & b.keys() 找交集（都有的鍵）。
# - a.keys() - b.keys() 找差集（只在 a 中的鍵）。
# - a.keys() | b.keys() 可找聯集（所有鍵）。
# - a.items() & b.items() 比較整個鍵值對，必須鍵和值都相同。
# - 集合運算搭配字典推導式，可高效進行鍵值篩選。
