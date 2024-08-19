"""Encode workflows with Nox.

Note that Nox support is experimental for the cookiecutter-snekpack
and is not up to feature parity as the Tox configuration.
"""

import nox

from pathlib import Path

nox.options.default_venv_backend = 'uv'

HERE = Path(__file__).parent.resolve()


@nox.session()
def tests(session: nox.Session):
    """Run unit and integration tests."""
    session.install(".[tests]")
    session.run("coverage", "run", "-p", "-m", "pytest", "--durations=20", "tests")
    session.run("coverage", "combine")
    session.run("coverage", "xml")


@nox.session()
def coverage_clean(session: nox.Session):
    """Remove testing coverage artifacts."""
    session.install("coverage")
    session.run("coverage", "erase")


@nox.session()
def doctests(session: nox.Session):
    """Test that documentation examples run properly."""
    session.install(".")
    session.install("xdoctest", "pygments")
    session.run("xdoctest", "-m", "src/")


@nox.session()
def treon(session: nox.Session):
    """Test that notebooks can run to completion."""
    if not HERE.joinpath("notebooks").is_dir():
        return
    session.install(".")
    session.install("treon")
    session.install("treon", "notebooks/")


@nox.session()
def format(session: nox.Session):
    """Format the code in a deterministic way using ruff."""
    session.install("ruff")
    session.run("ruff", "check", "--fix")
    session.run("ruff", "format")


@nox.session()
def lint(session: nox.Session):
    """Check code quality using ruff and other tools."""
    session.install("ruff", "darglint2")
    session.run("ruff", "check")
    session.run(
        "darglint2",
        "--strictness",
        "short",
        "--docstring-style",
        "sphinx",
        "-v",
        "2",
        "src/",
        "tests/",
        "notebooks/",
    )


@nox.session()
def doc8(session: nox.Session):
    """Run the doc8 tool to check the style of the RST files in the project docs."""
    session.install("sphinx", "doc8")
    session.run("doc8", "docs/source/")


@nox.session()
def docs_test(session: nox.Session):
    """Test building the documentation in an isolated environment."""
    session.install(".[docs]")
    session.chdir("docs")

    directory = Path(session.create_tmp())
    source = directory / "source"

    session.run("cp", "-r", "source", source, external=True)
    session.run(
        "python",
        "-m",
        "sphinx",
        "-W",  # Warnings are considered as errors via -W
        "-b",
        "html",
        "-d",
        directory / "build" / "doctrees",
        source,
        directory / "build" / "html",
    )


@nox.session()
def docstr_coverage(session: nox.Session):
    """Run the docstr-coverage tool to check documentation coverage."""
    session.install("docstr-coverage")
    session.run("docstr-coverage", "src/", "tests/", "--skip-private", "--skip-magic")


@nox.session()
def manifest(session: nox.Session):
    """Check that the MANIFEST.in is written properly and give feedback on how to fix it."""
    session.install("check-manifest")
    session.run("check-manifest")


@nox.session()
def mypy(session: nox.Session):
    """Run the mypy tool to check static typing on the project."""
    session.install("mypy", "pydantic")
    session.run("mypy", "--install-types", "--non-interactive", "--ignore-missing-imports", "src/")


@nox.session()
def pyroma(session: nox.Session):
    """Run the pyroma tool to check the package friendliness of the project."""
    session.install("pygments", "pyroma")
    session.run("pyroma", "--min=10", ".")
