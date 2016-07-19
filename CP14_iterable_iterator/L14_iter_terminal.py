__author__ = 'Hernan Y.Ke'
# A Closer Look at the iter Function
from random import randint
#roll a six-sided dice until a 1 is rolled:
def rolldice():
    return randint(1,6)

for i in iter(rolldice,1):  #must callable, not rolldice()
    print(i)