#-*- coding: utf-8 -*-

import math


def foo():
    index = 1
    while True:
        num = index * (index + 1) / 2
        count = 0
        mid = int(math.sqrt(num))
        for i in range(1, mid):
            if num % i == 0:
                count += 1

        if mid * mid == num:
            if count >= 250:
                break
        else:
            if count > 250:
                break

        index += 1

    return index * (index + 1) / 2

if __name__ == "__main__":
    print foo()
