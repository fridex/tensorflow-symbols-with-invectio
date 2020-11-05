# tensorflow-symbols

Library symbols as provided by TensorFlow in various releases

This repository holds all the relevant files needed to extract symbols as
provided by TensorFlow (Python layer). A tool called
[invectio](https://github.com/thoth-station/invectio) was used to extract
symbols and [thoth-python](https://github.com/thoth-station/python) to discover
releases available on PyPI.

All the symbols can be found in ``data/`` directory.

## Missing symbols

The library extracted only public symbols (without ``_`` based on Python
convention). Also, some TensorFlow releases were not compatible with more
recent versions of Python as they stated async parameter name in sources which
lead to syntax issues:

```
    def TFE_ContextOptionsSetAsync(arg1, async):
                                         ^
SyntaxError: invalid syntax
```
