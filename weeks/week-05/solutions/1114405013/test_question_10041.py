import sys
import unittest
from io import StringIO

from solution_question_10041 import min_total_distance, solve


class TestQuestion10041(unittest.TestCase):
    # 以暴力法計算最小總距離（僅用於小型測資交叉驗證）
    def _brute_force_min_distance(self, addresses):
        left = min(addresses)
        right = max(addresses)
        return min(
            sum(abs(house - x) for x in addresses) for house in range(left, right + 1)
        )

    # 驗證奇數個地址時，中位數位置可得到最小總距離
    def test_min_total_distance_odd_count(self):
        self.assertEqual(min_total_distance([2, 4, 6]), 4)

    # 驗證偶數個地址時，落在中間區間都可得到相同最小總距離
    def test_min_total_distance_even_count(self):
        self.assertEqual(min_total_distance([1, 2, 3, 4]), 4)

    # 驗證未排序輸入與重複門牌也能正確處理
    def test_min_total_distance_unsorted_and_duplicates(self):
        self.assertEqual(min_total_distance([10, 2, 2, 2, 20]), 26)

    # 驗證只有一位親戚時，總距離應為 0
    def test_min_total_distance_single_relative(self):
        self.assertEqual(min_total_distance([5]), 0)

    # 使用暴力法對多組小型資料做交叉比對，避免只靠固定範例
    def test_min_total_distance_matches_bruteforce(self):
        cases = [
            [1, 1, 10],
            [7, 3, 9, 15],
            [2, 8, 8, 9, 20],
            [30, 10, 20, 40, 50, 60],
        ]

        for addresses in cases:
            with self.subTest(addresses=addresses):
                expected = self._brute_force_min_distance(addresses)
                self.assertEqual(min_total_distance(addresses), expected)

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

    # 驗證題目格式的多組輸入輸出
    def test_solve_multiple_cases(self):
        input_data = """3
2 2 4
3 2 4 6
4 1 2 3 4
"""

        expected_output = """2
4
4"""

        self.assertEqual(self._run_solve(input_data), expected_output)


if __name__ == "__main__":
    # 直接執行此檔案時，啟動所有單元測試
    unittest.main()
