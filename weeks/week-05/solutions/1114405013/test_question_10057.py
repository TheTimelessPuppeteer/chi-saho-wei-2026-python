import subprocess
import sys
import unittest
from pathlib import Path


class TestQuestion10057(unittest.TestCase):
    """UVA 10057（A Mid-Summer Night's Dream）黑箱單元測試。"""

    @classmethod
    def setUpClass(cls) -> None:
        # 被測程式固定為同目錄下的 question_10057.py
        cls.target_script = Path(__file__).with_name("question_10057.py")

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

    def test_single_value_case(self) -> None:
        # 只有一個數字時：
        # 最佳 A 就是該數字，最小值數量為 1，可能 A 的數量也為 1
        input_data = """1
100
"""
        expected_output = """100 1 1
"""
        self._run_case(input_data, expected_output)

    def test_odd_count_with_repeated_median(self) -> None:
        # 奇數個數時，唯一最佳 A 為中位數
        # 這組資料中位數是 2，且 2 出現 3 次
        input_data = """5
1 2 2 2 9
"""
        expected_output = """2 3 1
"""
        self._run_case(input_data, expected_output)

    def test_even_count_distinct_middle_values(self) -> None:
        # 偶數個數時，若兩個中位值分別為 2 與 4，
        # 任意 A in [2,4] 都可達最小值，故可能 A 數量為 3
        # 第一欄需輸出較小中位值 2
        # 第二欄為落在 [2,4] 的資料數量：2,2,4,4 共 4 個
        input_data = """6
1 2 2 4 4 10
"""
        expected_output = """2 4 3
"""
        self._run_case(input_data, expected_output)

    def test_all_values_same(self) -> None:
        # 全部數字都相同時，答案應為：該值、n、1
        input_data = """4
7 7 7 7
"""
        expected_output = """7 4 1
"""
        self._run_case(input_data, expected_output)

    def test_multiple_cases_until_eof(self) -> None:
        # 題目為多組測資直到 EOF，需逐組輸出
        input_data = """1
100
6
1 2 2 4 4 10
4
10 10 20 20
"""
        expected_output = """100 1 1
2 4 3
10 4 11
"""
        self._run_case(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()
