import pytest

from langstring import Controller
from langstring import MultiLangString
from langstring import MultiLangStringFlag


@pytest.mark.parametrize(
    "text, flag_state, expected_exception", [("", True, ValueError), ("Hello", True, None), ("", False, None)]
)
def test_validate_ensure_text(text, flag_state, expected_exception):
    """
    Test the _validate_ensure_text method under different flag settings and text inputs.

    :param text: The text to test.
    :param flag_state: The state of the DEFINED_TEXT flag.
    :param expected_exception: The expected exception, if any.
    """
    Controller.set_flag(MultiLangStringFlag.DEFINED_TEXT, flag_state)
    mls = MultiLangString()

    # Directly accessing the protected method for testing purposes
    if expected_exception:
        with pytest.raises(expected_exception, match="cannot receive empty string"):
            mls._validate_ensure_text(text)
    else:
        mls._validate_ensure_text(text)  # Should not raise an exception
