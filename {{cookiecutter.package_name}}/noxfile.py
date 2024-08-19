"""Encode workflows with Nox.

Note that Nox support is experimental for the cookiecutter-snekpack
and is not up to feature parity as the Tox configuration.

H/T to Moritz Wolter and using
https://github.com/v0lta/PyTorch-Wavelet-Toolbox/blob/main/noxfile.py
as a guide for preparing this.
"""

import nox

from pathlib import Path

# see https://nox.thea.codes/en/stable/usage.html#changing-the-sessions-default-backend
nox.options.default_venv_backend = "uv|virtualenv"

HERE = Path(__file__).parent.resolve()


@nox.session(tags=["tests"])
def tests(session: nox.Session):
    """Run unit and integration tests."""
    session.install(".[tests]")
    session.run("coverage", "run", "-p", "-m", "pytest", "--durations=20", "tests")
    session.run("coverage", "combine")
    session.run("coverage", "xml")


@nox.session(tags=["pre"])
def coverage_clean(session: nox.Session):
    """Remove testing coverage artifacts."""
    session.install("coverage")
    session.run("coverage", "erase")


@nox.session(tags=["tests"])
def doctests(session: nox.Session):
    """Test that documentation examples run properly."""
    session.install(".")
    session.install("xdoctest", "pygments")
    session.run("xdoctest", "-m", "src/")


@nox.session(tags=["tests"])
def treon(session: nox.Session):
    """Test that notebooks can run to completion."""
    if not HERE.joinpath("notebooks").is_dir():
        return
    session.install(".")
    session.install("treon")
    session.install("treon", "notebooks/")


@nox.session(tags=["formatting"])
def format(session: nox.Session):
    """Format the code in a deterministic way using ruff."""
    session.install("ruff")
    session.run("ruff", "check", "--fix")
    session.run("ruff", "format")


@nox.session(tags=["linting"])
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


@nox.session(tags=["linting"])
def doc8(session: nox.Session):
    """Run the doc8 tool to check the style of the RST files in the project docs."""
    session.install("sphinx", "doc8")
    session.run("doc8", "docs/source/")


@nox.session(name="docs-test", tags=["docs"])
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


@nox.session(tags=["linting"])
def docstr_coverage(session: nox.Session):
    """Run the docstr-coverage tool to check documentation coverage."""
    session.install("docstr-coverage")
    session.run("docstr-coverage", "src/", "tests/", "--skip-private", "--skip-magic")


@nox.session(tags=["linting"])
def manifest(session: nox.Session):
    """Check that the MANIFEST.in is written properly and give feedback on how to fix it."""
    session.install("check-manifest")
    session.run("check-manifest")


@nox.session(tags=["linting"])
def mypy(session: nox.Session):
    """Run the mypy tool to check static typing on the project."""
    session.install("mypy", "pydantic")
    session.run(
        "mypy",
        "--install-types",
        "--non-interactive",
        "--ignore-missing-imports",
        "src/",
    )


@nox.session(tags=["linting"])
def pyroma(session: nox.Session):
    """Run the pyroma tool to check the package friendliness of the project."""
    session.install("pygments", "pyroma")
    session.run("pyroma", "--min=10", ".")


@nox.session(tags=["dev"], default=False)
def build(session: nox.Session):
    """Build the package."""
    session.install("wheel", "build[uv]", "setuptools")
    session.run("python", "-m", "build", "--sdist", "--wheel", "--no-isolation")


@nox.session(tags=["dev"], default=False)
def release(session: nox.Session):
    """Build a pip package."""
    build(session)
    session.install("twine>=1.5.0")
    session.run("python", "-m", "twine", "upload", "--skip-existing", "dist/*")


@nox.session(tags=["dev"], default=False)
def finish(session: nox.Session):
    """Finish this version increase the version number and upload to PyPI."""
    session.install("bump2version")
    session.run("python", "-m", "bumpversion", "release", "--tag")
    release(session)
    session.run("git", "push", "--tags", external=True)
    session.run("python", "-m", "bumpversion", "patch")
    session.run("git", "push", external=True)


@nox.session(tags=["dev"], default=False)
def test_release(session: nox.Session):
    """Build a pip package."""
    build(session)
    session.install("twine>=1.5.0")
    session.run(
        "python",
        "-m",
        "twine",
        "upload",
        "--skip-existing",
        "--repository",
        "testpypi",
        "dist/*",
    )


@nox.session(tags=["dev"], default=False)
def test_finish(session: nox.Session):
    """Finish this version increase the version number and upload to PyPI."""
    session.install("bump2version")
    session.run("python", "-m", "bumpversion", "release", "--tag")
    test_release(session)
    session.run("git", "push", "--tags", external=True)
    session.run("python", "-m", "bumpversion", "patch")
    session.run("git", "push", external=True)
