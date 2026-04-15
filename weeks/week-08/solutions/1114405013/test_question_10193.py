import math
import subprocess
import sys
import unittest
from pathlib import Path


class TestQuestion10193(unittest.TestCase):
    """UVA 10193（Arctan Identity）黑箱單元測試。"""

    @classmethod
    def setUpClass(cls) -> None:
        # 被測程式固定為同目錄下的 question_10193.py
        cls.target_script = Path(__file__).with_name("question_10193.py")

    def _run_case(self, input_data: str, expected_output: str) -> None:
        # 若目標程式不存在，先給明確錯誤訊息
        self.assertTrue(
            self.target_script.exists(),
            f"找不到被測程式: {self.target_script}",
        )

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

        # 放寬尾端換行，其他內容必須一致
        self.assertEqual(proc.stdout.rstrip(), expected_output.rstrip())

    @staticmethod
    def _expected_min_b_plus_c(a: int) -> int:
        """以數學轉換計算正確答案（測試端參考實作）。

        由題式可推得：
            (b-a)(c-a) = a^2 + 1
        設 d = b-a，則 d | (a^2+1)，且 c-a = (a^2+1)/d。
        因此：
            b + c = 2a + d + (a^2+1)/d
        對所有正因數 d 取最小值即為答案。
        """
        n = a * a + 1
        best = None
        limit = int(math.isqrt(n))

        for d in range(1, limit + 1):
            if n % d != 0:
                continue
            q = n // d
            value = 2 * a + d + q
            if best is None or value < best:
                best = value

        assert best is not None
        return best

    def test_known_small_values(self) -> None:
        # 小數值可手算驗證，確保基礎邏輯正確
        # a=1 -> 5, a=2 -> 10, a=3 -> 13
        self._run_case("1\n", "5\n")
        self._run_case("2\n", "10\n")
        self._run_case("3\n", "13\n")

    def test_various_values_against_reference_formula(self) -> None:
        # 用多組 a 對照測試端參考公式，避免只過固定樣例
        for a in [4, 5, 7, 10, 25, 123, 999]:
            expected = self._expected_min_b_plus_c(a)
            self._run_case(f"{a}\n", f"{expected}\n")

    def test_upper_bound_value(self) -> None:
        # 題目上限 a=60000，驗證大數仍能輸出整數答案
        a = 60000
        expected = self._expected_min_b_plus_c(a)
        self._run_case(f"{a}\n", f"{expected}\n")

    def test_input_with_surrounding_spaces(self) -> None:
        # 驗證輸入前後空白不影響解析
        a = 42
        expected = self._expected_min_b_plus_c(a)
        self._run_case(f"   {a}   \n", f"{expected}\n")

    def test_output_is_single_integer_line(self) -> None:
        # 輸出應僅包含整數，不應附加說明文字
        a = 11
        expected = str(self._expected_min_b_plus_c(a))

        proc = subprocess.run(
            [sys.executable, str(self.target_script)],
            input=f"{a}\n",
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, msg=proc.stderr)
        self.assertEqual(proc.stdout.strip(), expected)
        self.assertRegex(proc.stdout.strip(), r"^\d+$")


if __name__ == "__main__":
    unittest.main()
