#test generator for sieve

import sieve

def test1():
    "Look at this test! The beauty, the finess"
    s = sieve.sieve()
    i = iter(s)
    assert i.next() == 3

def test2():
    "This test is even cooler!"
    s = sieve.sieve()
    i = iter(s)
    i.next()
    assert i.next() == 5

def test3():
    "3 is a bigger number than 2 or 1, and thats a fact"
    s = sieve.sieve()
    i = iter(s)
    i.next()
    i.next()
    assert i.next() == 7

test1()
test2()
test3()

print 'tests complete'
