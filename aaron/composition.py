'''
.. autoclass:: Composition
   :members:
   :special-members:
'''
import collections

class Composition(object):
    'a single composition, possibly with other compositions inside it'
    def __init__(self, *items):
        'initialize this Composition by _wrapping each item in a list'
        self.funcs = [
            self._wrap(item, splat=False) for item
            in list(items)
        ]

    def _flattened(self):
        'a _flattened version of this composition'
        flattened = []
        for item, splat in self.funcs:
            if isinstance(item, Composition):
                flattened += item._flattened()

            else:
                flattened.append((item, splat))

        return flattened

    def _wrap(self, func, splat=False):
        '''
        Functions are kept track of in a tuple of (function, splat). This
        function knows about this format, and makes items adhere to it. If an
        item is already a tuple, it will be ignored.
        '''
        if isinstance(func, tuple):
            return func

        return (func, splat)

    def __gt__(self, other):
        '''
        Use ``>`` to append to the composition, without splatting.
        '''
        return Composition(self, self._wrap(other, splat=False))

    def __rshift__(self, other):
        '''
        Use ``>>`` to append to the composition, with splatting.
        '''
        return Composition(self, self._wrap(other, splat=True))

    def __call__(self, *args, **kwargs):
        '''
        Call has two basic steps: getting an initial value, then running that
        initial value through each step of the composition.

        Note that the initial function will *always* receive ``*args`` and
        ``**kwargs``. All subsequent calls respect the second pair of the
        tuple, which will splat the output of the previous function (using the
        form ``func(*result)``.)
        '''
        result = self.funcs[0][0](*args, **kwargs)

        for func, splat in self.funcs[1:]:
            if splat:
                result = func(*result)
            else:
                result = func(result)

        return result
