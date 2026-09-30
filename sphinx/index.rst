Welcome to langstring's code documentation!
=============================================

.. warning::

   **Verified hashing limitations in langstring 3.0.2.** An AI-assisted assessment
   independently reproduced two problems in the published package. With default
   flags, a ``LangString`` can equal a plain ``str`` while their hashes differ;
   do not rely on mixed-type dictionary keys or set members for lookup or
   deduplication. ``LangString``, ``SetLangString``, and ``MultiLangString`` are
   mutable and content-hashed: mutation after insertion into a set or use as a
   dictionary key can break lookup, including mutation of nested collections.

   Prefer dictionary values or list items, or use immutable snapshots as keys.
   For a ``LangString``, use ``value.text`` for text-only identity or
   ``(value.text, value.lang.casefold())`` for text-and-language identity.
   Do not mutate an instance while it is a key or set member. This warning does
   not fix the implementation or imply that ordinary use outside hashed
   keys/members is unsafe because of these findings. Unlike these custom
   classes, built-in mutable sets and dictionaries are unhashable; API wording
   comparing their hash methods should not be read as a safety guarantee.

.. note::

   Language-tag validation uses ``VALID_LANG`` and is disabled by default.
   Install ``langstring[langcodes]`` and enable the relevant class flag or
   ``GlobalFlag.VALID_LANG``. Invalid tags raise ``ValueError`` when they pass
   through validation with the dependency available. Enabling flags does not
   revalidate existing objects; direct edits to exposed collections may bypass
   validation. If importing ``langcodes`` fails, validation warns with
   ``UserWarning`` and is skipped unless ``GlobalFlag.ENFORCE_EXTRA_DEPEND`` is
   enabled, in which case it raises ``ImportError``. That flag alone does not
   enable validation. Flags are shared across the process.

.. raw:: html

    <div class="custom-logo">
        <img src="https://raw.githubusercontent.com/pedropaulofb/langstring/main/resources/langstring-lib-logo.png" alt="Library Logo">
    </div>

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

langstring Websites
===================

.. raw:: html

    <div style="text-align: left; margin-bottom: 20px;">
        <a href="https://github.com/pedropaulofb/langstring">
            <img src="https://raw.githubusercontent.com/pedropaulofb/langstring/main/resources/github-logo.png" width="20" align="middle"> View on GitHub </a>
    </div>
    <div style="text-align: left;">
        <a href="https://pypi.org/project/langstring">
            <img src="https://raw.githubusercontent.com/pedropaulofb/langstring/main/resources/pypi-logo.png" width="20" align="middle"> View on PyPI </a>
    </div>
