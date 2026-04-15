import subprocess
import sys
import unittest
from pathlib import Path


class TestQuestion10055(unittest.TestCase):
    """UVA 10055 黑箱單元測試。"""

    @classmethod
    def setUpClass(cls) -> None:
        # 被測程式固定為同目錄下的 question_10055.py
        cls.target_script = Path(__file__).with_name("question_10055.py")

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

    def test_basic_query_then_flip(self) -> None:
        # 初始全部為增函數，所以查詢整段應輸出 0
        # 翻轉一個函數後，減函數數量為奇數，整段查詢應輸出 1
        input_data = """5 3
2 1 5
1 3
2 1 5
"""
        expected_output = """0
1
"""
        self._run_case(input_data, expected_output)

    def test_flip_same_index_twice(self) -> None:
        # 同一位置翻轉兩次會回到原本狀態
        input_data = """4 6
1 2
2 1 4
1 2
2 1 4
1 4
2 3 4
"""
        expected_output = """1
0
1
"""
        self._run_case(input_data, expected_output)

    def test_range_parity_changes(self) -> None:
        # 驗證不同區間查詢時，減函數個數奇偶變化是否正確
        input_data = """8 9
1 2
1 5
1 7
2 1 8
2 2 5
2 6 8
1 5
2 2 5
2 5 7
"""
        expected_output = """1
0
1
1
1
"""
        self._run_case(input_data, expected_output)

    def test_single_function_boundary(self) -> None:
        # N=1 的邊界情況：查詢結果應直接反映該函數是否被翻轉
        input_data = """1 5
2 1 1
1 1
2 1 1
1 1
2 1 1
"""
        expected_output = """0
1
0
"""
        self._run_case(input_data, expected_output)

    def test_no_query_outputs_empty(self) -> None:
        # 全部操作都是翻轉時，不應輸出任何內容
        input_data = """3 2
1 1
1 2
"""
        expected_output = """"""
        self._run_case(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()
