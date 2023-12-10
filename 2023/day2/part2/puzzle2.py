test_files = [
    './2023/day2/part1/inputs_simple.txt',
    './2023/day2/part1/inputs_full.txt'
]

for test_file in test_files:
    print(test_file)
    total = 0
    with open(test_file) as file:
        for line in file:
            [game_id, displays] = line.split(': ')
            [_, game_id_str] = game_id.split(' ')

            sample_sets = [x.strip().strip().split(',')
                           for x in displays.split(';')]
            values = {}
            for ss in sample_sets:
                for sample in ss:
                    pair = sample.strip().split(' ')
                    val = int(pair[0])
                    key = pair[1].strip(',')
                    if key not in values:
                        values[key] = val
                    values[key] = max(val, values[key])
            power = 1
            for k in values:
                power = power * values[k]
            total = total + power
        print(total)
