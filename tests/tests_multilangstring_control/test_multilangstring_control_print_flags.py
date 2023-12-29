from langstring import MultiLangStringControl
from langstring import MultiLangStringFlag


def test_print_flags_outputs_current_flag_states(capsys):
    """
    Test if the print_flags method correctly outputs the current states of all flags to the console.
    """
    # Set a known state for a flag
    MultiLangStringControl.set_flag(MultiLangStringFlag.ENSURE_ANY_LANG, True)

    # Call the method and capture the output
    MultiLangStringControl.print_flags()
    captured = capsys.readouterr()

    # Check if the output contains the correct information
    expected_output = (
        "MultiLangStringFlag.ENSURE_TEXT = True\n"
        "MultiLangStringFlag.ENSURE_ANY_LANG = True\n"
        "MultiLangStringFlag.ENSURE_VALID_LANG = False\n"
    )
    assert captured.out == expected_output, "print_flags should output the current states of all flags correctly"
