#-*-coding: utf-8 -*-


def foo():
    count = 1
    num = 3
    primes = [2]
    while True:
        flag = True
        for p in primes:
            if num % p == 0:
                flag = False
                break
        if flag:
            primes.append(num)
            count += 1
        if count == 10001:
            break
        num += 2
    return num


if __name__ == "__main__":
    print foo()
