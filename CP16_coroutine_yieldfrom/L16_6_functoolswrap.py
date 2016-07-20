__author__ = 'Hernan Y.Ke'
from functools import wraps
def coroutine(func):
    @wraps(func)
    def primer(*args,**kwargs):
        gen=func(*args,**kwargs)
        next(gen)
        return gen
    return primer


@coroutine
def averager():
    total=0.0
    count=0
    ave=None
    while True:
        term = yield ave
        total+=term
        count+=1
        ave = total/count

coro_avg = averager()
from inspect import getgeneratorstate
print(getgeneratorstate(coro_avg))
coro_avg.send(10)
print(coro_avg.send(30))