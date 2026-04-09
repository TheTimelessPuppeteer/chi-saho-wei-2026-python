"""Question 10093 的單元測試。"""

import subprocess
import sys
import unittest
from pathlib import Path


TARGET_SCRIPT = Path(__file__).with_name("solution_question_10093.py")


class TestQuestion10093(unittest.TestCase):
    """測試炮兵最大部署數問題。"""

    def _build_input(self, grid):
        """將地圖資料組成題目輸入格式。"""
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0
        lines = [f"{rows} {cols}"]
        lines.extend(grid)
        return "\n".join(lines) + "\n"

    def _can_attack(self, r1, c1, r2, c2):
        """判斷兩支炮兵是否互相攻擊。"""
        # 同一列，橫向距離 2 以內會互相攻擊。
        if r1 == r2 and abs(c1 - c2) <= 2:
            return True

        # 同一行，縱向距離 2 以內會互相攻擊。
        if c1 == c2 and abs(r1 - r2) <= 2:
            return True

        return False

    def _is_valid_subset(self, cells):
        """檢查一組炮兵部署是否有效。"""
        for i in range(len(cells)):
            for j in range(i + 1, len(cells)):
                if self._can_attack(*cells[i], *cells[j]):
                    return False
        return True

    def _bruteforce_max(self, grid):
        """用暴力法求小地圖的最大可部署數。

        這個 helper 只用在小尺寸測資，作為正確答案來源。
        """
        plain_cells = []
        for r, row in enumerate(grid):
            for c, ch in enumerate(row):
                if ch == "P":
                    plain_cells.append((r, c))

        best = 0
        total = len(plain_cells)
        for mask in range(1 << total):
            selected = []
            for i in range(total):
                if mask & (1 << i):
                    selected.append(plain_cells[i])

            if len(selected) <= best:
                continue

            if self._is_valid_subset(selected):
                best = len(selected)

        return best

    def _run_solution(self, input_data):
        """執行被測程式並回傳標準輸出。"""
        if not TARGET_SCRIPT.exists():
            self.fail(
                "找不到被測程式："
                f"{TARGET_SCRIPT}。請先建立 solution_question_10093.py。"
            )

        completed = subprocess.run(
            [sys.executable, str(TARGET_SCRIPT)],
            input=input_data,
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

        return completed.stdout.strip()

    def assertCase(self, grid):
        """驗證指定地圖案例。"""
        input_data = self._build_input(grid)
        expected = str(self._bruteforce_max(grid))
        actual = self._run_solution(input_data)
        self.assertEqual(actual, expected)

    def test_single_plain_cell(self):
        """測試 1x1 平原。"""
        self.assertCase(["P"])

    def test_single_mountain_cell(self):
        """測試 1x1 山地。"""
        self.assertCase(["H"])

    def test_one_row_all_plain(self):
        """測試單列全平原。"""
        self.assertCase(["PPPPP"])

    def test_one_column_all_plain(self):
        """測試單行全平原。"""
        self.assertCase(["P", "P", "P", "P", "P"])

    def test_two_by_two_all_plain(self):
        """測試 2x2 全平原。"""
        self.assertCase(["PP", "PP"])

    def test_three_by_three_all_plain(self):
        """測試 3x3 全平原。"""
        self.assertCase(["PPP", "PPP", "PPP"])

    def test_mixed_terrain(self):
        """測試混合地形。"""
        self.assertCase(["PHP", "PPH", "HPP"])


if __name__ == "__main__":
    unittest.main()
