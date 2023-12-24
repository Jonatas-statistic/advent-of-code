from interval_map import SingleMap, IntervalMap, ListMap
from interval import Interval, IntervalList
from main import get_seeds_two

from pytest import fixture, mark
from test.test_main import almanac


# SingleMap

@mark.parametrize(
    'number,is_into',
    [
        (-1, False),
        (1, True),
        (4, False)
    ]
)
def test_into_source(number, is_into):
    single_map = SingleMap(10, 0, 4)

    assert single_map.into_source(number) == is_into

@mark.parametrize(
    'number,expected_number',
    [
        (0, 10),
        (1, 11),
        (3, 13)
    ]
)
def test_single_map_convert(number, expected_number):
    single_map = SingleMap(10, 0, 4)

    assert single_map.convert(number) == expected_number

@mark.parametrize(
    'interval,converted_interval',
    [
        (Interval(-3, -1), None),
        (Interval(-3, 1), Interval(10, 11)),
        (Interval(-3, 4), Interval(10, 13)),
        (Interval(2, 5), Interval(12, 13)),
        (Interval(4, 6), None)
    ]
)
def test_single_map_convert_interval(interval, converted_interval):
    single_map = SingleMap(10, 0, 4)

    assert single_map.convert_interval(interval) == converted_interval


# IntervalMap
@fixture
def interval_map():
    block = """source-to-destination map:
50 98 2
52 50 48
"""
    return IntervalMap(block)

def test_interval_map(interval_map):
    assert interval_map._list[0] == SingleMap(0, 0, 50)
    assert interval_map._list[1] == SingleMap(52, 50, 48)
    assert interval_map._list[2] == SingleMap(50, 98, 2)
    assert interval_map._list[3] == SingleMap(100, 100, float('Inf'))

@mark.parametrize(
    'number,converted_number',
    [
        (25, 25),
        (55, 57),
        (99, 51),
        (100, 100)
    ]
)
def test_interval_map_convert(number, converted_number, interval_map):
    assert interval_map.convert(number) == converted_number

@mark.parametrize(
    'interval,converted_interval',
    [
        (Interval(25, 55), IntervalList([Interval(25, 49), Interval(52, 57)])),
        (Interval(55, 99), IntervalList([Interval(57, 99), Interval(50, 51)])),
        (Interval(99, 100), IntervalList([Interval(51, 51), Interval(100, 100)]))
    ]
)
def test_interval_map_convert_interval(interval, converted_interval, interval_map):
    assert interval_map.convert_interval(interval) == converted_interval


def test_list_map_convert_interval_list_min(almanac):
    interval_list = get_seeds_two(almanac)
    list_map = ListMap(almanac)
    converted_list = list_map.convert_interval_list(interval_list)

    assert converted_list.min() == 46