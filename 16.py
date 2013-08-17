#-*- coding: utf-8 -*-


def foo():
    num = 2 ** 1000
    num = list(str(num))
    num = [int(v) for v in num]
    return sum(num)

if __name__ == "__main__":
    print foo()
