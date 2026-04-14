# R2. 解包數量不固定：星號解包（1.2）
# 在前一個範例中，序列的長度必須和變數數量完全符合。
# 如果資料數量不確定，可以使用「*」搭配星號變數，
# 將多餘的部分收集為 list。


def drop_first_last(grades):
    # grades 可以是任意長度的序列
    # 用法：把第一個元素賦給 first，把最後一個元素賦給 last，
    # 中間的所有項目都放到 middle 這個 list
    first, *middle, last = grades
    print("in drop_first_last, first=", first, "middle=", middle, "last=", last)
    # 然後忽略 first 和 last，只計算中間的平均
    return sum(middle) / len(middle)

# 範例 record，其中電話數量不固定
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
# 名字和 email 放進固定變數，剩下的全部封裝成 phone_numbers 列表
name, email, *phone_numbers = record
print("name=", name, "email=", email, "phones=", phone_numbers)

# 可以把星號變數放在序列的任何位置
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print("trailing=", trailing, "current=", current)

# 以下展示不同的呼叫方式：
print("drop_first_last on [1,2,3,4] ->", drop_first_last([1,2,3,4]))
print("drop_first_last on [10,20,30,40,50] ->", drop_first_last([10,20,30,40,50]))

# 解說要點：
# 1. 星號變數（*var）會接收「多於左側變數的數量」的元素，
#    結果一定是 list，甚至可能是空 list。
# 2. 如果序列的總長度太短（不能滿足至少一個前後元素），
#    解包時仍會 ValueError。
# 3. 星號變數可以放在開頭、中間或結尾，但只能使用一次。
# 4. 這個技巧常見於函數參數處理、不定長資料結構等情境。
