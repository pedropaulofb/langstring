import pytest

from langstring import SetLangString


class SetLangStringOperationTestCase:
    def __init__(self, texts1, lang1, texts2, lang2):
        self.texts1 = texts1
        self.lang1 = lang1
        self.texts2 = texts2
        self.lang2 = lang2

    def run_test(self, method_name, strict=False):
        set_lang_string = SetLangString(texts=self.texts1, lang=self.lang1)
        other_set = SetLangString(texts=self.texts2, lang=self.lang2)
        method = getattr(set_lang_string, method_name)
        if strict is not None:
            return method(other_set, strict=strict)
        else:
            return method(other_set)


def calculate_expected_result(texts1, texts2, method_name):
    set1 = set(texts1)
    set2 = set(texts2)
    if method_name == "difference":
        return set1 - set2
    elif method_name == "intersection":
        return set1 & set2
    elif method_name == "union":
        return set1 | set2
    else:
        raise ValueError("Invalid method name")


operation_test_cases = [
    SetLangStringOperationTestCase({"a", "b", "c"}, "en", {"a", "b", "c"}, "en"),
    SetLangStringOperationTestCase({"a", "b"}, "en", {"a", "b", "c"}, "en"),
    SetLangStringOperationTestCase({"a", "b", "c"}, "en", {"b", "c"}, "en"),
    SetLangStringOperationTestCase({"a"}, "En", {"a", "b", "c"}, "en"),
    SetLangStringOperationTestCase({"a", "b", "c"}, "en", {"a"}, "en"),
    SetLangStringOperationTestCase({"a", "b"}, "En", {"c", "d"}, "en"),
    SetLangStringOperationTestCase(set(), "En", {"a", "b", "c"}, "en"),
    SetLangStringOperationTestCase({"a", "b", "c"}, "eN", set(), "en"),
    SetLangStringOperationTestCase(set(), "En", set(), "eN"),
    SetLangStringOperationTestCase({"a", "b", "c"}, "eN", {"a", "b", "c"}, "EN"),
    SetLangStringOperationTestCase({"a", "b"}, "en", {"c", "d"}, "en"),
    SetLangStringOperationTestCase({"привет", "мир"}, "ru", {"мир", "земля"}, "ru"),
    SetLangStringOperationTestCase({"こんにちは", "世界"}, "jp", {"世界", "地球"}, "jp"),
    SetLangStringOperationTestCase({"hello", "world"}, "en", {"world", "universe"}, "en"),
    SetLangStringOperationTestCase({"1", "2", "3"}, "en", {"4", "5", "6"}, "EN"),
    # Sets with overlapping elements, same language
    SetLangStringOperationTestCase({"a", "b", "c"}, "en", {"b", "c", "d"}, "en"),
    SetLangStringOperationTestCase({"m", "n"}, "en", {"n", "o", "p"}, "en"),
    # Sets with non-overlapping elements, same language
    SetLangStringOperationTestCase({"a", "b"}, "en", {"c", "d", "e"}, "en"),
    SetLangStringOperationTestCase({"x", "y"}, "en", {"z", "w"}, "en"),
    # Sets with mixed character types
    SetLangStringOperationTestCase({"1", "2", "3"}, "en", {"3", "4", "5"}, "en"),
    SetLangStringOperationTestCase({"@", "#", "$"}, "en", {"$", "%", "^"}, "en"),
    # Sets with special characters
    SetLangStringOperationTestCase({"!", "@", "#"}, "en", {"#", "$", "%"}, "en"),
    SetLangStringOperationTestCase({"&", "*"}, "en", {"*", "("}, "en"),
    # Sets with mixed alphabets and special characters
    SetLangStringOperationTestCase({"a", "#", "c"}, "en", {"#", "d", "e"}, "en"),
    SetLangStringOperationTestCase({"1", "b", "@"}, "en", {"@", "2", "c"}, "en"),
    # Sets with emojis
    SetLangStringOperationTestCase({"😊", "😂", "😜"}, "en", {"😂", "😎"}, "en"),
    SetLangStringOperationTestCase({"🍏", "🍎"}, "en", {"🍎", "🍐"}, "en"),
    # Sets with mixed content
    SetLangStringOperationTestCase({"hello", "😊", "world"}, "en", {"😊", "🌍"}, "en"),
    SetLangStringOperationTestCase({"123", "abc", "😜"}, "en", {"😜", "def", "456"}, "en"),
    # Sets with case sensitivity
    SetLangStringOperationTestCase({"Hello", "World"}, "en", {"hello", "world"}, "en"),
    SetLangStringOperationTestCase({"APPLE", "BANANA"}, "en", {"apple", "banana"}, "en"),
    # Sets with spaces
    SetLangStringOperationTestCase({" hello ", " world"}, "en", {"hello", "world"}, "en"),
    SetLangStringOperationTestCase({" good ", " morning"}, "en", {"good", "morning"}, "en"),
    # Sets with numeric strings
    SetLangStringOperationTestCase({"123", "456"}, "en", {"456", "789"}, "en"),
    SetLangStringOperationTestCase({"100", "200"}, "en", {"300", "200"}, "en"),
    # Sets with empty strings and spaces
    SetLangStringOperationTestCase({"", " "}, "en", {" ", "  "}, "en"),
    SetLangStringOperationTestCase({"   ", ""}, "en", {"", "    "}, "en"),
    # More complex sets
    SetLangStringOperationTestCase({"apple", "orange", "banana"}, "en", {"banana", "grape", "melon"}, "en"),
    SetLangStringOperationTestCase({"cat", "dog", "bird"}, "en", {"bird", "fish", "hamster"}, "en"),
]


@pytest.mark.parametrize("test_case", operation_test_cases)
@pytest.mark.parametrize("method_name", ["difference", "intersection", "union"])
@pytest.mark.parametrize("strict", [None, False, True])
def test_setlangstring_operation_methods(test_case, method_name, strict):
    result_set_lang_string = test_case.run_test(method_name, strict)
    expected_result = calculate_expected_result(test_case.texts1, test_case.texts2, method_name)
    assert (
        set(result_set_lang_string.texts) == expected_result
    ), f"Failed {method_name} for texts1={test_case.texts1} and texts2={test_case.texts2} with strict={strict}"


@pytest.mark.parametrize("test_case", operation_test_cases)
@pytest.mark.parametrize("method_name", ["difference", "intersection", "union"])
def test_setlangstring_operation_methods_with_different_lang(test_case, method_name):
    # Modify lang2 to be different from lang1
    test_case.lang2 = "different_lang" if test_case.lang1 != "different_lang" else "another_lang"

    # Run the test and expect a ValueError
    with pytest.raises(ValueError):
        test_case.run_test(method_name, strict=False)


@pytest.mark.parametrize("test_case", operation_test_cases)
@pytest.mark.parametrize("method_name", ["difference", "intersection", "union"])
def test_setlangstring_operation_methods_with_set(test_case, method_name):
    # Use texts1 and lang1 to build a SetLangString
    set_lang_string = SetLangString(texts=test_case.texts1, lang=test_case.lang1)

    # Use texts2 as a regular set
    regular_set = test_case.texts2

    # Run the test and expect the operation to succeed
    method = getattr(set_lang_string, method_name)
    result_set_lang_string = method(regular_set)  # No strict parameter needed as regular set is used
    expected_result = calculate_expected_result(test_case.texts1, regular_set, method_name)
    assert (
        set(result_set_lang_string.texts) == expected_result
    ), f"Failed {method_name} for texts1={test_case.texts1} and texts2={regular_set}"
