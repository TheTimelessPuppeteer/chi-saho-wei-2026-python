# U07. 隨機種子與安全亂數（3.11）
# 本範例示範隨機數生成的兩個重要概念：
# 1. random 模組產生偽隨機數，可重現但不安全
# 2. secrets 模組提供密碼學安全的亂數，不可預測

import random
import secrets

# 相同種子 → 相同序列（可重現）
# random 模組使用梅森旋轉演算法產生偽隨機數
# 設定種子後，每次執行會產生相同的序列，這對於測試和重現很有用
random.seed(42)
seq1 = [random.randint(1, 100) for _ in range(5)]  # 產生 5 個 1-100 的隨機整數
random.seed(42)  # 重設相同種子
seq2 = [random.randint(1, 100) for _ in range(5)]  # 產生相同的序列
print(seq1 == seq2)  # True，因為種子相同，序列重現

# 不同 Random 實例各自獨立
# 可以建立多個獨立的隨機數生成器，每個有自己的狀態
rng1 = random.Random(1)  # 種子為 1
rng2 = random.Random(2)  # 種子為 2
print(rng1.random(), rng2.random())  # 各自產生不同的隨機浮點數

# 密碼學安全亂數（不可預測，不能設種子）
# secrets 模組使用作業系統的密碼學安全的隨機源（如 /dev/urandom）
# 這些亂數不可預測，適合用於安全應用
print(secrets.randbelow(100))  # 產生 0 到 99 之間的密碼學安全隨機整數
print(secrets.token_hex(16))  # 產生 16 位元組的隨機十六進位字串（32 個字元）
print(secrets.token_bytes(16))  # 產生 16 位元組的隨機 bytes

# 重要：random 模組不適合密碼、token、session key 等安全場景
# random 模組的輸出可預測（如果知道種子），不適合：
# - 密碼生成
# - 安全 token
# - session key
# - 密碼學應用
# 只適合遊戲、模擬、測試等非安全用途
# 對於安全需求，一律使用 secrets 模組
