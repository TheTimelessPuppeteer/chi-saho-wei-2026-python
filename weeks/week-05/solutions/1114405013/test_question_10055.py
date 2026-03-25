import sys
import unittest
from io import StringIO

from solution_question_10055 import process_queries, solve


class TestQuestion10055(unittest.TestCase):
    # 直觀模擬法：用 0/1 表示每個函數目前是增(0)或減(1)
    def _naive_process_queries(self, n, queries):
        states = [0] * (n + 1)
        outputs = []

        for query in queries:
            op = query[0]
            if op == 1:
                # 反轉指定位置：0 <-> 1
                idx = query[1]
                states[idx] ^= 1
            else:
                # 區間內減函數個數為奇數 -> 複合結果為減函數(1)
                _, left, right = query
                parity = sum(states[left : right + 1]) % 2
                outputs.append(parity)

        return outputs

    # 一開始全部是增函數，任何區間查詢都應輸出 0
    def test_all_increasing_queries(self):
        n = 5
        queries = [(2, 1, 5), (2, 2, 4), (2, 3, 3)]
        self.assertEqual(process_queries(n, queries), [0, 0, 0])

    # 單點反轉後，含該點的區間會受奇偶影響
    def test_single_flip_effect(self):
        n = 5
        queries = [(1, 3), (2, 1, 5), (2, 3, 3), (2, 1, 2)]
        self.assertEqual(process_queries(n, queries), [1, 1, 0])

    # 同一個位置反轉兩次應回復原狀
    def test_double_flip_same_index(self):
        n = 4
        queries = [(1, 2), (1, 2), (2, 1, 4), (2, 2, 2)]
        self.assertEqual(process_queries(n, queries), [0, 0])

    # 驗證區間內減函數數量奇偶變化對輸出的影響
    def test_range_parity_odd_even(self):
        n = 6
        queries = [
            (1, 2),
            (1, 4),
            (2, 1, 6),
            (1, 5),
            (2, 1, 6),
            (2, 2, 5),
            (1, 4),
            (2, 2, 5),
        ]
        self.assertEqual(process_queries(n, queries), [0, 1, 1, 0])

    # 用多組小型資料和直觀模擬法交叉驗證，避免只測固定案例
    def test_process_queries_matches_naive(self):
        cases = [
            (5, [(2, 1, 5), (1, 2), (2, 1, 5)]),
            (4, [(1, 1), (1, 4), (2, 1, 4), (2, 2, 3)]),
            (6, [(1, 3), (2, 3, 3), (1, 3), (2, 1, 6), (1, 6), (2, 4, 6)]),
            (7, [(1, 2), (1, 5), (2, 2, 5), (1, 2), (2, 1, 7)]),
        ]

        for n, queries in cases:
            with self.subTest(n=n, queries=queries):
                expected = self._naive_process_queries(n, queries)
                self.assertEqual(process_queries(n, queries), expected)

    # 封裝 solve() 的 stdin/stdout 測試流程
    def _run_solve(self, input_data):
        old_stdin = sys.stdin
        old_stdout = sys.stdout

        try:
            sys.stdin = StringIO(input_data)
            buffer = StringIO()
            sys.stdout = buffer
            solve()
            return buffer.getvalue().strip()
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout

    # 驗證操作交錯時的輸入輸出格式與結果
    def test_solve_mixed_operations_io(self):
        input_data = """5 7
2 1 5
1 3
2 1 5
1 1
2 1 3
1 3
2 2 5
"""

        expected_output = """0
1
0
0"""

        self.assertEqual(self._run_solve(input_data), expected_output)


if __name__ == "__main__":
    # 直接執行此檔案時，啟動所有單元測試
    unittest.main()
