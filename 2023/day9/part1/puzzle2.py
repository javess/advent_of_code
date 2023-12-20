from collections import Counter
import functools

test_files = [
    './2023/day9/inputs_simple.txt',
    './2023/day9/inputs_full.txt'
]


def navigate(readings):
    if all([x == 0 for x in readings]):
        return 0
    diffs = []
    for i in range(1, len(readings)):
        diffs.append(readings[i]-readings[i-1])
    val = navigate(diffs)
    newVal = val + readings[-1]
    return newVal


for test_file in test_files:
    print(test_file)

    with open(test_file) as file:
        readings = []

        for line in file:
            readings.append([int(x) for x in line.strip().split(' ')])

        total = 0
        for x in readings:
            total = total + navigate(x)

        print(total)
