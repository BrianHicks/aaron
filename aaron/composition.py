'composition'
import collections

class Composition(list):
    'a single composition'
    def __init__(self, *items):
        'initialize the collection'
        items = [(item, False) for item in items]

        super(Composition, self).__init__(items)

    def __gt__(self, other):
        'simple piping'
        self.append((other, False))

    def __rshift__(self, other):
        self.append((other, True))

    def __call__(self, initial):
        'apply the composition'
        result = initial
        for func, splat in self:
            if splat:
                result = func(*result)
            else:
                result = func(result)

        return result
