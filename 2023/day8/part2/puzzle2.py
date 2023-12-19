from collections import Counter
import functools

test_files = [
    './2023/day8/inputs_simple_part2.txt',
    './2023/day8/inputs_full.txt'
]


def are_final_nodes(nodes):
    return all([n.endswith('Z') for n in nodes])


def get_next_nodes(nodes, direction):
    next_nodes = []
    for node in nodes:
        (l, r) = graph[node]
        next_nodes.append(l if direction == 'L' else r)

    return next_nodes


def navigate(steps, nodes, graph):
    cnt = 0

    while not are_final_nodes(nodes):
        direction = steps[cnt % len(steps)]
        nodes = get_next_nodes(nodes, direction)
        cnt = cnt + 1

    return cnt


def navigate(steps, node, graph):
    print("====NAVIGATE====")
    cnt = 0

    while not node.endswith('Z'):
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
        start_nodes = []

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
                if key.endswith('A'):
                    start_nodes.append(key)

        lcms = [navigate(steps, node, graph) for node in start_nodes]
        from math import lcm
        print(f"Part 2: {lcm(*lcms)}")
