import sys

sys.stdin = open('test2.txt')


def get_edges(line):
    return line.find('#'), line.rfind('#') + 1


def got_intersection(bottom_edges, line_edges):
    bottom_edges_set = set(range(*bottom_edges))
    line_edges_set = set(range(*line_edges))
    return bool(bottom_edges_set & line_edges_set)


def get_current_max(shape):
    shape = [line for line in shape if '#' in line]
    if not shape:
        return 0
    prev_line = shape[0]
    prev_line_ixs = [i for i in range(len(prev_line)) if prev_line[i] == '#']
    max_ = len(prev_line_ixs)
    # line_idx = 2
    for line in shape[1:]:
        line_ixs = [i for i in range(len(line)) if line[i] == '#']
        ixn = sorted(list(set(prev_line_ixs) & set(line_ixs)))
        sym_diff = sorted(list(set(prev_line_ixs) ^ set(line_ixs)))
        left = [x for x in sym_diff if x < ixn[0]]
        right = [x for x in sym_diff[::-1] if x > ixn[-1]]
        # print(line_idx, 'left:', len(left), '|', len(ixn), '|', 'right:', len(right))
        # print()
        max_border = max(len(left), len(right))
        max_ = max(max_, max_border)
        prev_line_ixs = line_ixs
        # line_idx += 1
    return max_


shape = []
intersected = False
max_ = 0
n = 8

for i in range(n):
    line = input()
    shape_bottom = shape[-1] if shape else None

    if shape_bottom:
        intersected = got_intersection(get_edges(shape_bottom), get_edges(line))

    if intersected:
        shape.append(line)

    if i == 0 and '#' in line:
        intersected = True
        shape.append(line)

    if not intersected or i == n - 1:
        current_max_horizontal = get_current_max(shape)
        # current_max_vertical = get_current_max([''.join(x) for x in zip(*shape)])
        # current_max = max(current_max_horizontal, current_max_vertical)
        # max_ = max(current_max, max_)
        max_ = max(current_max_horizontal, max_)
        shape = []
        shape.append(line)

print(max_)



def get_edges(line):
    return line.find('#'), line.rfind('#') + 1


def got_intersection(bottom_edges, line_edges):
    bottom_edges_set = set(range(*bottom_edges))
    line_edges_set = set(range(*line_edges))
    return bool(bottom_edges_set & line_edges_set)


def get_current_max(shape):
    shape = [line for line in shape if '#' in line]
    if not shape:
        return 0
    prev_line = shape[0]
    prev_line_ixs = [i for i in range(len(prev_line)) if prev_line[i] == '#']
    max_ = len(prev_line_ixs)
    for line in shape[1:]:
        line_ixs = [i for i in range(len(line)) if line[i] == '#']
        ixn = sorted(list(set(prev_line_ixs) & set(line_ixs)))
        sym_diff = sorted(list(set(prev_line_ixs) ^ set(line_ixs)))
        left = [x for x in sym_diff if x < ixn[0]]
        right = [x for x in sym_diff[::-1] if x > ixn[-1]]
        max_border = max(len(left), len(right))
        max_ = max(max_, max_border)
        prev_line_ixs = line_ixs
    return max_



t = int(input())

for _ in range(t):
    n, m = [int(x) for x in input().split()]

    shape = []
    intersected = False
    max_ = 0

    for i in range(n):
        line = input()
        shape_bottom = shape[-1] if shape else None

        if shape_bottom:
            intersected = got_intersection(get_edges(shape_bottom), get_edges(line))

        if intersected:
            shape.append(line)

        if i == 0 and '#' in line:
            intersected = True
            shape.append(line)

        if not intersected or i == n-1:
            print(shape)
            current_max_horizontal = get_current_max(shape)
            # current_max_vertical = get_current_max([''.join(x) for x in zip(*shape)])
            # current_max = max(current_max_horizontal, current_max_vertical)
            # max_ = max(current_max, max_)
            max_ = max(current_max_horizontal, max_)
            shape = []
            shape.append(line)

    print(max_)
