import pytest
from langstring import LangString


class FormatMapTestCase:
    def __init__(self, input_string: str, mapping: dict, lang: str):
        self.input_string = input_string
        self.mapping = mapping
        self.lang = lang
        self.expected_output = input_string.format_map(mapping)


format_map_test_cases = [
    FormatMapTestCase("Hello, {name}", {"name": "Alice"}, "en"),
    FormatMapTestCase("Value: {value}", {"value": 42}, "en"),
    FormatMapTestCase("Template string", {"key": [1, 2, 3]}, "en"),  # Non-primitive type as value
    FormatMapTestCase("Template string", [("key", "value")], "en"),  # List instead of dictionary
    FormatMapTestCase("Template string", 123, "en"),  # Integer instead of dictionary
    FormatMapTestCase("Template string", {complex(1, 2): "value"}, "en"),  # Complex number as key
    FormatMapTestCase("Template string", {slice(0, 5): "value"}, "en"),  # Slice object as key
    FormatMapTestCase("Template string", {"not": {"allowed": "value"}}, "en"),  # Nested dictionary
    FormatMapTestCase("Template string", {"key": lambda x: x}, "en"),  # Function as value
]


@pytest.mark.parametrize("test_case", format_map_test_cases)
def test_format_map(test_case: FormatMapTestCase):
    lang_string = LangString(test_case.input_string, test_case.lang)
    result = lang_string.format_map(test_case.mapping)
    assert isinstance(result, LangString), "Result should be a LangString instance"
    assert result.text == test_case.expected_output, "Format_map method failed"
    assert result.lang == test_case.lang, "Language tag should remain unchanged"
