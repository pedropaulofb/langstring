from langstring.langstring import LangString
from langstring.multilangstring import MultiLangString


def test_to_string_list():
    mls = MultiLangString()
    ls1 = LangString("Hello", "en")
    ls2 = LangString("Bonjour", "fr")
    mls.add(ls1)
    mls.add(ls2)
    expected = ["'Hello'@en", "'Bonjour'@fr"]
    assert mls.to_string_list() == expected
