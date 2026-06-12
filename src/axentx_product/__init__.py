"""
Axentx Product Package
======================

This package provides a small, well‑tested example function that
is used by the test suite.  The function is intentionally simple
so that the focus remains on the packaging and test infrastructure.
"""

__all__ = ["add", "__version__"]

__version__ = "0.1.0"


def add(a: int | float, b: int | float) -> int | float:
    """
    Return the sum of *a* and *b*.

    Parameters
    ----------
    a : int | float
        First operand.
    b : int | float
        Second operand.

    Returns
    -------
    int | float
        The arithmetic sum of *a* and *b*.

    Examples
    --------
    >>> from axentx_product import add
    >>> add(2, 3)
    5
    >>> add(1.5, 2.5)
    4.0
    """
    return a + b
