test_files = [
    # './2023/day4/part2/inputs_simple.txt',
    './2023/day4/part2/inputs_full.txt'
]


cards = {}
pending_cards = []
processed_cards = {}


def rebuildCardId(card_id):
    pieces = card_id.split(' ')
    return f"Card {pieces[-1].strip()}"


def process_card(card_id, card_info):
    cid = rebuildCardId(card_id)
    cards[cid] = card_info
    pending_cards.append(cid)
    print(f"Add {cid}")


def consume_card(card_id, card_info):
    print(f"Consume {card_id}")
    curr_card_count = processed_cards.get(card_id, 0) + 1

    (winning_collection, numbers) = card_info.split('|')
    (_, id_str) = card_id.split(' ')
    id_int = int(id_str.strip())
    winning_collection_int = set([int(x)
                                  for x in winning_collection.strip().split(' ') if len(x) > 0])
    numbers_int = [int(x)
                   for x in numbers.strip().split(' ') if len(x) > 0]
    count = 0
    for n in numbers_int:
        if n in winning_collection_int:
            count = count + 1

    if count > 0:
        for i in range(count):
            next_id = id_int + i + 1
            idx = id_int - 1 + i + 1
            if idx < len(cards):
                next_id_str = f"Card {next_id}"
                processed_cards[next_id_str] = processed_cards.get(
                    next_id_str, 0) + curr_card_count
            else:
                print("DISCARD NOW!")

    return curr_card_count


for test_file in test_files:
    print(test_file)
    total = 0
    matrix = []
    with open(test_file) as file:
        for line in file:
            (card_id, card_info) = line.split(':')
            process_card(card_id, card_info)

    while len(pending_cards) > 0:
        card_id = pending_cards.pop(0)
        total = total + consume_card(card_id, cards[card_id])
    print(total)
