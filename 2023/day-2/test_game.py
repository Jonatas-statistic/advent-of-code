import pytest

from game import get_possible_ids, get_powers


@pytest.fixture
def some_games():
    return """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def test_get_possible_ids(some_games):
    possible_ids = get_possible_ids(some_games, lim_red=12, lim_green=13, lim_blue=14) 
    
    assert possible_ids == [1, 2, 5]
    assert sum(possible_ids) == 8


def test_get_powers(some_games):
    powers = get_powers(some_games)

    assert powers == [48, 12, 1560, 630, 36]
    assert sum(powers) == 2286