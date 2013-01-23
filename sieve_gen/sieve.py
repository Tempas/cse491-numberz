# sieve functionality using a generator


def _is_prime(primes, n):
    "function for finding if a number is prime"
    for i in primes:
        if n % i == 0:
            return False
    return True


def sieve():
    #store primeslist inside generator
    primeslist = [2]

    while 1:
        #this should look familiar
        start = primeslist[-1] + 1
        while 1:
            if _is_prime(primeslist, start):
                primeslist.append(start)
                yield start

            start += 1
        


  
