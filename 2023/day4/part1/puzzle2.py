test_files = [
    './2023/day4/part1/inputs_simple.txt',
    './2023/day4/part1/inputs_full.txt'
]


for test_file in test_files:
    print(test_file)
    total = 0
    matrix = []
    with open(test_file) as file:
        for line in file:
            (card_id, card_info) = line.split(':')
            (winning_collection, numbers) = card_info.split('|')
            winning_collection_int = set([int(x)
                                          for x in winning_collection.strip().split(' ') if len(x) > 0])
            numbers_int = [int(x)
                           for x in numbers.strip().split(' ') if len(x) > 0]
            value = 0
            for n in numbers_int:
                if n in winning_collection_int:
                    if (value == 0):
                        value = 1
                    else:
                        value = value * 2
            print(f"{card_id} = {value}")
            total = total + value
    print(total)
