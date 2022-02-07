#!/usr/bin/env python

"""Code to run after generating the project."""

import os
import pathlib

PROJECT_DIRECTORY = pathlib.Path(os.path.realpath(os.path.curdir)).resolve()
PACKAGE = PROJECT_DIRECTORY.joinpath("src", "{{ cookiecutter.package_name }}")
DOCS = PROJECT_DIRECTORY.joinpath("docs", "source")

if __name__ == '__main__':
    if '{{ cookiecutter.command_line_interface|lower }}' == "false":
        PACKAGE.joinpath("cli.py").unlink()
        PACKAGE.joinpath("__main__.py").unlink()
        DOCS.joinpath("cli.rst").unlink()
