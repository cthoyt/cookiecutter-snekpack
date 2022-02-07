#!/usr/bin/env python

"""Code to run before generating the project.

Adapted from https://github.com/audreyfeldroy/cookiecutter-pypackage/blob/master/hooks/pre_gen_project.py.
"""

import re
import sys

MODULE_REGEX = re.compile(r'^[_a-zA-Z][_a-zA-Z0-9]+$')

module_name = '{{ cookiecutter.package_name}}'

if not MODULE_REGEX.match(module_name):
    print(
        f'ERROR: {module_name} is not a valid Python module name. Please do not use a - and use _ instead'
    )

    # Exit to cancel project
    sys.exit(1)
