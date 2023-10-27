from langstring.langstring import LangString
from langstring.multilangstring import MultiLangString


def test_remove_langstring():
    mls = MultiLangString()
    ls = LangString("Hello", "en")
    mls.add(ls)
    assert len(mls.langstrings) == 1
    assert mls.remove_langstring(ls)
    assert len(mls.langstrings) == 0


def test_remove_langstring_not_found():
    mls = MultiLangString()
    ls = LangString("Hello", "en")
    assert not mls.remove_langstring(ls)
