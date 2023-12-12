import re

re_card_id = re.compile(r'Card\s+(\d+)')
re_number = re.compile(r'\d+')


def count_matching_numbers(card: dict) -> int:
    count = 0
    for number in card['my_numbers']:
        if number in card['winning_numbers']:
            count += 1
    return count

def calculate_worth(card: dict) -> int:
    count = count_matching_numbers(card)
    if count == 0:
        return 0
    return 2 ** (count - 1)

def get_scratchcard_info(scratchcard: str) -> dict:
    card_part, numbers_part = scratchcard.split(': ')
    winning_numbers_part, my_numbers_part = numbers_part.split(' | ')
    
    card_id = re_card_id.match(card_part).groups()[0]
    winning_numbers = re_number.findall(winning_numbers_part)
    my_numbers = re_number.findall(my_numbers_part)

    return {
        'card_id': int(card_id),
        'winning_numbers': [int(number) for number in winning_numbers],
        'my_numbers': [int(number) for number in my_numbers]
    }

def get_worths(scratchcards: str) -> list[int]:
    scratchcards_list = scratchcards.split('\n')
    cards_info = list(map(get_scratchcard_info, scratchcards_list))
    worths = list(map(calculate_worth, cards_info))

    return worths

def count_scratchcards(scratchcards: str) -> int:
    scratchcards_list = scratchcards.split('\n')
    cards_info = list(map(get_scratchcard_info, scratchcards_list))
    n_cards = len(cards_info)

    copies = [1] * n_cards
    count_m_numbers = [count_matching_numbers(card) for card in cards_info]

    for index in range(n_cards):
        count_m_number = count_m_numbers[index]

        index_aux = index + 1
        while count_m_number > 0 and index_aux < n_cards:
            copies[index_aux] += copies[index]
            count_m_number -= 1
            index_aux += 1

    return copies


if __name__ == '__main__':
    with open('scratchcards.txt') as f:
        scratchcards = f.read()

    worths = get_worths(scratchcards)

    # Part One
    print(f'Part One (Worth in total): {sum(worths)}')

    # Part Two
    copies = count_scratchcards(scratchcards)
    print(f'Part Two (Total scratchcards): {sum(copies)}')