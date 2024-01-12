import pytest

from langstring import Controller
from langstring import MultiLangStringFlag


def test_set_flag_updates_flag_state():
    """
    Test if the set_flag method correctly updates the state of a specified flag.
    """
    # Set a flag to a new state
    Controller.set_flag(MultiLangStringFlag.ENSURE_ANY_LANG, True)

    # Check if the flag's state is updated
    assert (
        Controller.get_flag(MultiLangStringFlag.ENSURE_ANY_LANG) is True
    ), "set_flag should correctly update the state of ENSURE_ANY_LANG to True"


@pytest.mark.parametrize(
    "flag, state",
    [
        (MultiLangStringFlag.DEFINED_TEXT, False),
        (MultiLangStringFlag.VALID_LANG, True),
    ],
)
def test_set_flag_with_various_flags_and_states(flag, state):
    """
    Test if the set_flag method correctly updates various flags to different states.

    :param flag: The flag to be tested.
    :param state: The state to set for the flag.
    """
    Controller.set_flag(flag, state)
    assert Controller.get_flag(flag) == state, f"set_flag should set {flag.name} to {state}"


@pytest.mark.parametrize("invalid_flag", [123, "DEFINED_TEXT", None, 5.5])
def test_set_flag_with_invalid_flag_type_raises_type_error(invalid_flag):
    """
    Test if the set_flag method raises TypeError when an invalid flag type is passed.

    :param invalid_flag: The invalid flag to test.
    """
    with pytest.raises(TypeError, match="Invalid flag"):
        Controller.set_flag(invalid_flag, True)


@pytest.mark.parametrize("invalid_state", ["True", 1, None, []])
def test_set_flag_with_invalid_state_type_raises_type_error(invalid_state):
    """
    Test if the set_flag method raises TypeError when an invalid state type is passed.

    :param invalid_state: The invalid state to test.
    """
    with pytest.raises(TypeError, match="Invalid state"):
        Controller.set_flag(MultiLangStringFlag.DEFINED_TEXT, invalid_state)


def test_set_flag_with_unrecognized_flag_raises_type_error():
    """
    Test if the set_flag method raises TypeError when an unrecognized flag is passed.
    """

    class FakeFlag:
        pass

    fake_flag = FakeFlag()
    with pytest.raises(TypeError, match="Invalid flag"):
        Controller.set_flag(fake_flag, True)
