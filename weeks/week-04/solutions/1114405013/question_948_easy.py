import sys


def check_one_guess(weighings, fake_coin, is_heavier):
    """檢查單一假設是否與所有秤重結果一致。

    參數說明：
    - weighings: 所有秤重資料，每筆為 (left, right, result)
      - left/right: 該次秤重左右盤硬幣編號清單
      - result: '<'、'>'、'=' 之一
    - fake_coin: 目前假設哪一顆是假幣
    - is_heavier: True 表示假設這顆較重；False 表示較輕

    回傳：
    - True: 此假設可解釋全部秤重
    - False: 至少有一筆秤重與假設衝突
    """
    for left, right, result in weighings:
        # balance 代表「左盤重量 - 右盤重量」的相對值。
        # 我們只關心比較結果，不需要真實重量，因此用 +1/-1 模擬即可。
        balance = 0

        # 若假幣在左盤：
        # - 偏重 -> 左盤相對更重，balance +1
        # - 偏輕 -> 左盤相對更輕，balance -1
        if fake_coin in left:
            balance += 1 if is_heavier else -1

        # 若假幣在右盤（注意是左減右）：
        # - 偏重 -> 右盤更重，等價於左盤更輕，balance -1
        # - 偏輕 -> 右盤更輕，等價於左盤更重，balance +1
        if fake_coin in right:
            balance += -1 if is_heavier else 1

        # 將模擬結果與題目符號比對：
        # '=': 兩邊應相等，所以 balance 必須是 0
        # '<': 左盤較輕，所以 balance 必須 < 0
        # '>': 左盤較重，所以 balance 必須 > 0
        # 任一筆不符合就可以直接排除此假設（提早結束）。
        if result == "=" and balance != 0:
            return False
        if result == "<" and balance >= 0:
            return False
        if result == ">" and balance <= 0:
            return False

    return True


def solve(tokens):
    """依題目輸入 token 計算每組測資答案。

    核心想法（好記版）：
    1) 每顆硬幣都當作候選假幣
    2) 每顆各試兩種狀態（偏重/偏輕）
    3) 只要其中一種狀態能通過全部秤重，就保留為候選
    4) 最後若候選只有 1 顆，輸出該編號；否則輸出 0

    時間複雜度：約 O(N * K * P)
    - N: 硬幣數
    - K: 秤重次數
    - P: 每次秤重盤上硬幣數（用 `in list` 判斷帶來的成本）
    在題目限制 N, K <= 100 下可輕鬆通過。
    """
    i = 0
    m = int(tokens[i])
    i += 1
    answers = []

    # 逐組處理測資
    for _ in range(m):
        n = int(tokens[i])
        i += 1
        k = int(tokens[i])
        i += 1

        weighings = []
        # 讀入 k 次秤重資料
        for _ in range(k):
            p = int(tokens[i])
            i += 1

            # 前 p 個是左盤，後 p 個是右盤
            left = [int(tokens[i + j]) for j in range(p)]
            i += p
            right = [int(tokens[i + j]) for j in range(p)]
            i += p

            # 每次秤重結論：'<', '>', '='
            result = tokens[i]
            i += 1
            weighings.append((left, right, result))

        # 「好記版」核心：每顆硬幣都試兩次（偏重/偏輕）。
        candidates = []
        for coin in range(1, n + 1):
            # 只要偏重或偏輕其中一種能成立，就先列為可能答案。
            if check_one_guess(weighings, coin, True) or check_one_guess(
                weighings, coin, False
            ):
                candidates.append(coin)

        # 只有唯一候選才能確定答案，否則輸出 0。
        answers.append(str(candidates[0]) if len(candidates) == 1 else "0")

    # 題目要求測資與測資之間保留一個空白列。
    return "\n\n".join(answers)


def main():
    # 用 split() 解析全部 token，可自動跳過空白與空白列，
    # 很適合這題「測資之間可能穿插空行」的輸入格式。
    tokens = sys.stdin.read().split()
    if not tokens:
        # 若沒有任何輸入，直接結束避免轉型錯誤。
        return

    # solve() 已處理好多組輸出的空白列格式，這裡直接印出即可。
    print(solve(tokens))


if __name__ == "__main__":
    main()
