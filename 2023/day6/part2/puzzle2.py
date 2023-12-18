import sys
test_files = [
    './2023/day6/inputs_simple.txt',
    './2023/day6/inputs_full.txt'
]


def calculateWaysToWin(time, distance):
    start = 0
    end = time

    for i in range(time):
        opt_distance = i * (time - i)
        if opt_distance > distance:
            start = i
            break
    for i in range(time, 0, -1):
        opt_distance = i * (time - i)
        if opt_distance > distance:
            end = i
            break
    print(f"{start} - {end}")
    return end - start + 1


for test_file in test_files:
    print(test_file)
    total = 0

    time = 0
    distance = 0
    with open(test_file) as file:
        for line in file:
            if line.startswith("Time:"):
                time = int(''.join([x for x in line.split(':')[
                    1].strip().split(' ') if x.isdigit()]))
                print(time)
            if line.startswith("Distance:"):
                distance = int(''.join([x for x in line.split(':')[
                    1].strip().split(' ') if x.isdigit()]))
                print(distance)

    margin_of_error = 1
    ways_to_win = calculateWaysToWin(time, distance)
    print(ways_to_win)
