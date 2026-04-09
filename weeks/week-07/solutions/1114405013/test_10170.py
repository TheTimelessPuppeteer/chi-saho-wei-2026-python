"""Question 10170 的單元測試。"""

import subprocess
import sys
import unittest
from pathlib import Path


TARGET_SCRIPT = Path(__file__).with_name("solution_question_10170.py")


class TestQuestion10170(unittest.TestCase):
    """測試 The Hotel with Infinite Rooms。"""

    def _days_sum(self, s, n):
        """計算從 s 到 n 的總天數（等差級數和）。"""
        count = n - s + 1
        return (s + n) * count // 2

    def _expected_group(self, s, d):
        """用二分搜尋計算第 d 天所屬的旅行團人數。"""
        # 找到一個足夠大的上界。
        lo = s
        hi = s
        while self._days_sum(s, hi) < d:
            hi *= 2

        # 二分搜尋最小 n，使 sum(s..n) >= d。
        while lo < hi:
            mid = (lo + hi) // 2
            if self._days_sum(s, mid) >= d:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def _run_solution(self, raw_input):
        """執行被測程式並回傳輸出行列表。"""
        if not TARGET_SCRIPT.exists():
            self.fail(
                "找不到被測程式："
                f"{TARGET_SCRIPT}。請先建立 solution_question_10170.py。"
            )

        completed = subprocess.run(
            [sys.executable, str(TARGET_SCRIPT)],
            input=raw_input,
            text=True,
            capture_output=True,
            check=False,
        )

        if completed.returncode != 0:
            self.fail(
                "被測程式執行失敗。\n"
                f"return code: {completed.returncode}\n"
                f"stderr:\n{completed.stderr}"
            )

        out = completed.stdout.strip()
        return out.splitlines() if out else []

    def assertCases(self, cases):
        """批次驗證多組 (S, D) 案例。"""
        raw_input = "\n".join(f"{s} {d}" for s, d in cases) + "\n"
        actual_lines = self._run_solution(raw_input)
        expected_lines = [str(self._expected_group(s, d)) for s, d in cases]
        self.assertEqual(actual_lines, expected_lines)

    def test_day_one_boundary(self):
        """測試第一天邊界。"""
        self.assertCases([(4, 1)])

    def test_end_of_first_group(self):
        """測試第一團最後一天。"""
        self.assertCases([(4, 4)])

    def test_next_group_first_day(self):
        """測試跨到下一團第一天。"""
        self.assertCases([(4, 5)])

    def test_multiple_input_lines(self):
        """測試多筆輸入（EOF 形式）。"""
        self.assertCases([(1, 1), (3, 6), (4, 9), (4, 10)])

    def test_large_values(self):
        """測試較大數值案例。"""
        self.assertCases([(10000, 10**12), (9999, 10**14 - 1)])


if __name__ == "__main__":
    unittest.main()
