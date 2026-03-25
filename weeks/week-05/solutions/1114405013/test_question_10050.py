import sys
import unittest
from io import StringIO

from solution_question_10050 import count_lost_days, solve


class TestQuestion10050(unittest.TestCase):
    # 以直觀模擬法當作基準答案，協助交叉驗證主要函式
    def _naive_count_lost_days(self, n, hartals):
        lost_days = set()

        for interval in hartals:
            day = interval
            while day <= n:
                # day % 7 == 6 代表星期五，== 0 代表星期六
                # 這兩天是休假日，不計入損失工作天
                if day % 7 not in (6, 0):
                    lost_days.add(day)
                day += interval

        return len(lost_days)

    # 題目敘述中的代表案例：N=14、h=[3,4,8]，答案應為 5
    def test_count_lost_days_sample_case(self):
        self.assertEqual(count_lost_days(14, [3, 4, 8]), 5)

    # 驗證星期五/星期六不算工作天（例如第 6 天為星期五）
    def test_count_lost_days_excludes_weekend(self):
        self.assertEqual(count_lost_days(7, [6]), 0)
        self.assertEqual(count_lost_days(14, [6]), 1)

    # 驗證多個政黨在同一天罷會時，只能計算一次損失
    def test_count_lost_days_no_double_count(self):
        self.assertEqual(count_lost_days(15, [3, 3, 5]), 6)

    # 用多組小型資料與基準模擬法比對，避免只測固定範例
    def test_count_lost_days_matches_naive(self):
        cases = [
            (14, [3, 4, 8]),
            (20, [2, 3]),
            (30, [4, 6, 9]),
            (21, [5, 11]),
        ]

        for n, hartals in cases:
            with self.subTest(n=n, hartals=hartals):
                expected = self._naive_count_lost_days(n, hartals)
                self.assertEqual(count_lost_days(n, hartals), expected)

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

    # 驗證 UVA 10050 常見多組輸入輸出格式
    def test_solve_multiple_cases(self):
        input_data = """2
14
3
3
4
8
100
4
12
15
25
40
"""

        expected_output = """5
15"""

        self.assertEqual(self._run_solve(input_data), expected_output)

    # 補一個週末排除的 I/O 案例，確認輸出為 0
    def test_solve_weekend_only_case(self):
        input_data = """1
7
1
6
"""

        expected_output = """0"""

        self.assertEqual(self._run_solve(input_data), expected_output)


if __name__ == "__main__":
    # 直接執行此檔案時，啟動所有單元測試
    unittest.main()
