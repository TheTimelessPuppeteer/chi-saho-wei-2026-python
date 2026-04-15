# U6. defaultdict 為何比手動初始化乾淨（1.6）

# defaultdict 會在存取不存在的鍵時自動建立預設值
# 避免了手動檢查鍵是否存在和初始化的繁瑣程式碼

from collections import defaultdict

# 範例資料：鍵值對列表
pairs = [('a', 1), ('a', 2), ('b', 3)]
print(f"原始資料: {pairs}")

# 方法1: 手動檢查和初始化（繁瑣）
print("\n--- 方法1: 手動檢查 ---")
d = {}
for k, v in pairs:
    if k not in d:  # 每次都要檢查鍵是否存在
        d[k] = []   # 手動初始化為空列表
    d[k].append(v)  # 加入值

print(f"手動結果: {dict(d)}")

# 方法2: 使用 defaultdict（簡潔）
print("\n--- 方法2: defaultdict ---")
d2 = defaultdict(list)  # 指定預設值工廠為 list
for k, v in pairs:
    d2[k].append(v)  # 直接使用，不需要檢查

print(f"defaultdict 結果: {dict(d2)}")

# defaultdict 的其他預設值工廠
print("\n--- 其他預設值工廠 ---")

# int 預設值：用於計數
print("int 預設值（計數）:")
word_counts = defaultdict(int)
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
for word in words:
    word_counts[word] += 1  # 自動從 0 開始計數
print(f"單字計數: {dict(word_counts)}")

# set 預設值：收集唯一值
print("\nset 預設值（收集唯一值）:")
word_sets = defaultdict(set)
for word in words:
    word_sets[word[0]].add(word)  # 按首字母分組
print(f"按首字母分組: {dict(word_sets)}")

# 自訂函式作為預設值工廠
print("\n自訂預設值工廠:")
def default_value():
    return "預設值"

custom_dict = defaultdict(default_value)
custom_dict['existing'] = "實際值"
print(f"現有鍵: {custom_dict['existing']}")
print(f"不存在鍵: {custom_dict['missing']}")  # 自動呼叫 default_value()

# 比較：手動 vs defaultdict 的程式碼差異
print("\n--- 程式碼比較 ---")
print("手動方式需要:")
print("  if key not in d: d[key] = default_value")
print("  d[key].operation()")
print("\ndefaultdict 只需要:")
print("  d[key].operation()  # 自動處理")

# defaultdict 的應用場景
print("\n--- 應用場景 ---")
print("1. 分組統計：按條件將資料分組")
print("2. 計數器：統計出現次數")
print("3. 圖結構：鄰接表")
print("4. 快取：避免重複計算")
print("5. 多值字典：一個鍵對應多個值")

# 注意事項
print("\n--- 注意事項 ---")
print("1. defaultdict 仍然是 dict 的子類別")
print("2. 預設值工廠只在鍵不存在時呼叫")
print("3. 修改預設值會影響字典")
print("4. 適合用於初始化模式明確的場景")

