mapping = {
    9: 6,
    8: 7,
    7: 3,
    6: 6,
    5: 5,
    4: 4,
    3: 5,
    2: 5,
    1: 2,
    0: 6,
}


def matches_amount(N):
    matches = 0
    for digit in N:
        matches += mapping[int(digit)]
    return matches


def matches_to_number(matches):
    if matches % 2:
        return int('7' + '1' * ((matches-3) // 2))
    return int('1' * (matches // 2))


T = int(input())
for _ in range(T):
    N = input()
    matches = matches_amount(N)
    print(matches_to_number(matches))
