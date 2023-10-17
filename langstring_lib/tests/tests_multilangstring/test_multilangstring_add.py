import pytest

from langstring_lib.langstring import LangString
from langstring_lib.multilangstring import MultiLangString


def test_add_langstring():
    mls = MultiLangString()
    ls = LangString("Hello", "en")
    mls.add(ls)
    assert len(mls.langstrings) == 1
    assert mls.get_langstring("en") == ["Hello"]


def test_add_duplicate_langstring_warn():
    mls = MultiLangString(control="BLOCK_WARN")
    ls1 = LangString("Hello", "en")
    ls2 = LangString("Hi", "en")
    with pytest.warns(UserWarning, match=r".*LangString with language tag 'en' already exists.*"):
        mls.add(ls1)
        mls.add(ls2)


def test_add_duplicate_langstring_error():
    mls = MultiLangString(control="BLOCK_ERROR")
    ls1 = LangString("Hello", "en")
    ls2 = LangString("Hi", "en")
    with pytest.raises(ValueError, match=r".*LangString with language tag 'en' already exists.*"):
        mls.add(ls1)
        mls.add(ls2)
