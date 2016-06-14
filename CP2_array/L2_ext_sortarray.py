__author__ = 'Hernan Y.Ke'
from array import array
arr = array('I',[1,3,2])

arr=array(arr.typecode,sorted(arr))   # typecode = I
print(arr)