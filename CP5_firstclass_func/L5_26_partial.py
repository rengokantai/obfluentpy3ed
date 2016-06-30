__author__ = 'Hernan Y.Ke'
from functools import partial
from operator import mul
doub = partial(mul,3)
print(doub(4))