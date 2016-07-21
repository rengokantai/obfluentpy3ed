__author__ = 'Hernan Y.Ke'
class Classstatic:
    @classmethod
    def klassmeth(*args):
        print(args)
    @staticmethod
    def statmeth(*args):
        print(args)
Classstatic.klassmeth()
Classstatic.klassmeth('spam')
Classstatic.statmeth()
Classstatic.statmeth('spam')