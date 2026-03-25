import math
import sys
import unittest
from io import StringIO

from solution_question_10056 import solve, win_probability


class TestQuestion10056(unittest.TestCase):
    # 以數學閉式解當作基準，方便交叉驗證函式正確性
    def _closed_form(self, n, p, i):
        if p == 0:
            return 0.0

        q = 1.0 - p
        denominator = 1.0 - (q**n)
        numerator = (q ** (i - 1)) * p
        return numerator / denominator

    # 基本案例：兩位玩家、成功率 0.5，第一位玩家獲勝機率應為 2/3
    def test_win_probability_basic_player_one(self):
        self.assertAlmostEqual(win_probability(2, 0.5, 1), 2.0 / 3.0, places=7)

    # 基本案例：兩位玩家、成功率 0.5，第二位玩家獲勝機率應為 1/3
    def test_win_probability_basic_player_two(self):
        self.assertAlmostEqual(win_probability(2, 0.5, 2), 1.0 / 3.0, places=7)

    # p=0 時永遠沒有人能成功，任一玩家勝率都為 0
    def test_win_probability_zero_probability(self):
        self.assertEqual(win_probability(5, 0.0, 1), 0.0)
        self.assertEqual(win_probability(5, 0.0, 4), 0.0)

    # p=1 時第一位玩家必勝，其餘玩家不可能贏
    def test_win_probability_full_probability(self):
        self.assertEqual(win_probability(4, 1.0, 1), 1.0)
        self.assertEqual(win_probability(4, 1.0, 2), 0.0)
        self.assertEqual(win_probability(4, 1.0, 4), 0.0)

    # 多組資料與閉式解交叉驗證，避免只測單一範例
    def test_win_probability_matches_closed_form(self):
        cases = [
            (3, 0.2, 1),
            (3, 0.2, 2),
            (3, 0.2, 3),
            (6, 0.35, 4),
            (10, 0.01, 7),
        ]

        for n, p, i in cases:
            with self.subTest(n=n, p=p, i=i):
                expected = self._closed_form(n, p, i)
                self.assertTrue(
                    math.isclose(
                        win_probability(n, p, i), expected, rel_tol=1e-9, abs_tol=1e-12
                    )
                )

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

    # 驗證 solve() 的多組輸入輸出與四位小數格式
    def test_solve_multiple_cases_and_format(self):
        input_data = """6
2 0.5 1
2 0.5 2
3 0.2 1
3 0.2 2
3 0 2
4 1 1
"""

        expected_output = """0.6667
0.3333
0.4098
0.3279
0.0000
1.0000"""

        self.assertEqual(self._run_solve(input_data), expected_output)


if __name__ == "__main__":
    # 直接執行此檔案時，啟動所有單元測試
    unittest.main()
