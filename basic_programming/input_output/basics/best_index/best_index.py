import sys

sys.stdin = open('data.txt')


def chunks(lst, step):
    i = 0
    while i < lst_len:
        if i + step > lst_len:
            break
        yield lst[i:i+step]
        i += step
        step += 1


def find_max(lst, step):
    max_ = 0
    for i in range(lst_len):
        l = []
        for x in chunks(lst[i:], step):
            l.extend(x)
        if sum(l) > max_:
            max_ = sum(l)
    return max_


lst_len = int(input())
lst = [int(x) for x in input().split()]
print(find_max(lst, 1))
