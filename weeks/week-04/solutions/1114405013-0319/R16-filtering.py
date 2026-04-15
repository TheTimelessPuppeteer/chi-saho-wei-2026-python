# R16. 過濾：推導式 / generator / filter / compress（1.16）

# 範例資料：一個包含正數、負數和零的列表
mylist = [1, 4, -5, 10]

# 方法1: 列表推導式過濾正數
# [n for n in mylist if n > 0] 會建立一個新列表，只包含大於0的元素
positive_list = [n for n in mylist if n > 0]
print("列表推導式過濾正數:", positive_list)

# 方法2: 生成器表達式過濾正數
# (n for n in mylist if n > 0) 會建立一個生成器，只有在需要時才計算值
pos = (n for n in mylist if n > 0)
print("生成器表達式過濾正數:", list(pos))  # 轉成列表來顯示

# 另一個範例：過濾字串是否能轉成整數
values = ['1', '2', '-3', '-', 'N/A']

# 定義一個函式來檢查字串是否能轉成整數
def is_int(val):
    try:
        int(val)  # 嘗試轉換
        return True  # 成功就回傳 True
    except ValueError:  # 如果發生 ValueError，表示不能轉換
        return False

# 方法3: 使用 filter 函式過濾能轉成整數的字串
# filter(is_int, values) 會過濾出滿足 is_int 條件的元素
int_values = list(filter(is_int, values))
print("filter 過濾能轉成整數的字串:", int_values)

# 方法4: 使用 compress 過濾
# compress 根據第二個可迭代物的布林值來選擇第一個可迭代物的元素
from itertools import compress

addresses = ['a1', 'a2', 'a3']  # 地址列表
counts = [0, 3, 10]  # 對應的計數
# [n > 5 for n in counts] 建立布林列表，標記哪些計數大於5
more5 = [n > 5 for n in counts]
print("counts > 5 的布林列表:", more5)
# compress(addresses, more5) 只保留對應 True 的地址
filtered_addresses = list(compress(addresses, more5))
print("compress 過濾地址（計數 > 5）:", filtered_addresses)

# 總結：不同的過濾方法
print("\n--- 過濾方法比較 ---")
print("列表推導式: 建立新列表，適合小資料")
print("生成器表達式: 建立生成器，適合大資料，節省記憶體")
print("filter: 使用函式過濾，函式式程式設計風格")
print("compress: 根據布林序列過濾，適合兩個相關序列")

