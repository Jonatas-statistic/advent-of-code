import pytest

from hand import Hand, HandTwo


@pytest.mark.parametrize(
    'hand, _type, _hand',
    [
        ('32T3K', '2', '32L3O'),
        ('T55J5', '4', 'L55M5'),
        ('KK677', '3', 'OO677'),
        ('KA345', '1', 'OP345')
    ]
)
def test_get_hand(hand, _type, _hand):
    hand_obj = Hand(hand, bid=0)
    
    assert hand_obj.type == _type
    assert hand_obj.ordered_hand == _hand


@pytest.mark.parametrize(
    'hand, _type, _hand',
    [
        ('32T3K', '2', '32L3O'),
        ('T55J5', '6', 'L5515'),
        ('KK677', '3', 'OO677'),
        ('KA345', '1', 'OP345'),
        ('555J5', '7', '55515'),
        ('J55J5', '7', '15515'),
        ('JJ5J5', '7', '11515'),
        ('TJJJ5', '6', 'L1115')
    ]
)
def test_get_hand_two(hand, _type, _hand):
    hand_obj = HandTwo(hand, bid=0)
    
    assert hand_obj.type == _type
    assert hand_obj.ordered_hand == _hand