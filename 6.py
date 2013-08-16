#-*-coding: utf-8 -*-


def foo():
    sum = 0
    for i in xrange(1, 101):
        for j in xrange(i + 1, 101):
            sum += 2 * i * j
    return sum

if __name__ == "__main__":
    print foo()
