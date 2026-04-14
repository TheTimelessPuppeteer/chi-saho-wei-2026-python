import subprocess
import sys
import unittest
from pathlib import Path


class TestQuestion10008(unittest.TestCase):
    """UVA 10008 的黑箱單元測試。"""

    @classmethod
    def setUpClass(cls) -> None:
        # 被測程式固定為同目錄下的 question_10008.py
        cls.target_script = Path(__file__).with_name("question_10008.py")

    def _run_case(self, input_data: str, expected_output: str) -> None:
        # 若被測檔不存在，直接提供清楚錯誤訊息
        self.assertTrue(
            self.target_script.exists(),
            f"找不到被測程式: {self.target_script}",
        )

        # 使用 subprocess 模擬線上評測：由 stdin 餵資料、比對 stdout
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

        # 放寬最後尾端換行，但不放寬中間內容
        self.assertEqual(proc.stdout.rstrip(), expected_output.rstrip())

    def test_mixed_case_and_frequency_sorting(self) -> None:
        # 驗證：大小寫視為同字母，並依「次數降序、字母升序」輸出
        input_data = """3
This is a test.
Count me 100%!
AAA bbb c
"""
        expected_output = """A 4
T 4
B 3
S 3
C 2
E 2
I 2
H 1
M 1
N 1
O 1
U 1
"""
        self._run_case(input_data, expected_output)

    def test_tie_breaker_by_alphabet(self) -> None:
        # 驗證：當次數相同時，必須以字母順序（A~Z）排序
        input_data = """1
bBaA
"""
        expected_output = """A 2
B 2
"""
        self._run_case(input_data, expected_output)

    def test_ignore_non_letters(self) -> None:
        # 驗證：數字、符號、空白都應忽略；只有英文字母會被統計
        input_data = """2
1234!!!
   
"""
        expected_output = """
"""
        self._run_case(input_data, expected_output)

    def test_empty_line_content_is_allowed(self) -> None:
        # 驗證：n 行資料中可包含空行，且仍可正確統計其他行
        input_data = """3

Aa
Z
"""
        expected_output = """A 2
Z 1
"""
        self._run_case(input_data, expected_output)

    def test_zero_lines_input(self) -> None:
        # 驗證：n=0 時沒有任何待分析文字，輸出應為空
        input_data = """0
"""
        expected_output = """
"""
        self._run_case(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()
