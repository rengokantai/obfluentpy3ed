__author__ = 'Hernan Y.Ke'
from array import array
from random import random
floats = array('d',(random() for i in range(10**2)))
fp = open('./large.txt','wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('./large.txt','rb')
floats2.fromfile(fp,10**2)
fp.close()
print(floats==floats2)