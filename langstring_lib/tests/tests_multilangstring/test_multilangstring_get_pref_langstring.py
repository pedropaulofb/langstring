from langstring_lib.langstring import LangString
from langstring_lib.multilangstring import MultiLangString


def test_get_pref_langstring():
    mls = MultiLangString()
    ls = LangString("Hello", "en")
    mls.add(ls)
    assert mls.get_pref_langstring() == ["Hello"]


def test_get_pref_langstring_none():
    mls = MultiLangString()
    assert mls.get_pref_langstring() is None