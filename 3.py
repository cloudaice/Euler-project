#-*- coding: utf-8 -*-


def foo(n):
    fac_list = []
    x = 2
    while True:
        while n % x == 0:
            n = n / x
            if x not in fac_list:
                fac_list.append(x)
        x += 1
        if n <= x:
            fac_list.append(n)
            break

    fac_list.sort()
    return fac_list[-1]

if __name__ == "__main__":
    print foo(600851475143)
