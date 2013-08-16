#-*- coding: utf-8 -*-


def is_pal(n):
    tmp = list(str(n))
    tmp.reverse()
    if n == int(''.join(tmp)):
        return True


def foo():
    large_pal = 0
    for i in xrange(100, 1000):
        for j in xrange(100, 1000):
            if is_pal(i * j) and i * j > large_pal:
                large_pal = i * j
    return large_pal


if __name__ == "__main__":
    print foo()
