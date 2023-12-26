import re
from functools import reduce
from operator import mul


def read_races(directory: str) -> list[dict]:
    with open(directory) as f:
        time_text, distance_text = f.read().split('\n')
    time: list[str] = re.findall(r'\d+', time_text)
    distance: list[str] = re.findall(r'\d+', distance_text)
    # races data
    races: list[dict] = []
    for index in range(len(time)):
        races.append(
            {
                'time': int(time[index]),
                'record_distance': int(distance[index])
            }
        )
    return races


# get number of ways you can beat the record
def get_number_of_ways(race: dict):
    odd = race['time'] % 2
    
    # number of ways you can beat the record
    ways = 1 - odd
    pos = race['time'] // 2 + 1
    while pos * (race['time'] - pos) > race['record_distance']:
        ways += 2
        pos += 1
    return ways


def get_margin_error(races: list[dict]):
    number_of_ways: list[int] = list(map(get_number_of_ways, races))
    margin = reduce(mul, number_of_ways, 1)

    return margin


# Part Two
        
def read_only_one_race(directory: str):
    with open(directory) as f:
        time_text, distance_text = f.read().split('\n')
    time = ''.join(re.findall(r'\d+', time_text))
    distance = ''.join(re.findall(r'\d+', distance_text))
    return {
        'time': int(time),
        'record_distance': int(distance)
    }

def get_number_of_ways_two(race: dict):
    # we distance must be more than race['record_distance'], than:
    #    my_time(race['time'] - my_time) - race['record_distance'] > 0
    delta = race['time'] ** 2 - 4 * race['record_distance']
    #root_1 = (race['time'] - delta ** (0.5)) / 2
    root_2 = (race['time'] + delta ** (0.5)) / 2

    if root_2 - int(root_2) > 0:
        number_of_ways = 1 + race['time'] - 2 * (race['time'] - int(root_2))
    else:
        number_of_ways = 1 + race['time'] - 2 * (race['time'] - int(root_2) + 1)

    return number_of_ways



if __name__ == '__main__':
    races = read_races('races.txt')

    # Part One
    margin_error = get_margin_error(races)
    print(f'First Part: {margin_error}')

    # Part Two
    race = read_only_one_race('races.txt')
    number_of_ways = get_number_of_ways_two(race)
    print(f'Second Part: {number_of_ways}')