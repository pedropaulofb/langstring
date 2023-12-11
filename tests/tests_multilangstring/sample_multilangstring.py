"""This module provides utility functions for creating sample MultiLangString objects for testing purposes.

The primary function in this module is `create_sample_multilangstring`, which returns a MultiLangString object
populated with example `LangString` entries in English, French, and German.
"""
from langstring.langstring import LangString
from langstring.multilangstring import MultiLangString


def create_sample_multilangstring() -> MultiLangString:
    """Create a sample MultiLangString for testing purposes.

    :return: A sample MultiLangString.
    :rtype: MultiLangString
    """
    langstring_en = LangString("Hello", "en")
    langstring_fr = LangString("Bonjour", "fr")
    langstring_de = LangString("Hallo", "de")

    return MultiLangString(langstring_en, langstring_fr, langstring_de, control="ALLOW")
