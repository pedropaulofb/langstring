from langstring import Controller


def test_print_flags_outputs_current_flag_states(capsys):
    """
    Test if the print_flags method correctly outputs the current states of all flags to the console.
    """
    # Call the method and capture the output
    Controller.print_flags()
    captured = capsys.readouterr()

    # Check if the output contains the correct information
    expected_output = "MultiLangStringFlag.DEFINED_TEXT = True\n" "MultiLangStringFlag.VALID_LANG = False\n"
    assert captured.out == expected_output, "print_flags should output the current states of all flags correctly"
