__author__ = 'Hernan Y.Ke'
import itertools
gen = itertools.count(1, .5)
#itertools.count(first, step)
#gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, .5))
print(next(gen))