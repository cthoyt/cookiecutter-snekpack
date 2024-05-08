# -*- coding: utf-8 -*-

"""This is a placeholder for putting the main code for your module.

If you don't want to keep ``api.py``, check the following places:

1. ``src/{{ cookiecutter.package_name }}/__init__.py`` contains a line
   ``from .api import *  # noqa``. You'll want to delete this and likely replace
   it with other imports for the most important functionality for your package
2. ``docs/usage.rst`` contains a line
   ``.. automodule:: {{cookiecutter.package_name}}.api``.
   You'll want to delete this and replace it with other imports
3. You don't need to update any linting or testing configuration since it is agnostic
   to the contents of the package.
"""

__all__ = [
    "hello",
]


def hello(name: str) -> None:
    """Print hello."""
    print(f"Hello, {name}")  # noqa: T201
