import pytest
from axentx_product import add, __version__


def test_add_integers():
    assert add(1, 2) == 3


def test_add_floats():
    assert add(1.5, 2.5) == 4.0


def test_version():
    assert isinstance(__version__, str)
    assert __version__ == "0.1.0"
