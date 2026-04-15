import subprocess
import sys
import unittest
from pathlib import Path


class TestQuestion10190(unittest.TestCase):
    """QUESTION-10190（自動傘）黑箱單元測試。"""

    @classmethod
    def setUpClass(cls) -> None:
        # 被測程式固定為同目錄下的 question_10190.py
        cls.target_script = Path(__file__).with_name("question_10190.py")

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

    def test_no_umbrella_baseline(self) -> None:
        # 無任何自動傘時，全部降雨都落在馬路上：W * T * V
        # 10 * 5 * 2 = 100.00
        input_data = """0 10 5 2
"""
        expected_output = """100.00
"""
        self._run_case(input_data, expected_output)

    def test_single_stationary_umbrella(self) -> None:
        # 單把靜止傘，覆蓋長度固定為 l
        # 落地雨量 = (W - l) * T * V = (10 - 4) * 5 * 2 = 60.00
        input_data = """1 10 5 2
2 4 0
"""
        expected_output = """60.00
"""
        self._run_case(input_data, expected_output)

    def test_single_moving_umbrella_same_covered_length(self) -> None:
        # 單把傘即使移動（含反彈），在任何時刻覆蓋長度仍是 l
        # 因此落地雨量仍是 (W - l) * T * V
        # (12 - 3) * 4 * 1 = 36.00
        input_data = """1 12 4 1
5 3 -2
"""
        expected_output = """36.00
"""
        self._run_case(input_data, expected_output)

    def test_two_stationary_umbrellas_with_overlap(self) -> None:
        # 兩把靜止傘有重疊時，應以聯集覆蓋長度計算
        # 傘1: [1,5]，傘2: [3,7]，聯集長度 6
        # 落地雨量 = (10 - 6) * 5 * 2 = 40.00
        input_data = """2 10 5 2
1 4 0
3 4 0
"""
        expected_output = """40.00
"""
        self._run_case(input_data, expected_output)

    def test_full_coverage_and_rounding(self) -> None:
        # 完全覆蓋時，不論 V/T 為何，落地雨量都應為 0.00
        # 也同時檢查輸出格式是否保留到小數點後兩位
        input_data = """1 8 7 3
0 8 1
"""
        expected_output = """0.00
"""
        self._run_case(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()
