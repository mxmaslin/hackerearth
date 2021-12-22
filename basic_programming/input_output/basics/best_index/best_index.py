def sum_line(lst, step):
    ixs = []
    i = 0
    while i < lst_len:
        if step > len(lst[i:i+step]):
            break
        ixs.extend(lst[i:i+step])
        i += step
        step += 1
    return sum(x for x in ixs)


def find_max(lst, step):
    max_ = 0
    for i in range(lst_len):
        sum_ = sum_line(lst[i:], step)
        if sum_ > max_:
            max_ = sum_
    return max_


lst_len = int(input())
lst = [int(x) for x in input().split()]

print(find_max(lst, 1))
