from langstring import Controller
from langstring import LangStringFlag


def test_print_flags_default(capfd) -> None:
    """
    Test the output of print_flags method with default flag settings.

    :param capfd: Pytest fixture to capture file descriptors.
    """
    Controller.print_flags()
    out, _ = capfd.readouterr()
    expected_output = (
        "LangStringFlag.ENSURE_TEXT = True\n"
        "LangStringFlag.ENSURE_ANY_LANG = False\n"
        "LangStringFlag.ENSURE_VALID_LANG = False\n"
    )
    assert out == expected_output, "Default flag settings should be printed correctly"


def test_print_flags_after_modification(capfd) -> None:
    """
    Test the output of print_flags method after modifying flag settings.

    :param capfd: Pytest fixture to capture file descriptors.
    """
    Controller.set_flag(LangStringFlag.ENSURE_TEXT, False)
    Controller.set_flag(LangStringFlag.ENSURE_ANY_LANG, True)
    Controller.print_flags()
    out, _ = capfd.readouterr()
    expected_output = (
        "LangStringFlag.ENSURE_TEXT = False\n"
        "LangStringFlag.ENSURE_ANY_LANG = True\n"
        "LangStringFlag.ENSURE_VALID_LANG = False\n"
    )
    assert out == expected_output, "Modified flag settings should be printed correctly"
    Controller.reset_flags_all()  # Reset flags to default after test


def test_print_flags_after_reset(capfd) -> None:
    """
    Test the output of print_flags method after resetting flags to default.

    :param capfd: Pytest fixture to capture file descriptors.
    """
    Controller.set_flag(LangStringFlag.ENSURE_TEXT, False)
    Controller.reset_flags_all()
    Controller.print_flags()
    out, _ = capfd.readouterr()
    expected_output = (
        "LangStringFlag.ENSURE_TEXT = True\n"
        "LangStringFlag.ENSURE_ANY_LANG = False\n"
        "LangStringFlag.ENSURE_VALID_LANG = False\n"
    )
    assert out == expected_output, "Flag settings should be reset and printed correctly"
