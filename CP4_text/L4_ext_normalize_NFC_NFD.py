__author__ = 'Hernan Y.Ke'
from unicodedata import normalize
s1='café'
s2='cafe\u0301'
print(s1)
print(normalize('NFC',s1))
print(normalize('NFD',s1))
