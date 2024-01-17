import pytest
from langstring import LangString


class StringTestCase:
    def __init__(self, string):
        self.string = string
        self.expected_results = self._generate_expected_results()

    def _generate_expected_results(self):
        results = {
            "isalnum": self.string.isalnum(),
            "isalpha": self.string.isalpha(),
            "isascii": self.string.isascii(),
            "isdecimal": self.string.isdecimal(),
            "isdigit": self.string.isdigit(),
            "isidentifier": self.string.isidentifier(),
            "islower": self.string.islower(),
            "isnumeric": self.string.isnumeric(),
            "isprintable": self.string.isprintable(),
            "isspace": self.string.isspace(),
            "istitle": self.string.istitle(),
            "isupper": self.string.isupper(),
        }
        return results


test_cases = [
    StringTestCase("Hello123"),
    StringTestCase("Hello 123"),
    StringTestCase("123"),
    StringTestCase("こんにちは"),
    StringTestCase(""),
    StringTestCase("123abc"),
    StringTestCase("123.45"),
    StringTestCase("   "),
    StringTestCase("HelloWorld"),
    StringTestCase("HELLO"),
    StringTestCase("hello"),
    StringTestCase("Hello World"),
    StringTestCase("1234567890"),
    StringTestCase("こんにちは123"),
    StringTestCase("😊😊😊"),
    StringTestCase("123\n"),
    StringTestCase("Title Case"),
    StringTestCase("123ABC"),
    StringTestCase("abc_def"),
    StringTestCase("1234567890abcdefABCDEF"),
    StringTestCase("Γειά σου Κόσμε"),
    StringTestCase("1234_5678"),
    StringTestCase("1234567890\n"),
    StringTestCase("1234567890\t"),
    StringTestCase("1234567890\r"),
    StringTestCase("1234567890\f"),
    StringTestCase("1234567890\v"),
    StringTestCase("1234567890 "),
    StringTestCase(" 1234567890"),
    StringTestCase("1234567890a"),
    StringTestCase("a1234567890"),
    StringTestCase("1234567890a "),
    StringTestCase(" 1234567890a"),
    StringTestCase("1234567890a\n"),
    StringTestCase("1234567890a\t"),
    StringTestCase("1234567890a\r"),
    StringTestCase("1234567890a\f"),
    StringTestCase("1234567890a\v"),
    StringTestCase("1234567890a "),
]

@pytest.mark.parametrize("test_case", test_cases)
def test_isalnum(test_case):
    lang_string = LangString(test_case.string, "en")
    assert lang_string.isalnum() == test_case.expected_results["isalnum"]

@pytest.mark.parametrize("test_case", test_cases)
def test_isalpha(test_case):
    lang_string = LangString(test_case.string, "en")
    assert lang_string.isalpha() == test_case.expected_results["isalpha"]
