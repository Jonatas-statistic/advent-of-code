from hand import Hand, HandTwo


def read_hands(directory: str) -> list[Hand]:
    with open(directory) as f:
        lines = f.readlines()
    hands = []
    for line in lines:
        hand, bid = line.strip().split(' ')
        hands.append(Hand(hand = hand, bid = int(bid)))
    return hands

def get_total_winnings(hands: list[Hand]):
    sorted_hands = sorted(hands, key = lambda hand: (hand.type, hand.ordered_hand))
    total_winnings = 0
    for index, hand in enumerate(sorted_hands):
        total_winnings += (index + 1) * hand.bid
    return total_winnings


# Part Two
def read_hands_two(directory: str) -> list[HandTwo]:
    with open(directory) as f:
        lines = f.readlines()
    hands = []
    for line in lines:
        hand, bid = line.strip().split(' ')
        hands.append(HandTwo(hand = hand, bid = int(bid)))
    return hands


if __name__ == '__main__':
    hands = read_hands('hands.txt')

    # Part One
    total_winnings = get_total_winnings(hands)
    print(f'Part One: {total_winnings}')

    # Part Two
    hands_two = read_hands_two('hands.txt')
    total_winnings_two = get_total_winnings(hands_two)
    print(f'Part Two: {total_winnings_two}')