import subprocess
import sys
import unittest
from pathlib import Path


class TestQuestion10035(unittest.TestCase):
    """UVA 10035（Primary Arithmetic）黑箱單元測試。"""

    @classmethod
    def setUpClass(cls) -> None:
        # 被測程式固定為同目錄下的 question_10035.py
        cls.target_script = Path(__file__).with_name("question_10035.py")

    def _run_case(self, input_data: str, expected_output: str) -> None:
        # 若被測程式不存在，先提供清楚錯誤訊息
        self.assertTrue(
            self.target_script.exists(),
            f"找不到被測程式: {self.target_script}",
        )

        # 以 subprocess 模擬線上評測：stdin 輸入、stdout 比對
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

        # 放寬尾端換行，但中間內容需完全一致
        self.assertEqual(proc.stdout.rstrip(), expected_output.rstrip())

    def test_sample_style_mixed_cases(self) -> None:
        # 經典混合案例：0 次、1 次、多次 carry
        input_data = """123 456
555 555
123 594
0 0
"""
        expected_output = """No carry operation.
3 carry operations.
1 carry operation.
"""
        self._run_case(input_data, expected_output)

    def test_different_digit_lengths(self) -> None:
        # 位數不同時仍要逐位進位（右對齊）
        input_data = """1 99999
0 0
"""
        expected_output = """5 carry operations.
"""
        self._run_case(input_data, expected_output)

    def test_leading_zeros_input(self) -> None:
        # 前導 0 不影響數值，但應保有正確進位次數
        input_data = """0001 0099
0 0
"""
        expected_output = """2 carry operations.
"""
        self._run_case(input_data, expected_output)

    def test_no_output_when_first_line_is_terminator(self) -> None:
        # 若第一行就是 0 0，代表立刻結束且不輸出任何內容
        input_data = """0 0
"""
        expected_output = """
"""
        self._run_case(input_data, expected_output)

    def test_extra_spaces_and_blank_lines(self) -> None:
        # 輸入含額外空白與空行時，解析仍應正確
        input_data = """
  95    5

1 99999
   0   0
"""
        expected_output = """2 carry operations.
5 carry operations.
"""
        self._run_case(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()
