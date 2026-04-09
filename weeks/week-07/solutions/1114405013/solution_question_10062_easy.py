"""Question 10062 的 easy 版本解答。

這一版刻意不用 Fenwick Tree 或 Segment Tree，
而是改用比較直觀、比較容易記憶的做法。

核心想法：
1. 題目給的是「第 i 個位置前面有幾個比它小的編號」。
2. 我們改成從後面往前還原答案。
3. 每次都從「目前還沒用過的編號」中，挑出對應位置的編號。

這樣寫的優點是邏輯好懂；缺點是 list 的刪除為 O(N)，
因此整體時間複雜度是 O(N^2)，比較適合教學與理解。
"""

import sys


def reconstruct_order(smaller_counts):
    """根據題目給的 smaller_counts 重建原始排列。

    參數說明：
    - smaller_counts[i] 代表「第 i+2 個位置」前面有多少個更小編號。
      因為第 1 個位置前面沒有任何牛，所以題目不會提供第一個位置的數值。

    例如：
    - N = 5
    - 題目輸入的 counts 長度會是 4
    - 我們手動在最前面補一個 0，代表第 1 個位置前面有 0 個更小編號
    """
    size = len(smaller_counts) + 1
    counts = [0] + list(smaller_counts)

    # answer 用來存放最後還原出的隊伍排列。
    answer = [0] * size

    # available 代表「目前還沒被放進答案中的編號」，而且永遠保持遞增。
    # 一開始所有編號 1..N 都可用。
    available = list(range(1, size + 1))

    # 從最後一個位置一路往前決定答案。
    #
    # 為什麼可以倒著做？
    # 因為當我們在決定第 index 個位置時，
    # index 後面的元素其實已經不重要了，
    # 我們只要知道「目前還剩哪些編號可以用」即可。
    #
    # counts[index] 的意思是：
    # 在這個位置前面，會有 counts[index] 個更小的編號。
    #
    # 由於 available 是遞增排序，
    # 所以直接取 available[counts[index]]，
    # 就等於取出「前面剛好有 counts[index] 個更小值」的那個編號。
    #
    # 取出後，這個編號就不能再用，因此使用 pop() 從 available 中刪掉。
    for index in range(size - 1, -1, -1):
        answer[index] = available.pop(counts[index])

    return answer


def solve():
    """讀取輸入、重建排列、輸出答案。"""

    # 使用 read().split() 可以一次吃完整份輸入，
    # 對這題的單組資料格式很方便。
    data = sys.stdin.read().strip().split()
    if not data:
        return

    # 第一個數字是 N，代表總共有幾頭牛。
    size = int(data[0])

    # 後面會有 N-1 個整數，分別對應第 2 個位置到第 N 個位置的資訊。
    smaller_counts = [int(value) for value in data[1 : 1 + size - 1]]

    # 呼叫核心函式重建答案。
    answer = reconstruct_order(smaller_counts)

    # 題目要求每個編號輸出一行。
    sys.stdout.write("\n".join(str(value) for value in answer))


if __name__ == "__main__":
    # 讓此檔案可以直接當作競賽程式執行。
    solve()
