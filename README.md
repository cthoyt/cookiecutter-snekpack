# Cookiecutter Python Package

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) for making new Python repositories.

This template is different from [@audreyfeldroy](https://github.com/audreyfeldroy)'s
[cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) because it uses the source
layout and has lots of code quality assurance checks built in. If you're looking for something similar but not quite
like this, try her package or see her [list of alternatives](https://cookiecutter-pypackage.readthedocs.io/en/latest/readme.html#similar-cookiecutter-templates).

I've written several blog posts outlining all of the ideas that made it into this template:

- [Blog: Flake8](https://cthoyt.com/2020/04/25/how-to-code-with-me-flake8)
- [Blog: Packaging](https://cthoyt.com/2020/06/03/how-to-code-with-me-organization)
- [Blog: CLIs](https://cthoyt.com/2020/06/11/click)
- [Blog: CLIs and Flask](https://cthoyt.com/2021/01/11/click-and-flask)

## 🛠️ Getting Started

1. Install `cookiecutter` with:

    ```shell
    $ pip install cookiecutter
    ```

2. Run `cookiecutter` with:

    ```shell
    $ cookiecutter https://github.com/cthoyt/cookiecutter-python-package
    ```

3. Enter the requested information, then win! Remember, package names should only have letters, numbers,
   and underscores.

4. If you're working under version control, copy the repository into your folder tracked under git, commit
   the files, and push to your remote.

## 💪 Features

Your new python package will have the following:

- Standard `src/` layout
- Declarative setup with `setup.cfg`
- Reproducible tests with `pytest` and `tox`
- A command line interface with `click`
- A vanity CLI via python entrypoints
- Version management with `bumpversion`
- Documentation build with `sphinx`
- Testing of code quality with `flake8` in `tox`
- Testing of documentation coverage with `docstr-coverage` in `tox`
- Testing of documentation format and build in `tox`
- Testing of package metadata completeness with `pyroma` in `tox`
- Testing of MANIFEST correctness with `check-manifest` in `tox`
- Automated running of tests on each push with GitHub Actions
- Configuration for ReadTheDocs
- A good base `.gitignore` generated from [gitignore.io](https://gitignore.io).
- A pre-formatted README with badges
- A pre-formatted LICENSE file with the MIT License (you can change this to whatever you want, though)
- A pre-formatted CONTRIBUTING guide
- Automatic tool for releasing to PyPI with `tox -e finish`

## ⚖️ License

This cookiecutter package is licensed under the MIT License.
