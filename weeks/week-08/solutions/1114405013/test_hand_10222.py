import subprocess
import sys
import unittest
from pathlib import Path


class TestHand10222(unittest.TestCase):
    """hand_10222.py 黑箱單元測試。"""

    ROWS = [
        "`1234567890-=",
        "qwertyuiop[]\\",
        "asdfghjkl;'",
        "zxcvbnm,./",
    ]

    @classmethod
    def setUpClass(cls) -> None:
        cls.target_script = Path(__file__).with_name("hand_10222.py")

    @classmethod
    def _decode_ref(cls, text: str) -> str:
        mapping = {}
        for row in cls.ROWS:
            for i in range(3, len(row)):
                mapping[row[i]] = row[i - 3]

        out = []
        for ch in text:
            low = ch.lower()
            if low in mapping:
                d = mapping[low]
                out.append(d.upper() if ch.isupper() else d)
            else:
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
        self.assertEqual(proc.returncode, 0, msg=f"stderr:\n{proc.stderr}")
        self.assertEqual(proc.stdout, self._decode_ref(input_data))

    def test_basic_letters(self) -> None:
        self._run_case("rty\n")

    def test_digits_and_symbols(self) -> None:
        self._run_case("7890-=\\\n")

    def test_sentence_with_spaces(self) -> None:
        self._run_case("jr;;p ept;f\n")

    def test_multiple_lines_until_eof(self) -> None:
        self._run_case("rty\nujm\n\npl,\n")

    def test_uppercase_preserved(self) -> None:
        self._run_case("RTY UJM\n")


if __name__ == "__main__":
    unittest.main()
