#-*- coding: utf-8 -*-


def bar(num):
    if num % 2 == 0:
        return num / 2
    else:
        return num * 3 + 1


def foo():
    dic = {}
    for i in xrange(2, 1000000):
        count = 1
        num = i
        while True:
            next_n = bar(num)
            if next_n == 1:
                dic[i] = count + 1
                break
            elif next_n in dic:
                dic[i] = count + dic[next_n]
                break
            else:
                count += 1
                num = next_n

    l = sorted(dic.items(), key=lambda d: d[1], reverse=True)

    return l[0][0]

if __name__ == "__main__":
    print foo()
