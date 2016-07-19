__author__ = 'Hernan Y.Ke'
import itertools
p =list(itertools.combinations_with_replacement('ABC', 2))

for word in p:
    print(word)