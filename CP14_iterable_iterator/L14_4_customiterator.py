__author__ = 'Hernan Y.Ke'
import re
import reprlib
reg = re.compile('\w+')     #put outside of class
class Sentence:

    def __init__(self,sentence):
        self.sentence = sentence
        self.words = reg.findall(sentence)

    def __iter__(self):
        return SentenceIterator(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.sentence) #reprlib.repr generate abbrivated sentence

class SentenceIterator:
    def __init__(self,words):
        self.words = words
        self.index=0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index+=2
        return word
    def __iter__(self):
        return self
s = Sentence('test python pu')
for word in s:
    print(word)