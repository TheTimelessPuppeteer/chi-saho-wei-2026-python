# R09. 時區操作（3.16）
# zoneinfo（Python 3.9+）取代 pytz，提供標準時區資料與轉換

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo, available_timezones

# 先建立常用時區物件，並用 tz-aware datetime 表示時間
utc = ZoneInfo("UTC")
central = ZoneInfo("America/Chicago")
taipei = ZoneInfo("Asia/Taipei")

# 建立帶時區的 datetime，這裡使用美國芝加哥時間
# tzinfo 參數讓 datetime 變成有時區資訊的物件
# 輸出格式會包含時區偏移 -06:00

d = datetime(2012, 12, 21, 9, 30, 0, tzinfo=central)
print(d)  # 2012-12-21 09:30:00-06:00

# 對 tz-aware datetime 使用 astimezone() 進行時區轉換
print(d.astimezone(ZoneInfo("Asia/Kolkata")))  # 2012-12-21 21:00:00+05:30
print(d.astimezone(taipei))  # 2012-12-21 23:30:00+08:00

# 取得當前 UTC 時間，直接傳入 tz 參數
now_utc = datetime.now(tz=utc)
print(now_utc)

# 最佳實踐：內部用 UTC 儲存時間，顯示時再轉成本地時區
# 這樣可避免跨時區計算錯誤
utc_dt = datetime(2013, 3, 10, 7, 45, 0, tzinfo=utc)
print(utc_dt.astimezone(central))  # 2013-03-10 01:45:00-06:00

# available_timezones() 回傳系統內可用的時區名稱
# 可以用關鍵字過濾特定國家或城市的時區

tw_zones = [z for z in available_timezones() if "Taipei" in z]
print(tw_zones)  # ['Asia/Taipei']
