"""{{ cookiecutter.short_description.rstrip(".") }}."""

from .api import hello, square

# being explicit about exports is important!
__all__ = [
    "hello",
    "square",
]
