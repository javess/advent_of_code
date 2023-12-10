test_files = [
    './2023/day1/part2/inputs_simple.txt',
    './2023/day1/part2/inputs_full.txt'
]


search_values = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def findValue(line: str):
    leftVal = -1
    rightVal = -1

    for i in range(len(line)):
        subline = line[i:]

        for k in search_values:
            if (subline.startswith(k)):
                leftVal = search_values[k]
                break
        if leftVal != -1:
            break

    for i in range(len(line)):
        subline = line[0:len(line)-i]

        for k in search_values:
            if (subline.endswith(k)):
                rightVal = search_values[k]
                break
        if rightVal != -1:
            break

    return leftVal * 10 + rightVal


for test_file in test_files:
    print(test_file)
    with open(test_file) as f:

        total = 0
        for l in f:
            val = findValue(l)
            total = total + val
        print(total)
