import pytest

from main import (
    read_races, get_number_of_ways, get_margin_error, 
    read_only_one_race, get_number_of_ways_two
)

@pytest.fixture
def races():
    return read_races('test_races.txt')

def test_read_races(races):
    assert races == [
        {'time': 7, 'record_distance': 9},
        {'time': 15, 'record_distance': 40},
        {'time': 30, 'record_distance': 200},
    ]

def test_number_of_ways(races):
    assert get_number_of_ways(races[0]) == 4
    assert get_number_of_ways(races[1]) == 8
    assert get_number_of_ways(races[2]) == 9

def test_get_margin_error(races):
    assert get_margin_error(races) == 288


# Part Two
    
@pytest.fixture
def only_race():
    return read_only_one_race('test_races.txt')
        
def test_read_only_one_race(only_race):
    assert only_race == {'time': 71530, 'record_distance': 940200}

def test_number_of_ways_two(only_race):
    assert get_number_of_ways_two(only_race) == 71503