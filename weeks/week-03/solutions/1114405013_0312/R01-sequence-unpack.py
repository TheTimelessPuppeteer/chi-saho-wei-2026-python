# R1. 序列解包（1.1）
# 這個檔案示範了如何把一個序列（tuple 或 list）中的元素一次性賦值給
# 多個變數，又稱為「序列解包」(sequence unpacking)。
# 這在 Python 中非常常見，用來清楚表達資料結構的內容。

p = (4, 5)  # p 是一個 tuple，包含兩個整數
# 右側的序列長度必須與左側變數數量相同，否則會拋出 ValueError。
x, y = p  # 把 p 的第一個元素 4 賦值給 x，第二個元素 5 賦值給 y
print("p unpacked:", x, y)  # 印出解包後的結果

# 接下來示範對 list 的解包：
data = ['ACME', 50, 91.1, (2012, 12, 21)]
# list 中有四個元素，因此左邊也要有四個變數
name, shares, price, date = data
# 這裡 name='ACME', shares=50, price=91.1, date=(2012,12,21)
print("full data unpacked:", name, shares, price, date)

# 可以在需要時再對嵌套的序列解包，像日期這種 3 元組：
name, shares, price, (year, mon, day) = data
# 這次把 date 拆成 year、mon、day 三個變數
print("nested unpack:", name, shares, price, year, mon, day)

# 如果你只對部分欄位有興趣，可以用“佔位變數”_忽略其它值：
# conventionally _ 用來表示「這個值不重要」
_, shares, price, _ = data
print("discarded some values, keep shares and price:", shares, price)

# 上面程式的重點：
# 1. 序列解包讓程式碼更簡潔，避免多次索引 (data[0]、data[1]...)
# 2. 變數數量必須和序列長度一致。
# 3. 可以搭配嵌套解包與丟棄變數實現更靈活的資料處理。
