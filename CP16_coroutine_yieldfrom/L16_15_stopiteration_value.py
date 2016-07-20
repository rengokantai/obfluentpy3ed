__author__ = 'Hernan Y.Ke'
from collections import namedtuple

Result = namedtuple('Result', 'count average')
def average():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total+=term
        count+=1
        average = total/count
    return Result(count,average)

coro_avg = average()
next(coro_avg)
coro_avg.send(10)
coro_avg.send(30)
try:
    coro_avg.send(None)
except StopIteration as exc:
    #result = exc.value
    print(exc.value)