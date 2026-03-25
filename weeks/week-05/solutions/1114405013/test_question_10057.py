import sys
import unittest
from io import StringIO

from solution_question_10057 import analyze_numbers, solve


class TestQuestion10057(unittest.TestCase):
    # 以暴力法枚舉所有 A，作為小型測資的正確性基準
    def _naive_analyze(self, values):
        min_value = min(values)
        max_value = max(values)

        best_cost = None
        best_as = []
        for candidate in range(min_value, max_value + 1):
            cost = sum(abs(number - candidate) for number in values)
            if best_cost is None or cost < best_cost:
                best_cost = cost
                best_as = [candidate]
            elif cost == best_cost:
                best_as.append(candidate)

        smallest_a = best_as[0]
        count = sum(1 for number in values if number in best_as)
        ways = len(best_as)
        return (smallest_a, count, ways)

    # 封裝 solve() 的 stdin/stdout，方便比對整段輸出
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

    # 奇數筆資料：中位數唯一，ways 應為 1
    def test_basic_odd_count(self):
        self.assertEqual(analyze_numbers([1, 2, 3]), (2, 1, 1))

    # 偶數筆資料：中位區間有兩個可行 A
    def test_even_count_multiple_medians(self):
        self.assertEqual(analyze_numbers([1, 2, 3, 4]), (2, 2, 2))

    # 全部數值相同：A 唯一，且 count 為資料筆數
    def test_all_same_values(self):
        self.assertEqual(analyze_numbers([5, 5, 5, 5, 5]), (5, 5, 1))

    # 大值範圍：驗證 ways 計算不受值域影響
    def test_large_value_range(self):
        self.assertEqual(analyze_numbers([1, 65535]), (1, 2, 65535))

    # 使用小型案例與暴力法交叉驗證 (a, count, ways)
    def test_matches_naive_on_small_cases(self):
        cases = [
            [1, 2, 2, 3],
            [10, 20, 30, 40],
            [1, 1, 2, 2],
            [1, 2, 3, 3, 3],
            [7, 8, 9],
        ]

        for values in cases:
            with self.subTest(values=values):
                self.assertEqual(analyze_numbers(values), self._naive_analyze(values))

    # 驗證 solve() 可正確處理多組輸入輸出
    def test_solve_multiple_cases(self):
        input_data = """1
10
4
1
2
3
4
4
1
1
2
2
5
5
5
5
5
5
2
1
65535
"""

        expected_output = """10 1 1
2 2 2
1 4 2
5 5 1
1 2 65535"""

        self.assertEqual(self._run_solve(input_data), expected_output)


if __name__ == "__main__":
    # 直接執行此檔案時，啟動所有單元測試
    unittest.main()
