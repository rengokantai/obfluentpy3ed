__author__ = 'Hernan Y.Ke'


def make_avr():
    series=[]
    def averager(new_value):
        series.append(new_value)
        total=sum(series)
        return total/len(series)
    return averager

avg = make_avr()

print(avg.__code__.co_freevars)
print(avg.__code__.co_varnames)
print(avg.__closure__[0].cell_contents)