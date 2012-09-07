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
class WrapTests(TestCase):
    def test_wraps(self):
        self.assertEqual(
            Composition().wrap('x'),
            ('x', False)
        )

    def test_wraps_splat(self):
        self.assertEqual(
            Composition().wrap('x', splat=True),
            ('x', True)
        )

    def test_ignores_tuples(self):
        self.assertEqual(
            Composition().wrap(('1', '2')),
            ('1', '2')
        )

class GtTests(TestCase):
    def test_gt(self):
        comp = Composition(add_one) > add_two

        self.assertEqual(
            [
                (add_one, False),
                (add_two, False)
            ],
            comp.flattened()
        )

class RshiftTest(TestCase):
    def test_rshift(self):
        comp = Composition(ints_less_than) >> product

        self.assertEqual(
            [
                (ints_less_than, False),
                (product, True)
            ],
            comp.flattened()
        )

class CallTest(TestCase):
    def test_nosplat(self):
        comp = Composition(add_one) > add_two

        self.assertEqual(comp(0), 3)

    def test_splat(self):
        comp = Composition(ints_less_than) >> product

        self.assertEqual(comp(4), 6)

    def test_short(self):
        comp = Composition(add_one)

        self.assertEqual(comp(0), 1)

    def test_long(self):
        comp = Composition(add_one)
        for _ in range(99):
            comp = comp > add_one

        self.assertEqual(comp(0), 100)
