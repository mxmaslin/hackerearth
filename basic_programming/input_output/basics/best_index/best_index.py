import sys
sys.stdin = open('data.txt')


def row_max(lst, step):
    ixs = []
    i = 0
    while i < lst_len:
        if step > len(lst[i:i+step]):
            break
        ixs.extend(lst[i:i+step])
        i += step
        step += 1
    return sum(ixs)


def find_max(lst, step):
    max_ = 0
    for i in range(lst_len):
        sum_ = row_max(lst[i:], step)
        max_ = max(sum_, max_)
    return max_


lst_len = int(input())
lst = [int(x) for x in input().split()]

print(find_max(lst, 1))
