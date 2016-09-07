import unittest
from force_pep8.check_code import check_cell_code


valid_codes = [
"""def lol(inputs):
    return 5 * inputs + a

a = 5 + 2
lol(a + 5)
""",
"b = 5",
"listy = [1, 2, 3, 4]"
]


def valid_code(code):
    output = check_cell_code(code, test=False)
    return bool(output) is False


class TestPEP8Check(unittest.TestCase):
    def test_valid_code(self):
        for code in valid_codes:
            self.assertTrue(valid_code(code))

    def test_no_space_around_operator(self):
        self.assertFalse(valid_code("a=4"))
