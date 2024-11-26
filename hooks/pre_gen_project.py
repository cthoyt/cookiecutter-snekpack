#!/usr/bin/env python

"""Code to run before generating the project.

Adapted from https://github.com/audreyfeldroy/cookiecutter-pypackage/blob/master/hooks/pre_gen_project.py.
"""

import re
import sys

PYTHON_PACKAGE_NAME_REGEX = re.compile(r"^[a-z][_a-z0-9]+$")
REPOSITORY_REGEX = re.compile(r"^[a-zA-Z][-a-zA-Z0-9]+$")

python_package_name = "{{ cookiecutter.package_name}}"
repository_name = "{{ cookiecutter.github_repository_name }}"

if not PYTHON_PACKAGE_NAME_REGEX.match(python_package_name):
    print(
        f"ERROR: {python_package_name} is not a valid Python package name. "
        "Please use lowercase only, do not use - and use _ instead."
    )

    # Exit to cancel project
    sys.exit(1)

if not REPOSITORY_REGEX.match(repository_name):
    print(
        f"ERROR: {repository_name} is not a good version control repository name. "
        f"Please do not use _ and use - instead."
    )

    # Exit to cancel project
    sys.exit(1)
