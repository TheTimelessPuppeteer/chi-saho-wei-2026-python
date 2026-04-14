# R7. OrderedDict（1.7）
# OrderedDict 是一個保持鍵插入順序的字典。
# 與一般 dict 不同，它記錄鍵的加入順序，並提供額外方法來操作順序。
# 在 Python 3.7+ 後，一般 dict 也會保持順序，但 OrderedDict 仍有其用途。

from collections import OrderedDict
import json

# 建立 OrderedDict 並加入鍵值
d = OrderedDict()
d['foo'] = 1; d['bar'] = 2
print("OrderedDict 內容:", d)
print("鍵的順序:", list(d.keys()))

# OrderedDict 在 JSON 序列化時會保持順序
json_str = json.dumps(d)
print("JSON 輸出:", json_str)

# 示範額外方法：move_to_end
d['baz'] = 3
print("加入 'baz' 後:", d)
d.move_to_end('foo')  # 將 'foo' 移到最後
print("move_to_end('foo') 後:", d)

# popitem(last=True) 預設移除最後一個，last=False 移除第一個
last_item = d.popitem(last=True)
print("popitem(last=True) 移除:", last_item, "剩下:", d)

# 理解重點：
# - OrderedDict 記錄插入順序，即使鍵值相同。
# - 適用於需要穩定順序的場景，如設定檔案、API 回應。
# - 在 Python 3.7+，一般 dict 也保持順序，但 OrderedDict 有更多順序操作方法。
# - JSON 序列化時，OrderedDict 確保鍵的順序與插入時一致。
