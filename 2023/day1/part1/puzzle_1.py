test_files = [
    './2023/day1/part1/inputs_simple.txt',
    './2023/day1/part1/inputs_full.txt'
]


for test_file in test_files:
    print(test_file)
    with open(test_file) as f:

        total = 0
        for l in f:
            alphanum = [int(x) for x in l if x.isnumeric()]
            total = total + 10 * alphanum[0] + alphanum[-1]
        print(total)
