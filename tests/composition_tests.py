'test composition'
from unittest import TestCase

from aaron.composition import Composition

# some example functions
def add_one(n):
    return n + 1

def add_two(n):
    return n + 2

def ints_less_than(n):
    return range(1, n)

def product(*ns):
    result = 1
    for n in ns:
        result *= n

    return result

# test
class GtTests(TestCase):
    def setUp(self):
        self.comp = Composition(add_one)

    def test_gt(self):
        self.comp > add_two

        self.assertEqual(
            [
                (add_one, False),
                (add_two, False)
            ],
            list(self.comp)
        )

    def test_result(self):
        self.comp > add_two

        self.assertEqual(3, self.comp(0))


class RshiftTest(TestCase):
    def setUp(self):
        self.comp = Composition(ints_less_than)

    def test_rshift(self):
        self.comp >> product

        self.assertEqual(
            [(ints_less_than, False), (product, True)],
            list(self.comp)
        )

    def test_call(self):
        self.comp >> product

        self.assertEqual(6, self.comp(4))
