import pytest

from main import (
    get_lowest_location,
    get_maps, 
    get_seeds, 
    get_seeds_two,
    to_from
)
from interval import Interval, IntervalList


@pytest.fixture
def almanac():
    return """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def test_get_seeds(almanac):
    seeds = get_seeds(almanac)

    assert seeds == [79, 14, 55, 13]


def test_get_maps(almanac):
    maps = get_maps(almanac)

    assert maps == {
        'seed': {
            'destination': 'soil',
            'map': [
                (50, 98, 2),
                (52, 50, 48)
            ]
        },
        'soil': {
            'destination': 'fertilizer',
            'map': [
                (0, 15, 37),
                (37, 52, 2),
                (39, 0, 15)
            ]
        },
        'fertilizer': {
            'destination': 'water',
            'map': [
                (49, 53, 8),
                (0, 11, 42),
                (42, 0, 7),
                (57, 7, 4)
            ]
        },
        'water': {
            'destination': 'light',
            'map': [
                (88, 18, 7),
                (18, 25, 70)
            ]
        },
        'light': {
            'destination': 'temperature',
            'map': [
                (45, 77, 23),
                (81, 45, 19),
                (68, 64, 13)
            ]
        },
        'temperature': {
            'destination': 'humidity',
            'map': [
                (0, 69, 1),
                (1, 0, 69)
            ]
        },
        'humidity': {
            'destination': 'location',
            'map': [
                (60, 56, 37),
                (56, 93, 4)
            ]
        }
    }


def test_to_from(almanac, elements=[79, 14, 55, 13], source='seed', destination='location'):
    maps = get_maps(almanac)
    location = to_from(elements, source, destination, maps)

    assert location == [82, 43, 86, 35]


def test_get_lowest_location(almanac):
    lowest_location = get_lowest_location(almanac)

    assert lowest_location == 35

# Part Two
def test_seeds_two(almanac):
    seeds = get_seeds_two(almanac)

    assert seeds == IntervalList([
        Interval(79, 92),
        Interval(55, 67)
    ])
