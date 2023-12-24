from interval import Interval, IntervalList

from pytest import mark


# Interval

@mark.parametrize(
    'first,last,lt,mt',
    [
        (-1, 1, False, False),
        (-3 , -2, False, True),
        (-3, -1, False, False),
        (0, 2, False, False),
        (1, 3, False, False),
        (3, 5, True, False)
    ]
)
def test_lt(first, last, lt, mt):
    interval = Interval(first=-1, last=1)
    other_interval = Interval(first=first, last=last)

    assert (interval < other_interval) == lt
    assert (interval > other_interval) == mt


# IntervalList

def test_insert_in_empty():
    inter_list = IntervalList()
    interval = Interval(-1, 1)

    inter_list.insert(interval)

    assert inter_list._list == [interval]


@mark.parametrize(
    'first,last,expected_list',
    [
        (-2, -1, [(-2, 1), (3, 4)]),
        (2, 2, [(0, 4)]),
        (5, 6, [(0, 1), (3, 6)]),
        (6, 8, [(0, 1), (3, 4), (6, 8)])
    ]
)
def test_insert(first, last, expected_list):
    first_interval = Interval(0, 1)
    last_interval = Interval(3, 4)
    interval = Interval(first, last)
    
    inter_list = IntervalList()
    inter_list.insert(first_interval)
    inter_list.insert(last_interval)
    inter_list.insert(interval)

    base_inter_list = IntervalList()
    for pair in expected_list:
        base_inter_list.insert(Interval(*pair))

    assert inter_list == base_inter_list