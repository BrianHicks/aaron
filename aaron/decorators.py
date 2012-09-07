'''
.. autofunction:: composable
'''
from aaron.composition import Composition

def composable(func):
    'return a Composition object with just this function'
    return Composition(func)
