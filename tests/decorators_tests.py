'tests for decorators'
from unittest import TestCase

from aaron.composition import Composition
from aaron.decorators import composable

def add_one(n):
    return n + 1

def test_composable():
    assert not isinstance(add_one, Composition)
    assert isinstance(composable(add_one), Composition)
