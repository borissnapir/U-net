# generic stuff
import pytest

# Local stuff
from repo_name_to_be_changed.skeleton import fib

def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
