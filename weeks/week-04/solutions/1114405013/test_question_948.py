import subprocess
import sys
import unittest
from pathlib import Path


class TestQuestion948(unittest.TestCase):
    """UVA 948 假幣問題的黑箱單元測試。"""

    @classmethod
    def setUpClass(cls) -> None:
        # 被測程式固定為同目錄下的 main.py
        cls.target_script = Path(__file__).with_name("main.py")

    def _run_case(self, input_data: str, expected_output: str) -> None:
        # 若 main.py 尚未建立，直接給出清楚錯誤訊息
        self.assertTrue(
            self.target_script.exists(),
            f"找不到被測程式: {self.target_script}",
        )

        # 以 subprocess 模擬線上評測：餵 stdin、比對 stdout
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

        # 允許最後多一個換行，但不放寬中間內容（含空白列）
        self.assertEqual(proc.stdout.rstrip(), expected_output.rstrip())

    def test_single_case_unique_lighter(self) -> None:
        # 先用 '=' 證明 1、2 都是真幣，再由 '<' 推出 3 較輕且為假幣
        input_data = """1

4 2
1 1 2
=
1 3 1
<
"""
        expected_output = """3
"""
        self._run_case(input_data, expected_output)

    def test_single_case_unique_heavier(self) -> None:
        # 先用 '=' 證明 1、3 都是真幣，再由 '>' 推出 2 較重且為假幣
        input_data = """1

4 2
1 1 3
=
1 2 1
>
"""
        expected_output = """2
"""
        self._run_case(input_data, expected_output)

    def test_ambiguous_case_returns_zero(self) -> None:
        # 只有一次 '=' 可排除 1、2，剩下 3、4 都可能是假幣，故答案為 0
        input_data = """1

4 1
1 1 2
=
"""
        expected_output = """0
"""
        self._run_case(input_data, expected_output)

    def test_multiple_cases_require_blank_line_between_outputs(self) -> None:
        # 驗證多組測資輸出時，兩組答案之間必須保留一個空白列
        input_data = """2

4 2
1 1 2
=
1 3 1
<

4 1
1 1 2
=
"""
        expected_output = """3

0
"""
        self._run_case(input_data, expected_output)

    def test_input_with_extra_blank_lines(self) -> None:
        # 題目輸入敘述含空白列，本案例刻意加入較多空白列驗證解析穩定性
        input_data = """2


4 2
1 1 3
=
1 2 1
>


4 1
1 1 2
=

"""
        expected_output = """2

0
"""
        self._run_case(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()
