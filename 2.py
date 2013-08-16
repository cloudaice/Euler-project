#-*- coding: utf-8 -*-


def foo():
    fib = [1, 2]
    while fib[-1] < 4000000:
        f3 = fib[-2] + fib[-1]
        fib.append(f3)

    sum = 0
    for v in fib[:-1]:
        if v % 2 == 0:
            sum += v

    return sum

if __name__ == "__main__":
    print foo()
