# Cookiecutter Snekpack

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) for making new Python repositories.

This template is different from [@audreyfeldroy](https://github.com/audreyfeldroy)'s
[cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) because it uses the source
layout and has lots of code quality assurance checks built in. If you're looking for something similar but not quite
like this, try her package or see
her [list of alternatives](https://cookiecutter-pypackage.readthedocs.io/en/latest/readme.html#similar-cookiecutter-templates).

I've written several blog posts outlining all the ideas that made it into this template:

- [Blog: Flake8](https://cthoyt.com/2020/04/25/how-to-code-with-me-flake8)
- [Blog: Packaging](https://cthoyt.com/2020/06/03/how-to-code-with-me-organization)
- [Blog: CLIs](https://cthoyt.com/2020/06/11/click)
- [Blog: CLIs and Flask](https://cthoyt.com/2021/01/11/click-and-flask)

## 🛠️ Getting Started

1. Install `cruft` with:

   ```shell
   python -m pip install cruft
   ```

2. Run `cruft` with:

   ```shell
   cruft create https://github.com/cthoyt/cookiecutter-snekpack
   ```

3. Enter the requested information, then win! Remember, package names should only have letters, numbers,
   and underscores.

4. If you're working under version control, copy the repository into your folder tracked under git, commit
   the files, and push to your remote.

You can see an example repository of what happens right after you run these commands at
https://github.com/cthoyt/snekpack-demo.

## 💪 Features

Your new python package will have the following:

- Standard `src/` layout
- Declarative setup with `pyproject.toml` (following [PEP 621](https://peps.python.org/pep-0621/))
- Reproducible workflows configured with `tox` or `nox`
  - Reproducible tests with `pytest` and 
  - Reproducible notebooks with [`treon`](https://github.com/reviewNB/treon)
  - Documentation build with `sphinx` 8.0+ and `sphinx-rtd-theme` 3.0+
  - Testing of code quality with `ruff`
  - Testing of documentation coverage with `docstr-coverage`
  - Testing of documentation format
  - Testing of package metadata completeness with `pyroma`
  - Testing of MANIFEST correctness with `check-manifest`
  - Testing of optional static typing with `mypy`
  - Version management with [`bump-my-version`](https://github.com/callowayproject/bump-my-version)
  - Building with `uv build`
  - Releasing to PyPI with `twine`
- A command line interface with `click`
- A vanity CLI via python entrypoints
- A `py.typed` file so other packages can use your type hints
- Automated running of tests on each push
  with [GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions)
- Configuration for [ReadTheDocs](https://readthedocs.org/)
- A good base `.gitignore` generated from [gitignore.io](https://gitignore.io).
- A pre-formatted README with badges
- A pre-formatted LICENSE file with the MIT License (you can change this to whatever you want, though)
- A pre-formatted CONTRIBUTING guide
- A copy of the [Contributor Covenant](https://www.contributor-covenant.org/) as a basic code of conduct

## Attribution

Feel free to adapt this template to your needs, but please credit me in your README and link back
to https://github.com/cthoyt/cookiecutter-snekpack.

### ⚖️ License

This cookiecutter package is licensed under the MIT License.
