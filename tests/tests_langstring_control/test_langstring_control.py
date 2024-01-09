import pytest

from langstring import Controller
from langstring import LangStringFlag


@pytest.mark.parametrize(
    "flag",
    [
        LangStringFlag.ENSURE_TEXT,
        LangStringFlag.ENSURE_ANY_LANG,
        LangStringFlag.ENSURE_VALID_LANG,
    ],
)
def test_default_flag_state(flag: LangStringFlag) -> None:
    """Test the default state of flags.

    :param flag: The LangStringFlag to check the default state for.
    """
    assert Controller.get_flag(LangStringFlag.ENSURE_TEXT)
    assert not Controller.get_flag(LangStringFlag.ENSURE_ANY_LANG)
    assert not Controller.get_flag(LangStringFlag.ENSURE_VALID_LANG)


def test_instantiation_of_langstringcontrol() -> None:
    """
    Test that instantiation of Controller raises a TypeError.

    This test ensures that Controller, being a static configuration manager, cannot be instantiated due to
    the NonInstantiable metaclass.

    :raises AssertionError: If Controller can be instantiated without raising a TypeError.
    """
    with pytest.raises(TypeError, match="Controller class cannot be instantiated."):
        Controller()


@pytest.mark.parametrize(
    "initial_state, new_state",
    [
        (False, True),
        (True, False),
    ],
)
def test_flag_state_persistence(initial_state: bool, new_state: bool) -> None:
    """
    Test the persistence of flag states after modification.

    This test verifies that once a flag's state is modified, it persists until explicitly changed again.

    :param initial_state: The initial state to set for a flag.
    :param new_state: The new state to set for the same flag.
    :raises AssertionError: If the flag state does not persist as expected.
    """
    flag = LangStringFlag.ENSURE_TEXT
    Controller.set_flag(flag, initial_state)
    assert Controller.get_flag(flag) == initial_state, "Initial flag state should persist"

    Controller.set_flag(flag, new_state)
    assert Controller.get_flag(flag) == new_state, "Modified flag state should persist"


def test_multiple_flag_modifications_integrity() -> None:
    """
    Test the integrity of flag states after multiple modifications.

    This test ensures that modifications to different flags do not interfere with each other's states.

    :raises AssertionError: If the state of any flag is not as expected after multiple modifications.
    """
    Controller.set_flag(LangStringFlag.ENSURE_TEXT, True)
    Controller.set_flag(LangStringFlag.ENSURE_ANY_LANG, False)
    Controller.set_flag(LangStringFlag.ENSURE_VALID_LANG, True)

    assert Controller.get_flag(LangStringFlag.ENSURE_TEXT), "ENSURE_TEXT flag should be True"
    assert not Controller.get_flag(LangStringFlag.ENSURE_ANY_LANG), "ENSURE_ANY_LANG flag should be False"
    assert Controller.get_flag(LangStringFlag.ENSURE_VALID_LANG), "ENSURE_VALID_LANG flag should be True"

    Controller.reset_flags_all()  # Reset flags to default after test


def test_flag_state_consistency_across_methods() -> None:
    """
    Test the consistency of flag states across different methods.

    This test checks if the flag states remain consistent when accessed through get_flag and get_flags methods.

    :raises AssertionError: If the flag states are inconsistent across different methods.
    """
    Controller.set_flag(LangStringFlag.ENSURE_TEXT, True)
    all_flags = Controller.get_flags()

    assert (
        Controller.get_flag(LangStringFlag.ENSURE_TEXT) == all_flags[LangStringFlag.ENSURE_TEXT]
    ), "Flag state should be consistent across get_flag and get_flags methods"

    Controller.reset_flags_all()  # Reset flags to default after test
