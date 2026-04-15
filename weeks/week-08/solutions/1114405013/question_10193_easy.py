import sys


def main() -> None:
    """QUESTION-10193 easy 版（最直覺、最好背）。

    口訣：
    1) 算 n = a^2 + 1
    2) 枚舉 n 的所有正因數 d
    3) 每個 d 算候選值 2a + d + n/d
    4) 取最小值

    背後數學（簡化版）：
    - 題目可推成 (b-a)(c-a) = a^2 + 1。
    - 設 d = b-a，則 d 必為 n=a^2+1 的正因數。
    - 另一個因數 q = n/d，對應 c-a。
    - 所以 b+c = 2a + d + q。
    - 我們只要在所有因數配對中找最小值。

    為何只枚舉到 sqrt(n)：
    - 因數成對出現：若 d 是因數，q=n/d 也是因數。
    - 枚舉到 sqrt(n) 就會把每一對都考慮到，避免重複。
    """

    # 讀入單一整數 a，strip() 可避免前後空白干擾。
    text = sys.stdin.read().strip()
    if not text:
        # 無輸入時直接結束。
        return

    a = int(text)

    # n 對應題目推導中的 a^2+1。
    n = a * a + 1

    # best 記錄目前最小的 b+c。
    best = None

    # 直接從 1 到 sqrt(n) 枚舉因數，
    # 每找到一個 d，就能得到另一個因數 q = n // d。
    d = 1
    while d * d <= n:
        if n % d == 0:
            q = n // d

            # 由公式 b+c = 2a + d + q 計算候選答案。
            candidate = 2 * a + d + q

            # 取最小值。
            if best is None or candidate < best:
                best = candidate
        d += 1

    # 題目輸出是一個整數。
    print(best)


if __name__ == "__main__":
    main()
