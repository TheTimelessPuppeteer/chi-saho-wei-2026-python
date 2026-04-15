# R07. 日期時間基本運算（3.12–3.13）
# timedelta 加減 / weekday() 計算指定星期

from datetime import datetime, timedelta

# ── 3.12 timedelta 基本運算 ───────────────────────────
# timedelta 用來表示時間差，支援天、秒、微秒、毫秒、分鐘、
# 小時、週等參數。也可以直接相加或相減。
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)  # 2，取整天數部分
print(c.total_seconds() / 3600)  # 58.5，將整個時間差轉成小時

# datetime 可以加上 timedelta 產生新的時間點
# 2012-09-23 加上 10 天會得到 2012-10-03

dt = datetime(2012, 9, 23)
print(dt + timedelta(days=10))  # 2012-10-03 00:00:00

# 兩個 datetime 相減會得到 timedelta
# 2012-12-21 減去 2012-09-23 得到 89 天差距

d1, d2 = datetime(2012, 9, 23), datetime(2012, 12, 21)
print((d2 - d1).days)  # 89

# 閏年的日期差會自動考慮 2 月 29 日
print((datetime(2012, 3, 1) - datetime(2012, 2, 28)).days)  # 2（閏年）
print((datetime(2013, 3, 1) - datetime(2013, 2, 28)).days)  # 1（平年）

# ── 3.13 計算指定星期日期 ─────────────────────────────
# weekday() 會回傳 0~6 的數字，分別對應 Monday~Sunday
# get_previous_byday() 會回傳 start 之前最近的指定星期幾
WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def get_previous_byday(dayname: str, start: datetime | None = None) -> datetime:
    if start is None:
        start = datetime.today()
    # start.weekday() 取得當前日期的星期數
    day_num = start.weekday()
    target = WEEKDAYS.index(dayname)

    # 如果今天就是 target，則回到上一週的同一天
    days_ago = (7 + day_num - target) % 7 or 7
    return start - timedelta(days=days_ago)


base = datetime(2012, 8, 28)  # 週二
print(get_previous_byday("Monday", base))  # 2012-08-27
print(get_previous_byday("Friday", base))  # 2012-08-24

# 如果沒有指定 start，會從今天開始向前搜尋
print(get_previous_byday("Sunday"))  # 會回傳今天之前最近的星期日
