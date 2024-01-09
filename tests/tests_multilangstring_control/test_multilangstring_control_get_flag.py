import pytest

from langstring import Controller
from langstring import MultiLangStringFlag


@pytest.mark.parametrize(
    "flag, expected_state",
    [
        (MultiLangStringFlag.ENSURE_TEXT, True),
        (MultiLangStringFlag.ENSURE_VALID_LANG, False),
    ],
)
def test_get_flag_returns_correct_initial_state(flag, expected_state):
    """
    Test if the get_flag method returns the correct initial state for each flag.

    :param flag: The flag to be tested.
    :param expected_state: The expected state of the flag.
    """
    assert (
        Controller.get_flag(flag) == expected_state
    ), f"get_flag should return {expected_state} for {flag.name} initially"


@pytest.mark.parametrize(
    "flag, state_to_set",
    [
        (MultiLangStringFlag.ENSURE_TEXT, False),
        (MultiLangStringFlag.ENSURE_VALID_LANG, True),
    ],
)
def test_get_flag_reflects_set_flag_state(flag, state_to_set):
    """
    Test if the get_flag method reflects the state set by set_flag method.

    :param flag: The flag to be tested.
    :param state_to_set: The state to set for the flag.
    """
    Controller.set_flag(flag, state_to_set)
    assert (
        Controller.get_flag(flag) == state_to_set
    ), f"get_flag should return {state_to_set} for {flag.name} after setting it"


@pytest.mark.parametrize("invalid_flag", [123, "ENSURE_TEXT", None, 5.5])
def test_get_flag_with_invalid_flag_type_raises_type_error(invalid_flag):
    """
    Test if the get_flag method raises TypeError when an invalid flag type is passed.

    :param invalid_flag: The invalid flag to test.
    """
    with pytest.raises(TypeError, match="Invalid flag"):
        Controller.get_flag(invalid_flag)


def test_get_flag_with_unrecognized_flag_raises_type_error():
    """
    Test if the get_flag method raises TypeError when an unrecognized flag is passed.
    """

    class FakeFlag:
        pass

    fake_flag = FakeFlag()
    with pytest.raises(TypeError, match="Invalid flag"):
        Controller.get_flag(fake_flag)
