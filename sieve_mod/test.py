#test functionality for sieve_mod

import sieve

def test1():
    "Good golly gumdrops batman! A test!"
    assert sieve.sieve_next() == 3

def test2():
    "Great leaping leppers batman! Another one!"
    sieve.sieve_next()
    assert sieve.sieve_next() == 7

def test3():
    "By my litle sidekick boots batman! A third test!"
    sieve.sieve_next()
    sieve.sieve_next()
    assert sieve.sieve_next() == 17

test1()
test2()
test3()


print 'tests complete'
