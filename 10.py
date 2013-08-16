#-*-coding: utf-8 -*-


def foo():
    values = [1 for i in xrange(2000000)]
    values[0] = 0
    values[1] = 0
    for i in xrange(2, 1000000):
        if values[i]:
            for j in xrange(i * 2, 2000000, i):
                values[j] = 0

    primes = [i for i in xrange(2000000) if values[i]]
    return sum(primes)

if __name__ == "__main__":
    print foo()
