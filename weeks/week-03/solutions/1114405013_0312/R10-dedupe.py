# R10. 去重且保序（1.10）
# 本範例展示兩個去重函數：
# 1. dedupe: 對基本類型（如數字、字串）進行去重，保留首次出現的順序
# 2. dedupe2: 更靈活的版本，支援 key 函數，可對複雜物件進行去重

def dedupe(items):
    # 簡單的去重函數，適用於可雜湊的對象（numbers, strings 等）
    # 使用 generator（yield）以節省記憶體，不必一次性載入所有資料
    seen = set()
    for item in items:
        # 如果此項目未見過，就輸出它，並記錄在 seen 中
        if item not in seen:
            yield item
            seen.add(item)

def dedupe2(items, key=None):
    # 進階版本，支援 key 參數以自定義比較邏輯
    # 適合對字典、物件的特定欄位進行去重
    seen = set()
    for item in items:
        # 如果指定 key，就用 key(item) 的結果進行去重；否則直接用 item
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

# ===== 示範使用 =====
if __name__ == '__main__':
    # 範例 1: 基本去重（數字）
    data = [1, 5, 2, 5, 3, 1, 4, 2]
    print("原始數據:", data)
    result = list(dedupe(data))
    print("dedupe 後（去除重複，保持順序）:", result)
    print()

    # 範例 2: 字串去重
    words = ['apple', 'banana', 'apple', 'cherry', 'banana']
    print("原始單字:", words)
    result = list(dedupe(words))
    print("dedupe 後（字串去重）:", result)
    print()

    # 範例 3: 複雜物件去重（字典列表，基於 id 欄位）
    users = [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'},
        {'id': 1, 'name': 'Alice'},  # 重複的 id
        {'id': 3, 'name': 'Charlie'},
    ]
    print("原始使用者列表:", users)
    # 使用 dedupe2，用 lambda 提取 'id' 欄位進行去重
    result = list(dedupe2(users, key=lambda x: x['id']))
    print("dedupe2 後（基於 id 去重）:", result)
    print()

    # 範例 4: 不區分大小寫的字串去重
    mixed_case = ['Apple', 'banana', 'APPLE', 'Banana', 'cherry']
    print("原始（混合大小寫）:", mixed_case)
    result = list(dedupe2(mixed_case, key=lambda x: x.lower()))
    print("dedupe2 後（不區分大小寫去重）:", result)

# 理解重點：
# 1. 去重同時保列元素出現的順序（不像 set 會丟失順序）
# 2. 使用 generator（yield）節省記憶體，適合大數據集
# 3. key 參數允許自定義去重的比較邏輯，靈活應對複雜場景
# 4. seen 是個 O(1) 查詢的集合，比 list.count() 高效得多
