#-*- coding: utf-8 -*-


def foo():
    a = range(21, 41)
    b = range(1, 21)
    func = lambda l: reduce(lambda x, y: x * y, l)
    return func(a) / func(b)

if __name__ == "__main__":
    print foo()
