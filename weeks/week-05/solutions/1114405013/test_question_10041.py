import subprocess
import sys
import unittest
from pathlib import Path


class TestQuestion10041(unittest.TestCase):
    """UVA 10041（Vito's Family）黑箱單元測試。"""

    @classmethod
    def setUpClass(cls) -> None:
        # 被測程式固定為同目錄下的 question_10041.py
        cls.target_script = Path(__file__).with_name("question_10041.py")

    def _run_case(self, input_data: str, expected_output: str) -> None:
        # 若被測檔不存在，先回報清楚訊息
        self.assertTrue(
            self.target_script.exists(),
            f"找不到被測程式: {self.target_script}",
        )

        # 以 subprocess 模擬線上評測（stdin -> 程式 -> stdout）
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

        # 放寬尾端換行差異，但其餘輸出需完全一致
        self.assertEqual(proc.stdout.rstrip(), expected_output.rstrip())

    def test_single_relative(self) -> None:
        # 只有一位親戚時，最小總距離必為 0
        input_data = """1
1 100
"""
        expected_output = """0
"""
        self._run_case(input_data, expected_output)

    def test_odd_count_addresses(self) -> None:
        # 奇數筆門牌，最佳位置在中位數（4），總距離為 4
        # |2-4| + |4-4| + |6-4| = 2 + 0 + 2 = 4
        input_data = """1
3 2 4 6
"""
        expected_output = """4
"""
        self._run_case(input_data, expected_output)

    def test_even_count_addresses(self) -> None:
        # 偶數筆門牌，介於兩個中位數之間皆可達最小值
        # 對 2,4,6,8 最小總距離為 8
        input_data = """1
4 2 4 6 8
"""
        expected_output = """8
"""
        self._run_case(input_data, expected_output)

    def test_duplicate_addresses(self) -> None:
        # 有重複門牌時仍可用中位數概念，答案應為 9
        input_data = """1
4 2 2 3 10
"""
        expected_output = """9
"""
        self._run_case(input_data, expected_output)

    def test_multiple_testcases(self) -> None:
        # 同一次輸入含多組資料，需逐組輸出對應最小總距離
        input_data = """3
2 2 4
5 1 2 10 20 30
6 1 1 2 2 4 100
"""
        expected_output = """2
47
102
"""
        self._run_case(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()
