import subprocess
import sys
import unittest
from pathlib import Path


class TestQuestion10019(unittest.TestCase):
    """UVA 10019（依題敘：Hashmat 差值）黑箱單元測試。"""

    @classmethod
    def setUpClass(cls) -> None:
        # 被測程式固定為同目錄下的 question_10019.py
        cls.target_script = Path(__file__).with_name("question_10019.py")

    def _run_case(self, input_data: str, expected_output: str) -> None:
        # 若檔案不存在，先回報清楚錯誤
        self.assertTrue(
            cls_exists := self.target_script.exists(),
            f"找不到被測程式: {self.target_script}",
        )
        if not cls_exists:
            return

        # 以 subprocess 模擬線上評測：stdin -> 程式 -> stdout
        proc = subprocess.run(
            [sys.executable, str(self.target_script)],
            input=input_data,
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertEqual(
            proc.returncode,
            0,
            msg=f"程式異常結束，stderr:\n{proc.stderr}",
        )

        # 僅放寬尾端換行，不放寬中間內容
        self.assertEqual(proc.stdout.rstrip(), expected_output.rstrip())

    def test_basic_difference(self) -> None:
        # 基本案例：直接計算 |10 - 12| = 2
        input_data = """10 12
"""
        expected_output = """2
"""
        self._run_case(input_data, expected_output)

    def test_swapped_order_still_positive(self) -> None:
        # 題敘提到可能是 Hashmat/敵人任一順序，輸出仍應為正差值
        input_data = """100 5
5 100
"""
        expected_output = """95
95
"""
        self._run_case(input_data, expected_output)

    def test_multiple_lines_until_eof(self) -> None:
        # UVA 此題通常是 EOF 輸入，需連續處理多組資料
        input_data = """1 1
0 10
999 1
"""
        expected_output = """0
10
998
"""
        self._run_case(input_data, expected_output)

    def test_large_values_near_2_power_63(self) -> None:
        # 大整數邊界：驗證接近 2^63 的數值也能正確處理
        input_data = """9223372036854775807 0
9223372036854775807 9223372036854775806
"""
        expected_output = """9223372036854775807
1
"""
        self._run_case(input_data, expected_output)

    def test_extra_spaces_and_blank_lines(self) -> None:
        # 容忍多空白與空行（若程式使用 split() 解析可自然通過）
        input_data = """
   3     9

7      2

  50   50
"""
        expected_output = """6
5
0
"""
        self._run_case(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()
