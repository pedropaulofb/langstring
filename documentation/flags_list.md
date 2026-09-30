# Available Flags

<!-- TOC -->
* [Available Flags](#available-flags)
  * [GlobalFlag](#globalflag)
  * [LangStringFlag](#langstringflag)
  * [SetLangStringFlag](#setlangstringflag)
  * [MultiLangStringFlag](#multilangstringflag)
<!-- TOC -->

`VALID_LANG` is disabled by default. Install `langstring[langcodes]` and enable the applicable class flag or `GlobalFlag.VALID_LANG` to validate tags on the library's validation paths. Invalid tags then raise `ValueError`. Enabling a flag does not revalidate existing objects, and direct edits to exposed collections can bypass validation.

If importing `langcodes` fails while validation is requested, the default is to emit `UserWarning` and skip validation. Set `GlobalFlag.ENFORCE_EXTRA_DEPEND` to `True` to raise `ImportError` instead. It does not enable validation by itself. Flags are process-wide settings. See the [README validation example](../README.md#optional-dependencies).

## GlobalFlag

- **DEFINED_LANG**: Ensures that a non-empty string is used for the 'lang' field of all classes.
- **DEFINED_TEXT**: Ensures that a non-empty string is used for the 'text' field of all classes.
- **ENFORCE_EXTRA_DEPEND**: Raises `ImportError` if importing `langcodes` fails when `VALID_LANG` requests validation; otherwise the default is a warning and skipped validation.
- **LOWERCASE_LANG**: Converts all language codes to lowercase.
- **METHODS_MATCH_TYPES**: Ensures that methods match the expected types for arguments and return values.
- **PRINT_WITH_LANG**: Includes language tags when printing multilingual text.
- **PRINT_WITH_QUOTES**: Wraps text entries in quotes when printing multilingual text.
- **STRIP_LANG**: Removes leading and trailing whitespace from language codes.
- **STRIP_TEXT**: Removes leading and trailing whitespace from text entries.
- **VALID_LANG**: Requests language-tag validation for all classes, subject to the dependency and validation-path conditions above.

## LangStringFlag

- **DEFINED_LANG**: Ensures that a non-empty string is used for the 'lang' field of a LangString.
- **DEFINED_TEXT**: Ensures that a non-empty string is used for the 'text' field of a LangString.
- **LOWERCASE_LANG**: Converts all language codes to lowercase within a LangString.
- **METHODS_MATCH_TYPES**: Ensures that methods match the expected types for arguments and return values within
                               a LangString.
- **PRINT_WITH_LANG**: Includes language tags when printing a LangString.
- **PRINT_WITH_QUOTES**: Wraps text entries in quotes when printing a LangString.
- **STRIP_LANG**: Removes leading and trailing whitespace from language codes within a LangString.
- **STRIP_TEXT**: Removes leading and trailing whitespace from text entries within a LangString.
- **VALID_LANG**: Requests language-tag validation for a LangString, subject to the dependency and validation-path conditions above.

## SetLangStringFlag

- **DEFINED_LANG**: Ensures that a non-empty string is used for the 'lang' field of a SetLangString.
- **DEFINED_TEXT**: Ensures that a non-empty string is used for the 'text' field of a SetLangString.
- **LOWERCASE_LANG**: Converts all language codes to lowercase within a SetLangString.
- **METHODS_MATCH_TYPES**: Ensures that methods match the expected types for arguments and return values within
                               a SetLangString.
- **PRINT_WITH_LANG**: Includes language tags when printing a SetLangString.
- **PRINT_WITH_QUOTES**: Wraps text entries in quotes when printing a SetLangString.
- **STRIP_LANG**: Removes leading and trailing whitespace from language codes within a SetLangString.
- **STRIP_TEXT**: Removes leading and trailing whitespace from text entries within a SetLangString.
- **VALID_LANG**: Requests language-tag validation for a SetLangString, subject to the dependency and validation-path conditions above.

## MultiLangStringFlag

- **DEFINED_LANG**: Ensures that a non-empty string is used for the 'lang' field of a MultiLangString.
- **DEFINED_TEXT**: Ensures that a non-empty string is used for the 'text' field of a MultiLangString.
- **LOWERCASE_LANG**: Converts all language codes to lowercase within a MultiLangString.
- **PRINT_WITH_LANG**: Includes language tags when printing a MultiLangString.
- **PRINT_WITH_QUOTES**: Wraps text entries in quotes when printing a MultiLangString.
- **STRIP_LANG**: Removes leading and trailing whitespace from language codes within a MultiLangString.
- **STRIP_TEXT**: Removes leading and trailing whitespace from text entries within a MultiLangString.
- **VALID_LANG**: Requests language-tag validation for a MultiLangString, subject to the dependency and validation-path conditions above.

