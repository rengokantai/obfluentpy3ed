__author__ = 'Hernan Y.Ke'
def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')

res1 = [x*3 for x in gen_AB()]

for i in res1:
    print('-->', i)