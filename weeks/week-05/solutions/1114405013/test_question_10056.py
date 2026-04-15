import subprocess
import sys
import unittest
from pathlib import Path


class TestQuestion10056(unittest.TestCase):
    """UVA 10056（What is the Probability ?）黑箱單元測試。"""

    @classmethod
    def setUpClass(cls) -> None:
        # 被測程式固定為同目錄下的 question_10056.py
        cls.target_script = Path(__file__).with_name("question_10056.py")

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

        # 放寬尾端換行差異，但其餘輸出需完全一致（含四位小數格式）
        self.assertEqual(proc.stdout.rstrip(), expected_output.rstrip())

    def test_single_player_always_wins(self) -> None:
        # N=1 時，第一位玩家總會在成功事件第一次發生時獲勝
        input_data = """1
1 0.5 1
"""
        expected_output = """1.0000
"""
        self._run_case(input_data, expected_output)

    def test_two_players_equal_success_probability(self) -> None:
        # N=2, p=0.5 時，玩家 1 與玩家 2 的勝率分別為 2/3 與 1/3
        input_data = """2
2 0.5 1
2 0.5 2
"""
        expected_output = """0.6667
0.3333
"""
        self._run_case(input_data, expected_output)

    def test_three_players_normal_case(self) -> None:
        # 一般案例：N=3, p=0.2，驗證不同 i 的機率與四位小數輸出
        input_data = """2
3 0.2 2
3 0.2 3
"""
        expected_output = """0.3279
0.2623
"""
        self._run_case(input_data, expected_output)

    def test_zero_probability_never_wins(self) -> None:
        # p=0 時，成功事件永遠不會發生，任何玩家勝率都為 0
        input_data = """1
10 0.0 4
"""
        expected_output = """0.0000
"""
        self._run_case(input_data, expected_output)

    def test_probability_one_boundary(self) -> None:
        # p=1 時，每輪第一位玩家必勝，其餘玩家勝率為 0
        input_data = """2
5 1.0 1
5 1.0 3
"""
        expected_output = """1.0000
0.0000
"""
        self._run_case(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()
