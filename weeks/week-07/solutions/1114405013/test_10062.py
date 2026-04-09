"""Question 10062 的單元測試。

此測試檔針對競賽常見的 stdin/stdout 介面設計，
預設會執行同資料夾下的 `solution_question_10062.py`。
"""

import subprocess
import sys
import unittest
from pathlib import Path


# 被測程式預設路徑。
TARGET_SCRIPT = Path(__file__).with_name("solution_question_10062.py")


class TestQuestion10062(unittest.TestCase):
    """測試乳牛排列重建問題。"""

    def _counts_from_permutation(self, permutation):
        """根據排列產生題目輸入需要的計數資料。

        對於第 i 個位置的乳牛，計算在它前面且編號比它小的乳牛數量。
        題目不提供第一個位置的資料，因此回傳長度會是 N - 1。
        """
        counts = []
        for index in range(1, len(permutation)):
            current = permutation[index]
            smaller_before = sum(1 for value in permutation[:index] if value < current)
            counts.append(smaller_before)
        return counts

    def _build_input(self, permutation):
        """將指定排列轉成題目輸入格式。"""
        counts = self._counts_from_permutation(permutation)
        lines = [str(len(permutation))]
        lines.extend(str(count) for count in counts)
        return "\n".join(lines) + "\n"

    def _expected_output(self, permutation):
        """將指定排列轉成預期輸出格式。"""
        return "\n".join(str(value) for value in permutation)

    def _run_solution(self, input_data):
        """執行被測程式並回傳標準輸出。"""
        if not TARGET_SCRIPT.exists():
            self.fail(
                "找不到被測程式："
                f"{TARGET_SCRIPT}。請先建立 solution_question_10062.py。"
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

    def assertPermutationSolved(self, permutation):
        """驗證指定排列是否能被正確重建。"""
        input_data = self._build_input(permutation)
        expected_output = self._expected_output(permutation)
        actual_output = self._run_solution(input_data)
        self.assertEqual(actual_output, expected_output)

    def test_minimum_case_ascending(self):
        """測試最小合法案例中的遞增排列。"""
        # N = 2 時，輸入只會有一個計數值。
        # 排列 [1, 2] 代表第二頭牛前面有 1 頭編號比它小的牛。
        self.assertPermutationSolved([1, 2])

    def test_minimum_case_descending(self):
        """測試最小合法案例中的遞減排列。"""
        # 排列 [2, 1] 時，第二頭牛前面沒有比它更小的編號。
        self.assertPermutationSolved([2, 1])

    def test_monotonic_increasing_order(self):
        """測試完全遞增的排列。"""
        # 這種情況下，第 i 個位置前面全部都是更小的牛。
        self.assertPermutationSolved([1, 2, 3, 4, 5])

    def test_monotonic_decreasing_order(self):
        """測試完全遞減的排列。"""
        # 這種情況下，除了第一個位置外，其餘輸入計數都會是 0。
        self.assertPermutationSolved([5, 4, 3, 2, 1])

    def test_mixed_order_case(self):
        """測試一般混合排列。"""
        # 此案例可驗證程式不是只處理單調順序。
        self.assertPermutationSolved([2, 1, 4, 3, 5])

    def test_longer_mixed_order_case(self):
        """測試較長且分布不規則的排列。"""
        # 這組資料用來檢查多個位置的計數交錯情況。
        self.assertPermutationSolved([3, 1, 6, 2, 5, 4])


if __name__ == "__main__":
    # 直接執行此檔案時，會跑完整份單元測試。
    unittest.main()
