"""Question 10071 的單元測試。"""

import subprocess
import sys
import unittest
from pathlib import Path


TARGET_SCRIPT = Path(__file__).with_name("solution_question_10071.py")


class TestQuestion10071(unittest.TestCase):
    """測試六元組計數問題。"""

    def _build_input(self, values):
        """將集合內容組成題目輸入格式。"""
        lines = [str(len(values))]
        lines.extend(str(value) for value in values)
        return "\n".join(lines) + "\n"

    def _bruteforce_count(self, values):
        """用暴力法計算符合條件的六元組數量。

        這個 helper 只用在小型測資，作為正確答案來源。
        """
        count = 0
        for a in values:
            for b in values:
                for c in values:
                    for d in values:
                        for e in values:
                            total = a + b + c + d + e
                            for f in values:
                                if total == f:
                                    count += 1
        return count

    def _run_solution(self, input_data):
        """執行被測程式並回傳標準輸出。"""
        if not TARGET_SCRIPT.exists():
            self.fail(
                "找不到被測程式："
                f"{TARGET_SCRIPT}。請先建立 solution_question_10071.py。"
            )

        completed = subprocess.run(
            [sys.executable, str(TARGET_SCRIPT)],
            input=input_data,
            text=True,
            capture_output=True,
            check=False,
        )

        if completed.returncode != 0:
            self.fail(
                "被測程式執行失敗。\n"
                f"return code: {completed.returncode}\n"
                f"stderr:\n{completed.stderr}"
            )

        return completed.stdout.strip()

    def assertCase(self, values):
        """驗證指定集合的輸出是否正確。"""
        input_data = self._build_input(values)
        expected_output = str(self._bruteforce_count(values))
        actual_output = self._run_solution(input_data)
        self.assertEqual(actual_output, expected_output)

    def test_single_zero(self):
        """測試只有 0 的最小集合。"""
        # 只有一個元素 0 時，0+0+0+0+0=0，剛好有 1 種六元組。
        self.assertCase([0])

    def test_single_positive(self):
        """測試只有正數的單元素集合。"""
        # 只有 1 時，1+1+1+1+1 不會等於 1，因此答案為 0。
        self.assertCase([1])

    def test_small_zero_one_set(self):
        """測試含 0 與 1 的小集合。"""
        self.assertCase([0, 1])

    def test_small_negative_positive_set(self):
        """測試含負數、0、正數的集合。"""
        self.assertCase([-1, 0, 1])

    def test_small_mixed_values(self):
        """測試一般混合小集合。"""
        self.assertCase([-2, 1, 3])


if __name__ == "__main__":
    unittest.main()
