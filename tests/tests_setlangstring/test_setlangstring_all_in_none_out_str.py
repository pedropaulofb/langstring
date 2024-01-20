import pytest

from langstring import SetLangString


class SetLangStringOperationTestCase:
    def __init__(self, texts, lang):
        self.texts = texts
        self.lang = lang

    def run_test(self, method_name):
        set_lang_string = SetLangString(texts=self.texts, lang=self.lang)
        method = getattr(set_lang_string, method_name)
        if method_name == "pop" and not self.texts:
            with pytest.raises(KeyError, match="pop from an empty set"):
                return method()
            return "KeyError"
        else:
            return method()


# Define test cases
operation_test_cases = [
    SetLangStringOperationTestCase({"a", "b", "c"}, "en"),
    SetLangStringOperationTestCase({"x", "y", "z"}, "en"),
    SetLangStringOperationTestCase({"1", "2", "3"}, "en"),
    SetLangStringOperationTestCase({"apple", "banana", "cherry"}, "en"),
    SetLangStringOperationTestCase({"hello", "world"}, "en"),
    SetLangStringOperationTestCase({"😊", "😂", "😜"}, "en"),
    SetLangStringOperationTestCase({"🍏", "🍎"}, "en"),
    SetLangStringOperationTestCase({"HELLO", "WORLD"}, "en"),
    SetLangStringOperationTestCase({" ", "  "}, "en"),
    SetLangStringOperationTestCase(set(), "en"),  # Empty set
    # Basic cases with different sizes
    SetLangStringOperationTestCase({"a", "b", "c"}, "en"),
    SetLangStringOperationTestCase({"x", "y"}, "en"),
    SetLangStringOperationTestCase({"1"}, "en"),
    SetLangStringOperationTestCase(set(), "en"),  # Empty set
    # Cases with mixed character types
    SetLangStringOperationTestCase({"1", "a", "@"}, "en"),
    SetLangStringOperationTestCase({"#", "$", "%", "&"}, "en"),
    # Cases with special characters and emojis
    SetLangStringOperationTestCase({"😊", "😂", "😜"}, "en"),
    SetLangStringOperationTestCase({"🍏", "🍎", "🍐"}, "en"),
    SetLangStringOperationTestCase({"!", "@", "#"}, "en"),
    # Cases with numeric strings
    SetLangStringOperationTestCase({"123", "456", "789"}, "en"),
    SetLangStringOperationTestCase({"100", "200", "300"}, "en"),
    # Cases with spaces and empty strings
    SetLangStringOperationTestCase({" ", "  ", "   "}, "en"),
    SetLangStringOperationTestCase({"", " ", "  "}, "en"),
    # Cases with mixed alphabets
    SetLangStringOperationTestCase({"apple", "banana", "cherry"}, "en"),
    SetLangStringOperationTestCase({"cat", "dog", "bird"}, "en"),
    # Cases with upper and lower case
    SetLangStringOperationTestCase({"Hello", "World"}, "en"),
    SetLangStringOperationTestCase({"APPLE", "BANANA", "CHERRY"}, "en"),
    # Cases with non-English alphabets
    SetLangStringOperationTestCase({"привет", "мир"}, "ru"),
    SetLangStringOperationTestCase({"こんにちは", "世界"}, "jp"),
    # Complex mixed content cases
    SetLangStringOperationTestCase({"hello", "world", "😊"}, "en"),
    SetLangStringOperationTestCase({"123", "abc", "😜"}, "en"),
    SetLangStringOperationTestCase({"Hello", "123", "🍏"}, "en"),
    SetLangStringOperationTestCase({"hello", "привет", "こんにちは"}, "en"),
    SetLangStringOperationTestCase(
        {"This is a very long string to test the handling of large elements within the SetLangString class"}, "en"
    ),
    SetLangStringOperationTestCase({"string", "String", "strIng"}, "en"),
    SetLangStringOperationTestCase({"√", "π", "Ω"}, "en"),
    SetLangStringOperationTestCase({"Line1\nLine2", "Tab\tSeparated"}, "en"),
]


@pytest.mark.parametrize("test_case", operation_test_cases)
@pytest.mark.parametrize("method_name", ["pop", "__repr__", "__str__"])
def test_setlangstring_operation_methods(test_case, method_name):
    result = test_case.run_test(method_name)
    if method_name == "pop":
        if test_case.texts:
            assert result in test_case.texts, f"Failed {method_name} for texts={test_case.texts}"
        else:
            assert result == "KeyError", "Expected KeyError for popping from an empty set"
    else:
        assert isinstance(result, str), f"Failed {method_name} for texts={test_case.texts}"
