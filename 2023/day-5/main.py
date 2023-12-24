import re
import time

import psutil

from interval import Interval, IntervalList
from interval_map import ListMap


# -----------------------------

re_source = re.compile(r'(\w+)-to-(\w+) map')
re_numbers = re.compile(r'\d+')

# -----------------------------

def get_source_destination(block: str):
    source, destination = re_source.match(block).groups()
    return source, destination

def get_map_block(block: str):
    _map = []

    lines = block.split('\n')
    for index in range(1, len(lines)):
        line = lines[index]
        map_line_str = re_numbers.findall(line)
        map_line = tuple([int(number) for number in map_line_str])
        _map.append(map_line)

    return _map


# Main functions

def get_seeds(almanac: str) -> list[int]:
    blocks = almanac.split('\n\n')

    seeds_text = re_numbers.findall(blocks[0])
    seeds = [int(number) for number in seeds_text]
    return seeds


def get_maps(almanac: str) -> dict[str|dict]:
    blocks = almanac.split('\n\n')

    maps = dict()
    for index in range(1, len(blocks)):
        block = blocks[index]
        
        source, destination = get_source_destination(block)
        _map = {
            'destination': destination,
            'map': get_map_block(block)
        }
        maps[source] = _map
    
    return maps


def to_from(elements: list[int], source: str, destination: str, maps: dict[str|dict], initial_time = None):
    if not initial_time:
        initial_time = time.time()
    _map = maps[source]

    destination_elements = []
    for element in elements:
        destination_element = None
        for map_line in _map['map']:
            diff = element - map_line[1]
            if 0 <= diff < map_line[2]:
                destination_element = map_line[0] + diff
        if destination_element is None:
            destination_element = element

        destination_elements.append(destination_element)

    if time.time() - initial_time > 15:
        raise TimeoutError('Elapsed time is more than 15 seconds!')

    if _map['destination'] != destination:
        destination_elements = to_from(
            elements=destination_elements,
            source=_map['destination'],
            destination=destination,
            maps=maps,
            initial_time=initial_time
        )

    return destination_elements


def get_lowest_location(almanac: str) -> int:
    seeds = get_seeds(almanac)
    maps = get_maps(almanac)

    locations = to_from(
        elements=seeds,
        source='seed',
        destination='location',
        maps=maps
    )
    
    return min(locations)


# Part Two

def get_seeds_two(almanac: str) -> IntervalList:
    # Limit memory usage to 100 MB
    process = psutil.Process()
    memory_limit = 100 * 1024 * 1024

    # Limit time elapsed
    initial_time = time.time()

    # Main code
    seeds = IntervalList()
    seed_pairs = get_seeds(almanac)

    for idx in range(0, len(seed_pairs), 2):
        first = seed_pairs[idx]
        last = seed_pairs[idx + 1] + first - 1
        seed_interval = Interval(first, last)
        seeds.insert(seed_interval)

        # Check memory usage
        memory_usage = process.memory_info().rss
        if memory_usage > memory_limit:
            raise MemoryError(f'Memory limit exceeded! Index: {idx}')

        # Check time elapsed
        if time.time() - initial_time > 15:
            raise TimeoutError('Elapsed time is more than 15 seconds!')

    return seeds



if __name__ == '__main__':
    with open('almanac.txt') as f:
        almanac = f.read()

    # Part One
    lowest_location = get_lowest_location(almanac)
    print(f'Part One (lowest location number): {lowest_location}')

    # Part Two
    seeds = get_seeds_two(almanac)
    maps = ListMap(almanac)
    
    locations = maps.convert_interval_list(seeds)
    print(f'Part Two (lowest location with pair numbers): {locations.min()}')