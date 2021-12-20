_ = input()
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

a_min = min(a)
b_mins = sorted({x for x in b if x <= a_min}, reverse=True)


def count(a_min_=a_min, mins=b_mins):
    counter = 0
    mismatch = False
    for a_, b_ in zip(a, b):
        local_counter = 0
        while a_ > a_min_ and b_ > 0:
            a_ -= b_
            local_counter += 1
        if a_ == a_min_:
            counter += local_counter
        else:
            mismatch = True
            break
    if not mismatch:
        return counter
    elif mins:
        return count(mins[0], mins=mins[1:])
    return -1


print(count())