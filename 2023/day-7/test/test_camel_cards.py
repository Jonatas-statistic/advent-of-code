import os
import pytest

from camel_cards import read_hands, get_total_winnings, read_hands_two
from hand import Hand


@pytest.fixture(scope='module')
def hands():
    return read_hands(os.path.join('test', 'test_hands.txt'))

@pytest.fixture(scope='module')
def hands_two():
    return read_hands_two(os.path.join('test', 'test_hands.txt'))


def test_read_hands(hands):
    expected_hand = [
        Hand(hand = '32T3K', bid = 765),
        Hand(hand = 'T55J5', bid = 684),
        Hand(hand = 'KK677', bid = 28),
        Hand(hand = 'KTJJT', bid = 220),
        Hand(hand = 'QQQJA', bid = 483)
    ]

    assert hands == expected_hand


def test_total_winnings(hands):
    assert get_total_winnings(hands) == 6440
    

def test_total_winnings_two(hands_two):
    assert get_total_winnings(hands_two) == 5905