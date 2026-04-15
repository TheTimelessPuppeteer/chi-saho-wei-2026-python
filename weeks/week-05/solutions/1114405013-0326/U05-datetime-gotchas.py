# U05. 日期時間的陷阱（3.12–3.15）
# 本範例示範日期時間處理中的兩個常見陷阱：
# 1. timedelta 不支援月份參數
# 2. strptime 的效能問題

import timeit
import calendar
from datetime import datetime, timedelta

# ── timedelta 不支援月份（3.12）──────────────────────
dt = datetime(2012, 9, 23)
# timedelta 只支援 days, seconds, microseconds, milliseconds, minutes, hours, weeks
# 不支援 months 或 years，因為月份天數不固定。
try:
    dt + timedelta(months=1)  # type: ignore[call-arg]
except TypeError as e:
    print(f"TypeError: {e}")  # 'months' is an invalid keyword argument

# 正確做法：手動處理月份加減，並考慮月份天數差異。
def add_one_month(dt: datetime) -> datetime:
    # 計算目標年月
    year = dt.year
    month = dt.month + 1
    if month == 13:  # 超過12月時進位到下一年
        year += 1
        month = 1

    # 使用 calendar.monthrange 取得目標月份的天數
    # monthrange 返回 (weekday_of_1st, days_in_month)
    _, days_in_target_month = calendar.monthrange(year, month)
    # 將日期限制在目標月份的有效範圍內，避免如1月31日加月後變成2月31日
    day = min(dt.day, days_in_target_month)

    # 使用 replace 建立新 datetime 物件
    return dt.replace(year=year, month=month, day=day)

print(add_one_month(datetime(2012, 1, 31)))  # 2012-02-29（2012年是閏年，2月29日）
print(add_one_month(datetime(2012, 9, 23)))  # 2012-10-23

# ── strptime 效能問題（3.15）─────────────────────────
# 建立測試資料：2012年各月1-28日的日期字串
dates = [f"2012-{m:02d}-{d:02d}" for m in range(1, 13) for d in range(1, 29)]

def use_strptime(s: str) -> datetime:
    # 使用 datetime.strptime 解析字串，靈活但較慢
    return datetime.strptime(s, "%Y-%m-%d")

def use_manual(s: str) -> datetime:
    # 手動分割字串並轉換，快速但格式固定
    y, m, d = s.split("-")
    return datetime(int(y), int(m), int(d))

# 驗證兩種方法結果相同
assert use_strptime("2012-09-20") == use_manual("2012-09-20")

# 效能測試：對所有日期執行解析
t1 = timeit.timeit(lambda: [use_strptime(d) for d in dates], number=100)
t2 = timeit.timeit(lambda: [use_manual(d) for d in dates], number=100)
print(f"strptime: {t1:.3f}s  手動解析: {t2:.3f}s（快 {t1 / t2:.1f} 倍）")
# 手動解析通常快得多，因為避免了正則式匹配和格式驗證的開銷。
