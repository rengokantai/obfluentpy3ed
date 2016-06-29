__author__ = 'Hernan Y.Ke'
from operator import add
from functools import reduce
ft=['banana','apple','mango','peach']
def reverse(word):
    return word[::-1]

print(sorted(ft,key=reverse))


print(reduce(add,range(1,10)))
