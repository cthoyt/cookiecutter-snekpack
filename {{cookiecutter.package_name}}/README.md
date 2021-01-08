<!--
<p align="center">
  <img src="docs/source/logo.png" height="150">
</p>
-->

<h1 align="center">
  {{cookiecutter.package_name_stylized}}
</h1>

<p align="center">
    <a href="https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.github_repository_name}}/actions?query=workflow%3ATests">
        <img alt="Tests" src="https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.github_repository_name}}/workflows/Check%20mappings/badge.svg" />
    </a>
    <!-- Uncomment after deploying to PyPI
    <a href="https://pypi.org/project/{{cookiecutter.package_name}}">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/{{cookiecutter.package_name}}" />
    </a>
    <a href="https://pypi.org/project/{{cookiecutter.package_name}}">
        <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/{{cookiecutter.package_name}}" />
    </a>
    <a href="https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.github_repository_name}}/blob/main/LICENSE">
        <img alt="PyPI - License" src="https://img.shields.io/pypi/l/{{cookiecutter.package_name}}" />
    </a>
    -->
</p>

{{cookiecutter.short_description}}

## ⬇️ Installation

The most recent release can be installed from
[PyPI](https://pypi.org/project/{{cookiecutter.package_name}}/) with:

```bash
$ pip install {{cookiecutter.package_name}}
```

The most recent code and data can be installed directly from GitHub with:

```bash
$ pip install git+https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.github_repository_name}}.git
```

To install in development mode, use the following:

```bash
$ git clone git+https://github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.github_repository_name}}.git
$ cd {{cookiecutter.github_repository_name}}
$ pip install -e .
```

## 💪 Usage

### Command Line Interface

The {{cookiecutter.package_name}} command line tool is automatically installed. It can
be used from the shell with the `--help` flag to show all subcommands:

```shell
$ {{cookiecutter.package_name}} --help
```

## ⚖️ License

The code in this package is licensed under the MIT License.
