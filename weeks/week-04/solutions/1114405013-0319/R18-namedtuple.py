# R18. namedtuple（1.18）

# 匯入 namedtuple 類別
from collections import namedtuple

# 範例1: 建立訂閱者 namedtuple
# namedtuple('Subscriber', ['addr', 'joined']) 定義一個類似類別的結構
# 第一個參數是類型名稱，第二個是欄位名稱列表
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])

# 建立 Subscriber 實例，類似於建立物件
sub = Subscriber('jonesy@example.com', '2012-10-19')
print("訂閱者資訊:")
print(f"  地址: {sub.addr}")  # 存取 addr 屬性
print(f"  加入日期: {sub.joined}")  # 存取 joined 屬性
print(f"  完整資訊: {sub}")  # 印出整個 namedtuple

# 範例2: 建立股票 namedtuple
# 定義股票的欄位：名稱、股數、價格
Stock = namedtuple('Stock', ['name', 'shares', 'price'])

# 建立股票實例
s = Stock('ACME', 100, 123.45)
print(f"\n原始股票: {s}")
print(f"  名稱: {s.name}, 股數: {s.shares}, 價格: {s.price}")

# 使用 _replace() 方法建立修改後的新實例（不改變原實例）
# _replace() 回傳新實例，原始實例保持不變
s = s._replace(shares=75)
print(f"修改股數後: {s}")
print(f"  名稱: {s.name}, 股數: {s.shares}, 價格: {s.price}")

# namedtuple 的其他特性
print(f"\n--- namedtuple 特性 ---")
print(f"欄位名稱: {s._fields}")  # 顯示所有欄位名稱
print(f"欄位數量: {len(s._fields)}")
print(f"轉成字典: {s._asdict()}")  # 轉成 OrderedDict
print(f"轉成列表: {s}")  # namedtuple 本身就是 tuple

# 比較 namedtuple 與普通 tuple
print(f"\n--- 與普通 tuple 比較 ---")
normal_tuple = ('ACME', 100, 123.45)
print(f"普通 tuple: {normal_tuple}")
print(f"namedtuple: {s}")
print(f"存取 tuple[0]: {normal_tuple[0]}")  # 需要記住索引
print(f"存取 s.name: {s.name}")  # 直接用名稱存取

# namedtuple 的應用場景
print(f"\n--- 應用場景 ---")
print("1. 讓程式碼更易讀（不用記索引）")
print("2. 類似輕量級的類別，但不可變")
print("3. 適合儲存簡單的資料結構")
print("4. 可以用 _replace() 建立變體")

