import subprocess
import sys
import unittest
from pathlib import Path


class TestQuestion10050(unittest.TestCase):
    """UVA 10050（Hartals）黑箱單元測試。"""

    @classmethod
    def setUpClass(cls) -> None:
        # 被測程式固定為同目錄下的 question_10050.py
        cls.target_script = Path(__file__).with_name("question_10050.py")

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

    def test_official_example_style_case(self) -> None:
        # 題目敘述中的經典案例：N=14, h=[3,4,8]，答案為 5
        input_data = """1
14
3
3
4
8
"""
        expected_output = """5
"""
        self._run_case(input_data, expected_output)

    def test_skip_friday_and_saturday(self) -> None:
        # h=1 代表每天都可能罷會，但週五/週六不算工作日
        # 在 7 天內實際只會損失 5 天工作日
        input_data = """1
7
1
1
"""
        expected_output = """5
"""
        self._run_case(input_data, expected_output)

    def test_overlap_should_count_once(self) -> None:
        # 不同政黨同一天罷會只能算 1 天
        # N=14, h=[2,4] 時，工作日損失為第 2,4,8,10,12 天，共 5 天
        input_data = """1
14
2
2
4
"""
        expected_output = """5
"""
        self._run_case(input_data, expected_output)

    def test_multiple_testcases_in_one_input(self) -> None:
        # 同次輸入含多組測資時，需逐組輸出結果
        # case1: N=14, h=[3,4,8] -> 5
        # case2: N=30, h=[2,3,4] -> 14
        # case3: N=20, h=[5,6] -> 5
        input_data = """3
14
3
3
4
8
30
3
2
3
4
20
2
5
6
"""
        expected_output = """5
14
5
"""
        self._run_case(input_data, expected_output)

    def test_larger_day_range(self) -> None:
        # 較大天數範圍，確認在多政黨下仍可正確計數
        input_data = """1
100
4
12
15
25
40
"""
        expected_output = """15
"""
        self._run_case(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()
