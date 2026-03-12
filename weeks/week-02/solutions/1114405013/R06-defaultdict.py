# R6. 多值字典 defaultdict / setdefault（1.6）
# 當字典的值需要是可追加的物件（list、set等），通常要先檢查 key 是否存在。
# defaultdict 與 setdefault 可以省掉重複的檢查程式碼。

from collections import defaultdict

# 用 list 當 default factory，第一次存取時會自動建立列表
d = defaultdict(list)
d['a'].append(1); d['a'].append(2)
print("使用 defaultdict(list) ->", d)

# 用 set 當 default factory，適合要避免重複元素的情況
d = defaultdict(set)
d['a'].add(1); d['a'].add(2)
print("使用 defaultdict(set) ->", d)

# 等價的純 dict 作法，利用 setdefault
d = {}
d.setdefault('a', []).append(1)
print("使用 setdefault ->", d)

# 細節說明：
# - defaultdict(f) 在存取不存在的 key 時，自動呼叫 f() 產生預設值。
# - setdefault(key, default) 只會在 key 不存在時把 default 放進字典，
#   然後回傳對應值，常見於原生 dict。
# - 上例中，list 與 set 分別呈現可重複與唯一性特性。
# - defaultdict 也可以用於 int, dict 等，常用於計數或巢狀結構。

