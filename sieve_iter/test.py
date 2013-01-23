#test functionality of iterator for sieve

import sieve

def test1():
    "this is a pretty self explanitory test"
    s = sieve.sieve()
    i = iter(s)
    assert i.next() == 3

def test2():
    "so is this one"
    s = sieve.sieve()
    i = iter(s)
    i.next()
    assert i.next() == 5

def test3():
    "This one is impossibly difficult to understand"
    # psych
    s = sieve.sieve()
    i = iter(s)
    i.next()
    i.next()
    assert i.next() == 7

test1()
test2()
test3()

print 'tests complete'
