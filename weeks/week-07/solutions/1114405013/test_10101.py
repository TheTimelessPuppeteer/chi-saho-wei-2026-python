"""Question 10101 的單元測試。"""

import subprocess
import sys
import unittest
from pathlib import Path


TARGET_SCRIPT = Path(__file__).with_name("solution_question_10101.py")

# 七段顯示器對應（a,b,c,d,e,f,g）
SEGMENTS = {
    "0": {"a", "b", "c", "d", "e", "f"},
    "1": {"b", "c"},
    "2": {"a", "b", "d", "e", "g"},
    "3": {"a", "b", "c", "d", "g"},
    "4": {"b", "c", "f", "g"},
    "5": {"a", "c", "d", "f", "g"},
    "6": {"a", "c", "d", "e", "f", "g"},
    "7": {"a", "b", "c"},
    "8": {"a", "b", "c", "d", "e", "f", "g"},
    "9": {"a", "b", "c", "d", "f", "g"},
}


class TestQuestion10101(unittest.TestCase):
    """測試單根木棒移動等式修正問題。"""

    def _run_solution(self, raw_input):
        """執行被測程式並回傳單行輸出。"""
        if not TARGET_SCRIPT.exists():
            self.fail(
                "找不到被測程式："
                f"{TARGET_SCRIPT}。請先建立 solution_question_10101.py。"
            )

        completed = subprocess.run(
            [sys.executable, str(TARGET_SCRIPT)],
            input=raw_input,
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

    def _eval_side(self, text):
        """計算只含 +、- 與整數的表達式值（允許前導零）。"""
        i = 0
        sign = 1
        total = 0

        if i < len(text) and text[i] == "-":
            sign = -1
            i += 1

        while i < len(text):
            start = i
            while i < len(text) and text[i].isdigit():
                i += 1

            if start == i:
                raise ValueError("數字解析失敗")

            total += sign * int(text[start:i])

            if i >= len(text):
                break

            if text[i] == "+":
                sign = 1
            elif text[i] == "-":
                sign = -1
            else:
                raise ValueError("運算符解析失敗")
            i += 1

        return total

    def _is_equation_true(self, expr):
        """檢查等式是否成立。"""
        if expr.count("=") != 1:
            return False
        left, right = expr.split("=")
        return self._eval_side(left) == self._eval_side(right)

    def _is_one_match_move(self, original_expr, new_expr):
        """檢查是否只移動一根數字木棒。"""
        if len(original_expr) != len(new_expr):
            return False

        # 非數字位置必須完全相同（運算符不能改）。
        for oc, nc in zip(original_expr, new_expr):
            if not oc.isdigit() or not nc.isdigit():
                if oc != nc:
                    return False

        removed = 0
        added = 0

        for oc, nc in zip(original_expr, new_expr):
            if not oc.isdigit():
                continue

            before = SEGMENTS[oc]
            after = SEGMENTS[nc]
            removed += len(before - after)
            added += len(after - before)

        return removed == 1 and added == 1

    def _assert_valid_solution(self, original, candidate):
        """斷言輸出為合法可行解。"""
        self.assertTrue(candidate.endswith("#"), "輸出需以 # 結尾")

        original_expr = original[:-1]
        new_expr = candidate[:-1]

        self.assertTrue(
            self._is_equation_true(new_expr),
            "輸出等式必須成立",
        )
        self.assertTrue(
            self._is_one_match_move(original_expr, new_expr),
            "必須是只移動一根木棒得到的新等式",
        )

    def test_known_solvable_case(self):
        """測試已知可解案例。"""
        source = "1+1=3#\n"
        result = self._run_solution(source)

        self.assertNotEqual(result, "No", "可解案例不應輸出 No")
        self._assert_valid_solution(source.strip(), result)

    def test_known_unsolvable_case(self):
        """測試已知無解案例。"""
        source = "1+1=1#\n"
        result = self._run_solution(source)
        self.assertEqual(result, "No")


if __name__ == "__main__":
    unittest.main()
