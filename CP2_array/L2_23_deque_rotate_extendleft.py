__author__ = 'Hernan Y.Ke'
from collections import deque

dq = deque(range(5),maxlen=5)

dq.extend([1,2,3])
print(dq)
dq.extendleft([5,6,7])
print(dq)