'decorators'
from aaron.composition import Composition

def composable(func):
    return Composition(func)
