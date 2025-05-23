#!/usr/bin/env python

"""Code to run after generating the project."""

import os
import pathlib
import subprocess

PROJECT_DIRECTORY = pathlib.Path(os.path.realpath(os.path.curdir)).resolve()
PACKAGE = PROJECT_DIRECTORY.joinpath("src", "{{ cookiecutter.package_name }}")
DOCS = PROJECT_DIRECTORY.joinpath("docs", "source")

if __name__ == "__main__":
    if "{{ cookiecutter.command_line_interface|lower }}" == "false":
        PACKAGE.joinpath("cli.py").unlink()
        PACKAGE.joinpath("__main__.py").unlink()
        DOCS.joinpath("cli.rst").unlink()

    if "{{ cookiecutter.gitlab|lower }}" == "false":
        PROJECT_DIRECTORY.joinpath(".gitlab-ci.yml").unlink()

    if "{{ cookiecutter.runner }}" == "tox":
        PROJECT_DIRECTORY.joinpath("noxfile.py").unlink()
    else:
        PROJECT_DIRECTORY.joinpath("tox.ini").unlink()

    # Invokes prettier to reformat markdown files
    subprocess.call([
        "npx", "--yes", "prettier", "--prose-wrap", "always", "--write", "**/*.md",
    ])

    # Invokes docstrfmt to clean up RST and docstrings
    subprocess.call([
        "uvx", "docstrfmt", "src/", "tests/", "docs/", "--no-docstring-trailing-line",
    ])
