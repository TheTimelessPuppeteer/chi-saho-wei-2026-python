# R14. 物件排序 attrgetter（1.14）
# 此範例展示如何使用 operator 模組中的 attrgetter 函數
# 來對物件列表進行排序（按照物件的屬性）

# 從 operator 模組匯入 attrgetter
# attrgetter 是一個用於取得物件屬性的函數工廠
# 與 itemgetter 類似，但 itemgetter 用於字典（取鍵值）
# 而 attrgetter 用於物件（取屬性）
from operator import attrgetter


# 定義一個簡單的 User 類別
# 類別是物件的藍圖，可以用來建立多個具有相同結構的物件
class User:
    # __init__ 是建構函數，建立新物件時會自動呼叫
    # self 代表物件本身，user_id 是傳入的參數
    def __init__(self, user_id):
        # 將傳入的 user_id 儲存為物件的屬性
        # self.user_id 表示「這個物件的 user_id 屬性」
        self.user_id = user_id


# 建立一個包含三個 User 物件的列表
# 每個 User 物件有不同的 user_id：23, 3, 99
users = [User(23), User(3), User(99)]

# 印出原始資料
print("=" * 50)
print("原始資料：")
print("=" * 50)
for user in users:
    print(f"  User 物件的 user_id = {user.user_id}")
print()

# 使用 sorted() 搭配 attrgetter 來排序
# attrgetter('user_id') 表示「取得每個物件的 user_id 屬性作為排序依據」
# sorted() 會根據這些屬性值進行排序（預設為升序）
# 這裡會依照 user_id 進行排序：3 -> 23 -> 99
result = sorted(users, key=attrgetter("user_id"))

# 印出排序後的結果
print("=" * 50)
print("按照 user_id 排序後：")
print("=" * 50)
for user in result:
    print(f"  User 物件的 user_id = {user.user_id}")
print()

# 如果要降序排序（從大到小），可以加上 reverse=True
result_desc = sorted(users, key=attrgetter("user_id"), reverse=True)
print("=" * 50)
print("按照 user_id 降序排序（reverse=True）：")
print("=" * 50)
for user in result_desc:
    print(f"  User 物件的 user_id = {user.user_id}")
print()

# ========== 程式碼解說 ==========
#
# 1. 類別（Class）與物件（Object）：
#    - 類別是建立物件的藍圖/模板
#    - 物件是類別的實例（instance）
#    - 例如：User 是類別，User(23) 是一個 User 物件
#
# 2. 屬性（Attribute）：
#    - 屬性是附加在物件上的變數
#    - 例如：user.user_id 是 user 物件的 user_id 屬性
#    - 可以用 物件.屬性名 來存取
#
# 3. attrgetter 的用途：
#    - attrgetter('user_id') 建立一個函數，該函數接受一個物件
#    - 並返回該物件的 user_id 屬性值
#    - 類似於：lambda obj: obj.user_id
#
# 4. 為什麼用 attrgetter 而不是 lambda？
#    - attrgetter 效能更好（用 C 實現）
#    - 語法更簡潔
#    - 支援多屬性排序：attrgetter('lastname', 'firstname')
#
# 5. 與 itemgetter 的比較：
#    - itemgetter：用於字典，取鍵值 -> itemgetter('name')({'name': 'John'}) => 'John'
#    - attrgetter：用於物件，取屬性 -> attrgetter('name')(obj) => obj.name
#
# 6. 實際應用場景：
#    - 對資料庫物件進行排序
#    - 對自訂類別的實例進行排序
#    - 對具有多個屬性的物件進行多鍵排序
#
# 7. 對比 lambda 的寫法：
#    sorted(users, key=lambda x: x.user_id)  # 等同於 attrgetter('user_id')
