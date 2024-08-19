{{cookiecutter.package_name_stylized}} |release| Documentation
{{'=' * (cookiecutter.package_name_stylized|length)}}========================

Cookiecutter
------------
This package was created with the `cookiecutter <https://github.com/cookiecutter/cookiecutter>`_
package using `cookiecutter-snekpack <https://github.com/cthoyt/cookiecutter-snekpack>`_ template.
It comes with the following:

- Standard `src/` layout
- Declarative setup with `pyproject.toml` (following [PEP 621](https://peps.python.org/pep-0621/))
- Reproducible tests with `pytest` and `{{ cookecutter.runner }}`{% if cookiecutter.command_line_interface|lower != "false" %}
- A command line interface with `click`{% endif %}
- A vanity CLI via python entrypoints
- Version management with `bumpversion`
- Documentation build with `sphinx`
- Testing of code quality with `ruff` in `{{ cookiecutter.runner }}`
- Testing of documentation coverage with `docstr-coverage` in `{{ cookecutter.runner }}`
- Testing of documentation format and build in `{{ cookecutter.runner }}`
- Testing of package metadata completeness with `pyroma` in `{{ cookecutter.runner }}`
- Testing of MANIFEST correctness with `check-manifest` in `{{ cookecutter.runner }}`
- Testing of optional static typing with `mypy` in `{{ cookecutter.runner }}`
- A `py.typed` file so other packages can use your type hints
- Automated running of tests on each push with GitHub Actions
- Configuration for `ReadTheDocs <https://readthedocs.org/>`_
- A good base `.gitignore` generated from `gitignore.io <https://gitignore.io>`_.
- A pre-formatted README with badges
- A pre-formatted LICENSE file with the MIT License (you can change this to whatever you want, though)
- A pre-formatted CONTRIBUTING guide
- Automatic tool for releasing to PyPI with ``{{ cookecutter.runner }} -e finish``
- A copy of the `Contributor Covenant <https://www.contributor-covenant.org>`_ as a basic code of conduct

Table of Contents
-----------------
.. toctree::
   :maxdepth: 2
   :caption: Getting Started
   :name: start

   installation
   usage
{% if cookiecutter.command_line_interface|lower != "false" %}   cli{% endif %}

Indices and Tables
------------------
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
