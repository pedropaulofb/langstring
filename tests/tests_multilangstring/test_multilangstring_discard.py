import pytest

from langstring import Controller
from langstring import LangString
from langstring import MultiLangString
from langstring import MultiLangStringFlag
from langstring import SetLangString


@pytest.mark.parametrize(
    "arg, expected_result",
    [
        (
            LangString("Bonjour", "fr"),
            {"en": {"Hello", "World"}, "fr": set(), "es": {"Hola", "Adios"}},
        ),  # Discard LangString
        (
            SetLangString({"Hola"}, "es"),
            {"en": {"Hello", "World"}, "fr": {"Bonjour"}, "es": {"Adios"}},
        ),  # Discard SetLangString
        (
            SetLangString({"Hola", "Adios"}, "es"),
            {"en": {"Hello", "World"}, "fr": {"Bonjour"}, "es": set()},
        ),  # Discard SetLangString
        (("Adios", "es"), {"en": {"Hello", "World"}, "fr": {"Bonjour"}, "es": {"Hola"}}),  # Discard tuple
    ],
)
def test_discard_various_args_off(arg, expected_result):
    """
    Test the `discard` method with various types of arguments to ensure correct functionality across supported input types.

    :param arg: Argument to discard, which could be a string, LangString, SetLangString, or tuple.
    :param expected_result: Expected state of the MultiLangString instance after the discard operation.
    """
    mls = MultiLangString({"en": {"Hello", "World"}, "fr": {"Bonjour"}, "es": {"Hola", "Adios"}})
    mls.discard(arg)
    assert mls.mls_dict == expected_result, f"Expected dictionary did not match after discarding {arg}."


@pytest.mark.parametrize(
    "arg, expected_result",
    [
        (
            LangString("Bonjour", "fr"),
            {"en": {"Hello", "World"}, "es": {"Hola", "Adios"}},
        ),  # Discard LangString
        (
            SetLangString({"Hola"}, "es"),
            {"en": {"Hello", "World"}, "fr": {"Bonjour"}, "es": {"Adios"}},
        ),  # Discard SetLangString
        (
            SetLangString({"Hola", "Adios"}, "es"),
            {"en": {"Hello", "World"}, "fr": {"Bonjour"}},
        ),  # Discard SetLangString
        (("Adios", "es"), {"en": {"Hello", "World"}, "fr": {"Bonjour"}, "es": {"Hola"}}),  # Discard tuple
    ],
)
def test_discard_various_args_on(arg, expected_result):
    """
    Test the `discard` method with various types of arguments to ensure correct functionality across supported input types.

    :param arg: Argument to discard, which could be a string, LangString, SetLangString, or tuple.
    :param expected_result: Expected state of the MultiLangString instance after the discard operation.
    """
    Controller.set_flag(MultiLangStringFlag.CLEAR_EMPTY_LANG, True)
    mls = MultiLangString({"en": {"Hello", "World"}, "fr": {"Bonjour"}, "es": {"Hola", "Adios"}})
    mls.discard(arg)
    assert mls.mls_dict == expected_result, f"Expected dictionary did not match after discarding {arg}."


def test_discard_with_invalid_type():
    """
    Test the `discard` method raises a TypeError when an invalid argument type is passed.
    """
    mls = MultiLangString({"en": {"Hello"}})
    with pytest.raises(TypeError, match="Argument '.+' must be of type"):
        mls.discard(123)  # Invalid type argument


@pytest.mark.parametrize(
    "arg, expected_result, test_case_description",
    [
        (
            SetLangString(set(), "en"),
            {"en": {"Hello", "World"}, "fr": {"Bonjour"}, "es": {"Hola", "Adios"}},
            "Discarding empty SetLangString does nothing",
        ),
    ],
)
def test_discard_edge_cases(arg, expected_result, test_case_description):
    """
    Test the `discard` method with edge cases like None, empty string, and empty SetLangString.

    :param arg: Argument to discard, could be None, an empty string, or an empty SetLangString.
    :param expected_result: Expected state of the MultiLangString instance after the discard operation.
    :param test_case_description: Description of the test case being executed.
    """
    mls = MultiLangString({"en": {"Hello", "World"}, "fr": {"Bonjour"}, "es": {"Hola", "Adios"}})
    mls.discard(arg)
    assert mls.mls_dict == expected_result, f"After {test_case_description}, expected dictionary did not match."


def test_discard_with_none():
    """
    Test that passing None as an argument to `discard` raises a TypeError.
    """
    mls = MultiLangString({"en": {"Hello", "World"}, "fr": {"Bonjour"}, "es": {"Hola", "Adios"}})
    with pytest.raises(TypeError, match="Argument 'None' must be of type"):
        mls.discard(None)  # Passing None should raise TypeError


