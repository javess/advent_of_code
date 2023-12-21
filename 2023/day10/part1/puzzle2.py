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

    loop_pos = []
    if (start[0] > 0):
        if matrix[start[0] - 1][start[1]] in ['|', '7', 'F']:
            # up is valid
            loop_pos.append((start[0] - 1, start[1]))
    if (start[0] < len(matrix[0])-1):
        if matrix[start[0] + 1][start[1]] in ['|', 'J', 'L']:
            # down is valid
            loop_pos.append((start[0] + 1, start[1]))

    if (start[1] > 0):
        if matrix[start[0]][start[1] - 1] in ['-', 'L', 'F']:
            # up is valid
            loop_pos.append((start[0], start[1]-1))
    if (start[1] < len(matrix)-1):
        if matrix[start[0]][start[1] + 1] in ['-', 'J', '7']:
            # down is valid
            loop_pos.append((start[0], start[1]+1))

    loop = loop_pos[0]
    while loop:
        # mark nodes as visited
        new_loop = gen_next_pos(loop, matrix, visited)
        visited.append(loop)
        loop = new_loop

    print(len(visited) // 2)


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
