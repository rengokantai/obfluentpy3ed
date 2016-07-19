__author__ = 'Hernan Y.Ke'
import itertools
p = list(itertools.zip_longest('ABC', range(5), fillvalue='?'))
for word in p:
    print(word)