# Test case for discarding a non-empty string in a non-default language when the CLEAR_EMPTY_LANG flag is off.
(
    LangString("World", "en"),
    {"en": {"Hello"}, "fr": {"Bonjour"}, "es": {"Hola", "Adios"}},
    "Discarding 'World' from 'en' with CLEAR_EMPTY_LANG off",
),

# Test case for discarding a non-empty SetLangString in a non-default language when the CLEAR_EMPTY_LANG flag is off.
(
    SetLangString({"Adios"}, "es"),
    {"en": {"Hello", "World"}, "fr": {"Bonjour"}, "es": {"Hola"}},
    "Discarding 'Adios' from 'es' with CLEAR_EMPTY_LANG off",
),

# Test case for discarding an existing tuple in a non-default language when the CLEAR_EMPTY_LANG flag is off.
(
    ("Hola", "es"),
    {"en": {"Hello", "World"}, "fr": {"Bonjour"}, "es": {"Adios"}},
    "Discarding tuple ('Hola', 'es') with CLEAR_EMPTY_LANG off",
),


# Test for discarding with None, expecting a TypeError, to specifically catch incorrect argument types.
def test_discard_with_none_raises_error():
    """
    Test that passing None as an argument to `discard` method raises a TypeError, ensuring robust input validation.
    """
    mls = MultiLangString({"en": {"Hello", "World"}, "fr": {"Bonjour"}, "es": {"Hola", "Adios"}})
    with pytest.raises(TypeError, match="Argument 'None' must be of type"):
        mls.discard(None)  # Passing None should raise TypeError


@pytest.mark.parametrize(
    "initial_contents, discarding_mls_contents, expected_result, description",
    [
        # mls1 has exactly mls2
        (
            {"en": {"Hello", "World"}, "fr": {"Bonjour"}},
            {"en": {"Hello", "World"}, "fr": {"Bonjour"}},
            {"en": set(), "fr": set()},
            "mls1 has exactly mls2",
        ),
        # mls1 has some of mls2
        (
            {"en": {"Hello", "World", "Universe"}, "fr": {"Bonjour", "Salut"}},
            {"en": {"World"}, "fr": {"Bonjour"}},
            {"en": {"Hello", "Universe"}, "fr": {"Salut"}},
            "mls1 has some of mls2",
        ),
        # mls1 has all mls2 and more
        (
            {"en": {"Hello", "World"}, "fr": {"Bonjour", "Salut"}},
            {"en": {"World"}},
            {"en": {"Hello"}, "fr": {"Bonjour", "Salut"}},
            "mls1 has all mls2 and more",
        ),
        # mls1 has none of mls2
        ({"en": {"Hello"}}, {"fr": {"Bonjour"}}, {"en": {"Hello"}}, "mls1 has none of mls2"),
    ],
)
def test_discard_multilangstring_various_scenarios(
    initial_contents, discarding_mls_contents, expected_result, description
):
    """
    Test the `discard` method when receiving a MultiLangString as an argument across various scenarios.

    :param initial_contents: Initial contents of the MultiLangString instance.
    :param discarding_mls_contents: Contents of the MultiLangString to be discarded.
    :param expected_result: Expected contents of the MultiLangString after the discard operation.
    :param description: Description of the test case.
    """
    mls_initial = MultiLangString(initial_contents)
    mls_discarding = MultiLangString(discarding_mls_contents)
    mls_initial.discard(mls_discarding)
    assert (
        mls_initial.mls_dict == expected_result
    ), f"After discarding {description}, expected dictionary did not match."


@pytest.mark.parametrize(
    "initial_contents, discarding_mls_contents, expected_result, description",
    [
        # mls1 has exactly mls2
        (
            {"en": {"Hello", "World"}, "fr": {"Bonjour"}},
            {"en": {"Hello", "World"}, "fr": {"Bonjour"}},
            {},
            "mls1 has exactly mls2",
        ),
        # mls1 has all mls2 and more
        (
            {"en": {"Hello", "World"}, "fr": {"Bonjour", "Salut"}},
            {"en": {"Hello", "World"}},
            {"fr": {"Bonjour", "Salut"}},
            "mls1 has all mls2 and more",
        ),
    ],
)
def test_discard_multilangstring_various_scenarios_on(
    initial_contents, discarding_mls_contents, expected_result, description
):
    """
    Test the `discard` method when receiving a MultiLangString as an argument across various scenarios.

    :param initial_contents: Initial contents of the MultiLangString instance.
    :param discarding_mls_contents: Contents of the MultiLangString to be discarded.
    :param expected_result: Expected contents of the MultiLangString after the discard operation.
    :param description: Description of the test case.
    """
    Controller.set_flag(MultiLangStringFlag.CLEAR_EMPTY_LANG, True)
    mls_initial = MultiLangString(initial_contents)
    mls_discarding = MultiLangString(discarding_mls_contents)
    mls_initial.discard(mls_discarding)
    assert (
        mls_initial.mls_dict == expected_result
    ), f"After discarding {description}, expected dictionary did not match."
