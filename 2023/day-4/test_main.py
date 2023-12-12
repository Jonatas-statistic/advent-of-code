import pytest

from main import (
    count_scratchcards,
    get_scratchcard_info,
    get_worths
)


def get_ex_scratchcards():
    return """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

@pytest.fixture
def ex_scratchcards():
    return get_ex_scratchcards()


@pytest.mark.parametrize(
    'scratchcards_line, expected_card_info',
    zip(
        get_ex_scratchcards().split('\n'),
        [
            {
                'card_id': 1,
                'winning_numbers': [41, 48, 83, 86, 17],
                'my_numbers': [83, 86, 6, 31, 17, 9, 48, 53]
            },
            {
                'card_id': 2,
                'winning_numbers': [13, 32, 20, 16, 61],
                'my_numbers': [61, 30, 68, 82, 17, 32, 24, 19]
            },
            {
                'card_id': 3,
                'winning_numbers': [1, 21, 53, 59, 44],
                'my_numbers': [69, 82, 63, 72, 16, 21, 14, 1]
            },
            {
                'card_id': 4,
                'winning_numbers': [41, 92, 73, 84, 69],
                'my_numbers': [59, 84, 76, 51, 58, 5, 54, 83]
            },
            {
                'card_id': 5,
                'winning_numbers': [87, 83, 26, 28, 32],
                'my_numbers': [88, 30, 70, 12, 93, 22, 82, 36]
            },
            {
                'card_id': 6,
                'winning_numbers': [31, 18, 13, 56, 72],
                'my_numbers': [74, 77, 10, 23, 35, 67, 36, 11]
            }
        ]
    )
)
def test_get_scratchcard_info(scratchcards_line, expected_card_info):
    card_info = get_scratchcard_info(scratchcards_line)

    assert card_info == expected_card_info


def test_get_worths(ex_scratchcards):
    worths = get_worths(ex_scratchcards)

    assert worths == [8, 2, 2, 1, 0, 0]


# Part Two

def test_count_scratchcards(ex_scratchcards):
    ex_scratchcards += '\nCard 7: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'
    copies = count_scratchcards(ex_scratchcards)

    assert copies == [1, 2, 4, 8, 14, 1, 1]
    assert sum(copies) == 31