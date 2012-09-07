'tests for decorators'
from unittest import TestCase

from aaron.composition import Composition
from aaron.decorators import composable

def add_one(n):
    return n + 1

class ComposableTests(TestCase):
    'tests for composable decorator'

    def test_isinstance(self):
        self.assertFalse(isinstance(add_one, Composition))
        self.assertTrue(isinstance(composable(add_one), Composition))
