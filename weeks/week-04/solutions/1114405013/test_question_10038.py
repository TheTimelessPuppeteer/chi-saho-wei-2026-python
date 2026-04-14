import subprocess
import sys
import unittest
from pathlib import Path


class TestQuestion10038(unittest.TestCase):
    """UVA 10038（Jolly Jumpers）黑箱單元測試。"""

    @classmethod
    def setUpClass(cls) -> None:
        # 被測程式固定為同目錄下的 question_10038.py
        cls.target_script = Path(__file__).with_name("question_10038.py")

    def _run_case(self, input_data: str, expected_output: str) -> None:
        # 被測程式不存在時，直接回報清楚錯誤訊息
        self.assertTrue(
            self.target_script.exists(),
            f"找不到被測程式: {self.target_script}",
        )

        # 以 subprocess 模擬線上評測：stdin 輸入，stdout 輸出比對
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

        # 允許尾端多一個換行，不放寬中間內容
        self.assertEqual(proc.stdout.rstrip(), expected_output.rstrip())

    def test_single_number_sequence_is_jolly(self) -> None:
        # n=1 時沒有相鄰差值，依定義視為 Jolly
        input_data = """1 100
"""
        expected_output = """Jolly
"""
        self._run_case(input_data, expected_output)

    def test_classic_jolly_case(self) -> None:
        # 經典範例：差值為 3,2,1，完整覆蓋 1..n-1
        input_data = """4 1 4 2 3
"""
        expected_output = """Jolly
"""
        self._run_case(input_data, expected_output)

    def test_classic_not_jolly_case(self) -> None:
        # 經典反例：差值重複且出現超範圍值，不是 Jolly
        input_data = """5 1 4 2 -1 6
"""
        expected_output = """Not jolly
"""
        self._run_case(input_data, expected_output)

    def test_duplicate_differences_not_jolly(self) -> None:
        # 差值全為 3（重複），缺少 1、2，故為 Not jolly
        input_data = """4 1 4 7 10
"""
        expected_output = """Not jolly
"""
        self._run_case(input_data, expected_output)

    def test_multiple_lines_and_whitespace_tolerance(self) -> None:
        # 多組資料 + 負數 + 額外空白，驗證 EOF 逐行處理與容錯
        input_data = """
4   1 4 2 3

5 1 4 2 -1 6
4   -1 -4 -2 -3
"""
        expected_output = """Jolly
Not jolly
Jolly
"""
        self._run_case(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()
