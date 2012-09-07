'composition'
import collections

class Composition(object):
    'a single composition'
    def __init__(self, *items):
        'initialize the collection'
        self.funcs = [
            self.wrap(item, splat=False) for item
            in list(items)
        ]

    def flattened(self):
        'a flattened version of this composition'
        flattened = []
        for item, splat in self.funcs:
            if isinstance(item, Composition):
                flattened += item.flattened()

            else:
                flattened.append((item, splat))

        return flattened

    def wrap(self, func, splat=False):
        'wrap a function'
        if isinstance(func, tuple):
            return func

        return (func, splat)

    def __gt__(self, other):
        'simple piping'
        return Composition(self, self.wrap(other, splat=False))

    def __rshift__(self, other):
        return Composition(self, self.wrap(other, splat=True))

    #def __call__(self, initial):
        #'apply the composition'
        #result = initial
        #for func, splat in self:
            #if splat:
                #result = func(*result)
            #else:
                #result = func(result)

        #return result
