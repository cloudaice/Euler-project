#-*- coding: utf-8 -*-


def foo(a, b, c):
    mti_a = (c - 1) / a
    mti_b = (c - 1) / b
    mti_d = (c - 1) / (a * b)

    def bar(v1, v2):
        return v1 * (v2 + 1) * v2 / 2

    return bar(a, mti_a) + bar(b, mti_b) - bar(a * b, mti_d)

if __name__ == "__main__":
    print foo(2, 3, 1000)
