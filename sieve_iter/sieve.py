#implementation of 'sieve' functionality via Python iterator

class sieve(object):
    def __init__(self):
        self.primeslist = [2]


    def __iter__(self):
        return self

    def _isPrime(self, n):
        "private method for detirmining priminivity (I made that word up)"
        for i in self.primeslist:
            if n % i == 0:
                return False
        return True

    def next(self):
        "called in 'for' loop implicitly"

        #this should look familiar to you
        start = self.primeslist[-1] + 1
        while 1:
            if self._isPrime(start):
                self.primeslist.append(start)
                return start
            start += 1

