#-*- coding: utf-8 -*-

import math


def foo():
    values = [i ** 2 for i in xrange(1, 501)]
    for i in xrange(500):
        for j in xrange(i, 500):
            if values[i] + values[j] in values and i + 1 + j + 1 + int(math.sqrt(values[i] + values[j])) == 1000:
                print (i + 1) * (j + 1) * int(math.sqrt(values[i] + values[j]))


if __name__ == "__main__":
    foo()
