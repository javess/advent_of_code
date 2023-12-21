from collections import Counter
import functools

test_files = [
    './2023/day10/inputs_simple.txt',
    './2023/day10/inputs_full.txt'
]


producers = {
    '|': [(1, 0), (-1, 0)],
    '-': [(0, 1), (0, -1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(1, 0), (0, -1)],
    'F': [(1, 0), (0, 1)]
}

UP = 1
DOWN = 1 << 1
LEFT = 1 << 2
RIGHT = 1 << 3

start_map = {
    UP | DOWN: '|',
    LEFT | RIGHT: '-',
    UP | RIGHT: 'L',
    UP | LEFT: 'J',
    DOWN | RIGHT: 'F',
    DOWN | LEFT: '7',
}


def gen_next_pos(pos, matrix, visited):
    char = matrix[pos[0]][pos[1]]
    steps = producers.get(char, [])
    for s in steps:
        row = pos[0] + s[0]
        col = pos[1] + s[1]
        if row < 0 or col < 0 or row > len(matrix) or col > len(matrix[0]):
            # invalid position to check, skip... we should never hit this on good inputs
            continue
        if visited and (row, col) == visited[-1]:
            continue
        else:
            return (row, col)
    return None


def print_matrix(matrix):
    print("\n========= MATRIX ========\n")
    for m in matrix:
        print(m)


def clean_matrix(matrix, visited, start, start_symbol):
    new_matrix = []
    for m in matrix:
        new_matrix.append(['.'] * len(m.strip()))

    for v in visited:
        new_matrix[v[0]][v[1]] = matrix[v[0]][v[1]]

    new_matrix[start[0]][start[1]] = start_symbol
    return new_matrix


def horizontal_count(matrix):
    openers = ['F', '7']
    closers = ['J', 'L']
    closer_map = {
        'F': 'J',
        '7': 'L',
    }
    toggler = ['-']
    opener = None
    count = 0

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(cols):
        is_inside = False
        opener = None
        for j in range(rows):
            c = matrix[j][i]
            print(f'checking c ({j}, {i}) c = {c}, is_inside = {is_inside}')
            if c in toggler:
                is_inside = not is_inside
            elif c in openers:
                opener = c
            elif c in closers and closer_map.get(opener, 'XXX') == c:
                is_inside = not is_inside

            if c == '.' and is_inside:
                matrix[j][i] = 'X'
                count = count + 1
    print_matrix(matrix)
    return count


def navigate(matrix, start):
    # | is a vertical pipe connecting north and south.
    # - is a horizontal pipe connecting east and west.
    # L is a 90-degree bend connecting north and east.
    # J is a 90-degree bend connecting north and west.
    # 7 is a 90-degree bend connecting south and west.
    # F is a 90-degree bend connecting south and east.
    # . is ground; there is no pipe in this tile.
    # S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

    lenght = 1
    visited = [start]

    start_key = 0

    loop_pos = []
    if (start[0] > 0):
        if matrix[start[0] - 1][start[1]] in ['|', '7', 'F']:
            # up is valid
            start_key = start_key | UP
            print("start has up")
            loop_pos.append((start[0] - 1, start[1]))
    if (start[0] < len(matrix)-1):
        if matrix[start[0] + 1][start[1]] in ['|', 'J', 'L']:
            # down is valid
            print("start has down")
            start_key = start_key | DOWN
            loop_pos.append((start[0] + 1, start[1]))

    if (start[1] > 0):
        if matrix[start[0]][start[1] - 1] in ['-', 'L', 'F']:
            start_key = start_key | LEFT
            print("start has left")

            loop_pos.append((start[0], start[1]-1))
    if (start[1] < len(matrix[0])-1):
        if matrix[start[0]][start[1] + 1] in ['-', 'J', '7']:
            print("start has right")
            start_key = start_key | RIGHT
            loop_pos.append((start[0], start[1]+1))

    loop = loop_pos[0]
    while loop:
        # mark nodes as visited
        new_loop = gen_next_pos(loop, matrix, visited)
        visited.append(loop)
        loop = new_loop

    print(len(visited) // 2)
    print(visited)
    print(start_map.get(start_key, 'H'))
    matrix = clean_matrix(matrix, visited, start,
                          start_map.get(start_key, 'H'))
    print_matrix(matrix)
    print("\n==== FILL COUNT ====")
    print(horizontal_count(matrix))


for test_file in test_files:
    print(test_file)

    with open(test_file) as file:
        matrix = []
        start = (-1, -1)
        x, y = 0, 0
        for line in file:
            matrix.append(line)
            try:
                x = line.index('S')
                start = (y, x)
            except ValueError:
                pass
            y = y + 1

        print(start)
        navigate(matrix, start)
