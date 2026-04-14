# R13. 字典列表排序 itemgetter（1.13）
# 此範例展示如何使用 operator 模組中的 itemgetter 函數
# 來對字典列表進行排序

# 從 operator 模組匯入 itemgetter
# itemgetter 是一個用於取得可迭代物件中指定索引項目的函數工廠
# 在排序情境中，我們通常用它來指定要依照哪個鍵（key）進行排序
from operator import itemgetter

# 建立一個包含兩個字典的列表（list of dictionaries）
# 每個字典代表一個人，包含名字（fname）和用戶ID（uid）
rows = [{"fname": "Brian", "uid": 1003}, {"fname": "John", "uid": 1001}]

# 印出原始資料
print("原始資料：")
print(rows)
print()

# 使用 sorted() 函數搭配 itemgetter 來排序
# itemgetter('fname') 表示「取得每個字典中的 'fname' 欄位值作為排序依據」
# sorted() 會根據這些值進行排序（預設為升序）
# 這裡會依照名字（fname）進行排序：Brian -> John（按照字母順序）
result1 = sorted(rows, key=itemgetter("fname"))
print("按照名字（fname）排序：")
print(result1)
print()

# itemgetter('uid') 表示「取得每個字典中的 'uid' 欄位值作為排序依據」
# 這裡會依照用戶ID（uid）進行排序：1001 -> 1003（數字升序）
result2 = sorted(rows, key=itemgetter("uid"))
print("按照用戶ID（uid）排序：")
print(result2)
print()

# itemgetter('uid', 'fname') 表示「先依照 'uid' 排序，若 'uid' 相同則依照 'fname' 排序」
# 這稱為「多鍵排序」（multi-key sorting）
# 範例中 uid 不同，所以會依照 uid: 1001 (John) -> 1003 (Brian)
result3 = sorted(rows, key=itemgetter("uid", "fname"))
print("先按照 uid，再按照 fname 排序（多鍵排序）：")
print(result3)
print()

# ========== 程式碼解說 ==========
#
# 1. itemgetter 的基本用法：
#    itemgetter('fname') 會建立一個函數，該函數接受一個字典，
#    並返回字典中 'fname' 鍵對應的值。
#    例如：itemgetter('fname')({'fname': 'Brian'}) 會返回 'Brian'
#
# 2. 為什麼要使用 itemgetter？
#    - 比 lambda 函數更快（itemgetter 是用 C 實現的）
#    - 語法更簡潔
#    - 支援多鍵排序
#
# 3. sorted() 函數：
#    - sorted(iterable, key=...) 回傳一個新的排序後的列表
#    - 參數 key 指定一個函數，用於從每個元素中提取比較鍵
#    - 預設是升序（小到大），若要降序可加上 reverse=True
#
# 4. 實際應用場景：
#    - 對資料庫查詢結果進行排序
#    - 對 CSV/Excel 資料進行排序
#    - 對 JSON 資料進行排序
#
# 5. 對比 lambda 的寫法：
#    sorted(rows, key=lambda x: x['fname'])  # 等同於 itemgetter('fname')
#    sorted(rows, key=lambda x: (x['uid'], x['fname']))  # 等同於 itemgetter('uid', 'fname')
