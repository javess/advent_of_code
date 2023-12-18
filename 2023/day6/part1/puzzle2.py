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

    times = []
    distances = []
    with open(test_file) as file:
        for line in file:
            if line.startswith("Time:"):
                times = [int(x) for x in line.split(':')[
                    1].strip().split(' ') if x.isdigit()]
                print(times)
            if line.startswith("Distance:"):
                distances = [int(x) for x in line.split(':')[
                    1].strip().split(' ') if x.isdigit()]
                print(distances)

    margin_of_error = 1
    for i in range(len(times)):
        ways_to_win = calculateWaysToWin(times[i], distances[i])
        if ways_to_win > 0:
            margin_of_error = margin_of_error * ways_to_win
        print(f"{ways_to_win} {margin_of_error}")

    print(margin_of_error)
