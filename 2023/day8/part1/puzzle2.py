from collections import Counter
import functools

test_files = [
    './2023/day8/inputs_simple.txt',
    './2023/day8/inputs_full.txt'
]


def navigate(steps, node, end, graph):
    print("====NAVIGATE====")
    cnt = 0

    while node != end:
        (l, r) = graph[node]
        direction = steps[cnt % len(steps)]
        if direction == 'L':
            node = l
        else:
            node = r

        cnt = cnt + 1

    return cnt


for test_file in test_files:
    print(test_file)

    with open(test_file) as file:
        graph = {}
        visited = []
        steps = ''

        for line in file:
            if not line.strip():
                continue
            if len(steps) == 0:
                steps = line.strip()
            else:
                parts = line.split(' = ')
                key = parts[0]
                lr = parts[1].strip().strip('(').strip(')').split(', ')
                graph[key] = (lr[0], lr[1])
        print(navigate(steps, 'AAA', 'ZZZ', graph))
