from collections import Counter
import functools

test_files = [
    './2023/day7/inputs_simple.txt',
    './2023/day7/inputs_full.txt'
]


def card_to_value(chr):
    if chr.isdigit():
        return int(chr)

    if chr == 'A':
        return 14
    if chr == 'K':
        return 13
    if chr == 'Q':
        return 12
    if chr == 'J':
        return 11
    if chr == 'T':
        return 10


def compare_hands(hand1, hand2):
    print(f'Compare {hand1} {hand2}')
    for i in range(len(hand1[0])):
        chr1 = hand1[0][i]
        chr2 = hand2[0][i]
        print(f'Comparing {chr1} == {chr2}')
        if (chr1 == chr2):
            continue

        if card_to_value(chr1) < card_to_value(chr2):
            return 1
        elif card_to_value(chr1) > card_to_value(chr2):
            return -1
        else:
            return 0


for test_file in test_files:
    print(test_file)
    total = 0

    times = []
    distances = []
    hand_types = [
        '5_kind',
        '4_kind',
        'full_house',
        '3_kind',
        '2_pair',
        '1_pair',
        'high_card'
    ]
    hands_by_type = {
        '5_kind': [],
        '4_kind': [],
        'full_house': [],
        '3_kind': [],
        '2_pair': [],
        '1_pair': [],
        'high_card': []
    }
    with open(test_file) as file:
        hand_count = 0
        for line in file:
            parts = line.split(' ')
            hand = parts[0]
            counter = Counter(hand)
            bid = int(parts[1])
            hand_count = hand_count + 1
            if len(counter) == 1:
                hands_by_type['5_kind'].append((hand, bid))
            elif len(counter) == 2:
                if (any([x == 1 or x == 4 for x in counter.values()])):
                    hands_by_type['4_kind'].append((hand, bid))
                else:
                    hands_by_type['full_house'].append((hand, bid))
            elif len(counter) == 3:
                if (any([x == 3 for x in counter.values()])):
                    hands_by_type['3_kind'].append((hand, bid))
                else:
                    hands_by_type['2_pair'].append((hand, bid))
            elif len(counter) == 4:
                hands_by_type['1_pair'].append((hand, bid))
            else:
                hands_by_type['high_card'].append((hand, bid))
        print(hands_by_type)

        hand_idx = 0
        full_value = 0
        for t in hand_types:
            hands = hands_by_type[t]
            hands.sort(key=functools.cmp_to_key(compare_hands))
            for h in hands:
                print(h)
                print(f"{h[1]} * {hand_count - hand_idx}")
                full_value = full_value + (h[1] * (hand_count - hand_idx))
                hand_idx = hand_idx + 1
        print(f"Total value {full_value}")
