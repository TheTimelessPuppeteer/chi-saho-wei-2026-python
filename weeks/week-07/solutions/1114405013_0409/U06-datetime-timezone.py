# U06. 時區操作最佳實踐：UTC 優先（3.16）
# 本範例示範時區處理的最佳實踐：內部計算一律使用 UTC，避免夏令時跳躍問題。
# 為什麼用 UTC？本地時間有夏令時（DST）調整，會造成時間跳躍或重複，導致計算錯誤。

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# 定義時區物件
utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago")  # 芝加哥時區，有夏令時

# 問題：直接在本地時間加減，夏令時邊界會出錯
# 美國 2013-03-10 凌晨 2:00 時鐘往前撥一小時（夏令時開始）
# 這意味著 2:00 到 3:00 的時間不存在
local_dt = datetime(2013, 3, 10, 1, 45, tzinfo=central)
wrong = local_dt + timedelta(minutes=30)
print(f"錯誤結果：{wrong}")  # 2:15（不存在的時間！時鐘會直接跳到 3:00）

# 正確做法：先轉 UTC 計算，再轉回本地
# 將本地時間轉為 UTC，進行計算，然後轉回本地顯示
utc_dt = local_dt.astimezone(utc)
correct = utc_dt + timedelta(minutes=30)
print(f"正確結果：{correct.astimezone(central)}")  # 3:15（正確跳過不存在的 2:xx 時段）

# 最佳實踐：輸入→UTC→計算→輸出時轉本地
# 1. 用戶輸入通常是本地時間（naive datetime）
user_input = "2012-12-21 09:30:00"
naive = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")  # 解析成 naive datetime

# 2. 假設輸入是特定時區，附加時區資訊並轉為 UTC 儲存
aware = naive.replace(tzinfo=central).astimezone(utc)
print(f"存 UTC：{aware}")  # 內部儲存 UTC 時間

# 3. 顯示時轉為目標時區（如台北時間）
print(f"顯示台北：{aware.astimezone(ZoneInfo('Asia/Taipei'))}")
# 這種做法確保所有計算都在 UTC 下進行，避免時區問題。
