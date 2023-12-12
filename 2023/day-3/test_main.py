import pytest

from functools import cache
from re import Match

from main import (
    get_adjacent_part_numbers, get_gears, get_match_part_numbers, get_part_numbers, is_adjacent
)


@pytest.fixture
def ex_engine_schematic():
    return """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

@cache
@pytest.fixture
def match_part_numbers(ex_engine_schematic):
    return get_match_part_numbers(ex_engine_schematic)

@cache
@pytest.fixture
def part_numbers(ex_engine_schematic):
    return get_part_numbers(ex_engine_schematic)


@pytest.mark.parametrize(
    'number',
    [467, 35, 633, 617, 592, 755, 664, 598]
)
def test_get_part_numbers_has(number, part_numbers):
    assert number in part_numbers

@pytest.mark.parametrize(
    'number',
    [58, 114]
)
def test_get_part_numbers_hasnt(number, part_numbers):
    assert number not in part_numbers

def test_sum_get_part_numbers_sum(part_numbers):
    assert sum(part_numbers) == 4361


@pytest.mark.parametrize(
    'location, number_1, number_2',
    [
        (14, 467, 35),
        (93, 755, 598)
    ]
)
def test_get_adjacent_part_numbers(location, number_1, number_2, match_part_numbers, width=11):
    adjacent_part_numbers = get_adjacent_part_numbers(location, match_part_numbers, width)

    assert len(adjacent_part_numbers) == 2
    assert number_1 in adjacent_part_numbers
    assert number_2 in adjacent_part_numbers

def test_get_gears(ex_engine_schematic):
    gears: list[dict] = get_gears(ex_engine_schematic)

    assert len(gears) == 2

    assert gears[0]['location'] == 14
    assert sorted(gears[0]['part_numbers']) == [35, 467]
    assert gears[0]['gear_ratio'] == 16345

    assert gears[1]['location'] == 93
    assert sorted(gears[1]['part_numbers']) == [598, 755]
    assert gears[1]['gear_ratio'] == 451490