#-*- coding: utf-8 -*-


def large_fac(a, b):
    if a % b == 0:
        return b
    else:
        return large_fac(b, a % b)


def foo():
    n = 1
    for i in xrange(2, 21):
        n = i * n / large_fac(n, i)
    return n

if __name__ == "__main__":
    print foo()
