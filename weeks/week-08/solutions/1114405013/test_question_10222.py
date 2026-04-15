import subprocess
import sys
import unittest
from pathlib import Path


class TestQuestion10222(unittest.TestCase):
    """UVA 10222（Decode the Mad man）黑箱單元測試。"""

    # 題目指定的 QWERTY 鍵盤配置（只使用小寫）。
    ROWS = [
        "`1234567890-=",
        "qwertyuiop[]\\",
        "asdfghjkl;'",
        "zxcvbnm,./",
    ]

    @classmethod
    def setUpClass(cls) -> None:
        # 被測程式固定為同目錄下的 question_10222.py
        cls.target_script = Path(__file__).with_name("question_10222.py")

    @classmethod
    def _decode_ref(cls, text: str) -> str:
        """參考解碼器：每個字元往鍵盤左移三格。"""
        mapping = {}
        for row in cls.ROWS:
            for i in range(3, len(row)):
                mapping[row[i]] = row[i - 3]

        out = []
        for ch in text:
            if ch == "\n":
                out.append("\n")
                continue

            low = ch.lower()
            if low in mapping:
                decoded = mapping[low]
                # 若輸入是大寫字母，輸出也維持大寫。
                out.append(decoded.upper() if ch.isupper() else decoded)
            else:
                # 不在映射表的字元（例如空白）原樣保留。
                out.append(ch)
        return "".join(out)

    def _run_case(self, input_data: str) -> None:
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

        expected = self._decode_ref(input_data)
        self.assertEqual(proc.stdout, expected)

    def test_basic_letters(self) -> None:
        # 基本字母解碼：例如 r->e, t->r, y->t
        self._run_case("rty\n")

    def test_digits_and_symbols(self) -> None:
        # 測試數字與符號也要能左移三鍵
        self._run_case("7890-=\\\n")

    def test_sentence_with_spaces(self) -> None:
        # 空白需原樣保留，只有鍵盤字元會被映射
        self._run_case("jr;;p ept;f\n")

    def test_multiple_lines_until_eof(self) -> None:
        # 多行輸入（EOF）應逐行完整解碼
        self._run_case("rty\nujm\n\npl,\n")

    def test_uppercase_preserved(self) -> None:
        # 若輸入為大寫字母，輸出也應維持大寫
        self._run_case("RTY UJM\n")


if __name__ == "__main__":
    unittest.main()
