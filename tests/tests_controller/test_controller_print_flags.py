import pytest

from langstring import Controller
from langstring import GlobalFlag
from langstring import LangStringFlag
from langstring import MultiLangStringFlag
from langstring import SetLangStringFlag

all_flags = (
    list(LangStringFlag.__members__.values())
    + list(SetLangStringFlag.__members__.values())
    + list(MultiLangStringFlag.__members__.values())
    + list(GlobalFlag.__members__.values())
)


def construct_expected_output():
    output = ""
    # Dynamically construct the expected output based on the actual order and default states
    for flag, state in Controller.flags.items():
        flag_class_name = flag.__class__.__name__
        default_state = "True" if state else "False"
        output += f"{flag_class_name}.{flag.name} = {default_state}\n"
    return output


def test_print_flags_default(capfd):
    Controller.print_flags()
    out, _ = capfd.readouterr()
    expected_output = construct_expected_output()
    assert out == expected_output, "Default flag settings should be printed correctly"


@pytest.mark.parametrize("flag", all_flags)
def test_print_flags_after_modification(capfd, flag):
    Controller.set_flag(flag, False)
    Controller.print_flags()
    out, _ = capfd.readouterr()
    expected_line = f"{flag.__class__.__name__}.{flag.name} = False"
    assert expected_line in out, "Modified flag settings should be printed correctly"


def test_print_flags_after_reset(capfd):
    Controller.set_flag(LangStringFlag.DEFINED_TEXT, False)
    Controller.reset_flags()
    Controller.print_flags()
    out, _ = capfd.readouterr()
    expected_output = construct_expected_output()
    assert out == expected_output, "Flag settings should be reset and printed correctly"
