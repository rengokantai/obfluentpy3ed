__author__ = 'Hernan Y.Ke'
import random
class Bg:
    def __init__(self, items):
        self._items=list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('error')

    def __call__(self, *args, **kwargs):
        return self.pick()

print(callable(Bg(range(2))))
