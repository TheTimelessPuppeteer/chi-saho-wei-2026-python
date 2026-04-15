import math
import subprocess
import sys
import unittest
from pathlib import Path


class TestQuestion10221(unittest.TestCase):
    """UVA 10221（Satellites）黑箱單元測試。"""

    EARTH_RADIUS = 6440.0

    @classmethod
    def setUpClass(cls) -> None:
        # 被測程式固定為同目錄下 question_10221.py
        cls.target_script = Path(__file__).with_name("question_10221.py")

    @classmethod
    def _reference(cls, s: float, a: float, unit: str) -> tuple[float, float]:
        """題意對應的參考計算。

        - r = 6440 + s
        - unit=min 時，角度 a 需除以 60 轉成度
        - 若角度 > 180，取較小圓心角 360-a
        - 弧長 = r * rad
        - 弦長 = 2 * r * sin(rad / 2)
        """
        r = cls.EARTH_RADIUS + s

        if unit == "min":
            a = a / 60.0

        if a > 180.0:
            a = 360.0 - a

        rad = a * math.pi / 180.0
        arc = r * rad
        chord = 2.0 * r * math.sin(rad / 2.0)
        return arc, chord

    def _run_case(
        self, input_data: str, expected_pairs: list[tuple[float, float]]
    ) -> None:
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

        # 過濾空行，確保輸出行數與輸入案例數一致
        lines = [line.strip() for line in proc.stdout.splitlines() if line.strip()]
        self.assertEqual(len(lines), len(expected_pairs))

        for i, (line, (exp_arc, exp_chord)) in enumerate(
            zip(lines, expected_pairs), start=1
        ):
            parts = line.split()
            self.assertEqual(
                len(parts),
                2,
                msg=f"第 {i} 行輸出應包含兩個浮點數，實際為: {line}",
            )

            got_arc = float(parts[0])
            got_chord = float(parts[1])

            # 題目要求小數六位，因此以 1e-6 等級驗證
            self.assertAlmostEqual(got_arc, exp_arc, places=6)
            self.assertAlmostEqual(got_chord, exp_chord, places=6)

    def test_problem_sample_like_input(self) -> None:
        # 以題目文件中的示例型態驗證基本正確性
        cases = [
            (500, 30, "deg"),
            (700, 60, "min"),
            (200, 45, "deg"),
        ]
        input_data = "\n".join(f"{s} {a} {u}" for s, a, u in cases) + "\n"
        expected = [self._reference(s, a, u) for s, a, u in cases]
        self._run_case(input_data, expected)

    def test_angle_more_than_180_should_use_minor_arc(self) -> None:
        # a=300 度應等價於 60 度（取較小圓心角）
        cases = [
            (1000, 300, "deg"),
            (1000, 60, "deg"),
        ]
        input_data = "\n".join(f"{s} {a} {u}" for s, a, u in cases) + "\n"
        expected = [self._reference(s, a, u) for s, a, u in cases]
        self._run_case(input_data, expected)

    def test_zero_angle_boundary(self) -> None:
        # 角度為 0 時，弧長與弦長都應為 0
        cases = [(0, 0, "deg")]
        input_data = "0 0 deg\n"
        expected = [self._reference(*cases[0])]
        self._run_case(input_data, expected)

    def test_straight_angle_180_boundary(self) -> None:
        # 角度為 180 度時，弧長為半圓、弦長為直徑
        cases = [(0, 180, "deg")]
        input_data = "0 180 deg\n"
        expected = [self._reference(*cases[0])]
        self._run_case(input_data, expected)

    def test_multiple_lines_mixed_units(self) -> None:
        # 混合 deg / min 多筆輸入，驗證 EOF 逐行處理
        cases = [
            (10, 5400, "min"),  # 5400 分 = 90 度
            (20, 90, "deg"),
            (30, 30, "deg"),
            (40, 1800, "min"),  # 1800 分 = 30 度
        ]
        input_data = "\n".join(f"{s} {a} {u}" for s, a, u in cases) + "\n"
        expected = [self._reference(s, a, u) for s, a, u in cases]
        self._run_case(input_data, expected)


if __name__ == "__main__":
    unittest.main()
