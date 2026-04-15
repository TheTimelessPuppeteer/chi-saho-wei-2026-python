import subprocess
import sys
import unittest
from pathlib import Path


class TestQuestion10189(unittest.TestCase):
    """UVA 10189（Minesweeper）黑箱單元測試。"""

    @classmethod
    def setUpClass(cls) -> None:
        # 被測程式固定為同目錄下的 question_10189.py
        cls.target_script = Path(__file__).with_name("question_10189.py")

    def _run_case(self, input_data: str, expected_output: str) -> None:
        # 若被測檔不存在，先給出明確錯誤訊息。
        self.assertTrue(
            self.target_script.exists(),
            f"找不到被測程式: {self.target_script}",
        )

        # 以 subprocess 模擬線上評測（stdin -> 程式 -> stdout）。
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

        # 允許尾端換行差異，但中間格式（含空白列）必須一致。
        self.assertEqual(proc.stdout.rstrip(), expected_output.rstrip())

    def test_problem_sample_two_fields(self) -> None:
        # 題目範例：驗證多組 Field、標題編號與組間空白列格式。
        input_data = """4 4
*...
....
.*..
....
3 5
**...
.....
.*...
0 0
"""
        expected_output = """Field #1:
*100
2210
1*10
1110

Field #2:
**100
33200
1*100
"""
        self._run_case(input_data, expected_output)

    def test_single_cell_mine(self) -> None:
        # 1x1 且為地雷：輸出應保留星號。
        input_data = """1 1
*
0 0
"""
        expected_output = """Field #1:
*
"""
        self._run_case(input_data, expected_output)

    def test_single_cell_empty(self) -> None:
        # 1x1 且為空白：周圍沒有地雷，應輸出 0。
        input_data = """1 1
.
0 0
"""
        expected_output = """Field #1:
0
"""
        self._run_case(input_data, expected_output)

    def test_all_mines_grid(self) -> None:
        # 全地雷地圖：每格都維持星號，不做數字計算。
        input_data = """2 3
***
***
0 0
"""
        expected_output = """Field #1:
***
***
"""
        self._run_case(input_data, expected_output)

    def test_edge_and_corner_neighbor_counting(self) -> None:
        # 驗證角落與邊緣計數是否正確（常見 off-by-one 錯誤點）。
        input_data = """3 3
*..
...
..*
0 0
"""
        expected_output = """Field #1:
*10
121
01*
"""
        self._run_case(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()
