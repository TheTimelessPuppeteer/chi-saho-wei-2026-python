import sys


def one_case(n: int, p: float, i: int) -> float:
    # 先處理特例：若單次成功機率 p=0，代表遊戲永遠不會結束，
    # 當然第 i 位玩家的勝率也就一定是 0。
    if p == 0.0:
        return 0.0

    # q 是「單次失敗機率」。
    # 因為成功或失敗二選一，所以 q = 1 - p。
    q = 1.0 - p

    # hit_in_round 表示：在某一輪中，第 i 位玩家剛好獲勝的機率。
    # 條件是：
    # 1) 前面 i-1 位玩家都失敗 -> q^(i-1)
    # 2) 第 i 位玩家成功       -> p
    # 兩者相乘得到 hit_in_round。
    hit_in_round = (q ** (i - 1)) * p

    # round_all_fail 表示「一整輪 N 位玩家全部失敗」的機率。
    # 每位都失敗機率是 q，N 人獨立嘗試，所以是 q^N。
    round_all_fail = q**n

    # 第 i 位玩家總勝率 =
    # 第一輪就中獎
    # + 先整輪失敗一次後，在下一輪中獎
    # + 先整輪失敗兩次後，在再下一輪中獎 + ...
    #
    # 公式：
    # hit_in_round * (1 + round_all_fail + round_all_fail^2 + ...)
    # 這是等比級數，總和為 hit_in_round / (1 - round_all_fail)。
    return hit_in_round / (1.0 - round_all_fail)


# 讀取整份輸入，每行代表一組或設定資訊。
lines = sys.stdin.read().strip().splitlines()

# 若沒有輸入資料，直接結束。
if not lines:
    sys.exit(0)

# 第一行是測資筆數 S。
s = int(lines[0])

# 用 out 收集每組答案，最後一次輸出。
out = []

# 從第 2 行開始，每行格式為：N p i
# N: 玩家總數、p: 單次成功機率、i: 目標玩家編號（1-based）
for k in range(1, s + 1):
    n_str, p_str, i_str = lines[k].split()
    n = int(n_str)
    p = float(p_str)
    i = int(i_str)

    # 計算本組答案，並格式化為小數點後四位。
    ans = one_case(n, p, i)
    out.append(f"{ans:.4f}")  # 題目要求固定四位小數

# 每組答案各佔一行輸出。
print("\n".join(out))
