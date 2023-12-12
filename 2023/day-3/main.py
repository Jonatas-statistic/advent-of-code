import re

from functools import partial
from typing import Iterator


def is_part_number(match_number: re.Match, engine_schematic_point: str, width: int):
    start, final = match_number.span()

    left_diff = start - width
    right_diff = final + width

    if start > 0:
        if engine_schematic_point[start - 1] != '.':
            return True
    
    if engine_schematic_point[final] != '.':
        return True

    if left_diff == 0:
        for character in engine_schematic_point[: final - width + 1]:
            if character != '.':
                return True
        
    if left_diff > 0:
        for character in engine_schematic_point[left_diff - 1: final - width + 1]:
            if character != '.':
                return True
            
    if right_diff < len(engine_schematic_point):
        for character in engine_schematic_point[start + width - 1: right_diff + 1]:
            if character != '.':
                return True
        
    return False


def get_match_part_numbers(engine_schematic: str):
    lines = engine_schematic.split('\n')
    
    engine_schematic_point = engine_schematic.replace('\n', '.') + '.'
    width = len(lines[0]) + 1 # because each line has '.' as the last character
    
    match_numbers = re.finditer(r'\d+', engine_schematic_point)

    # filter part numbers
    this_is_part_number = partial(
        is_part_number, 
        engine_schematic_point=engine_schematic_point, 
        width=width
    )
    match_part_numbers = list(filter(this_is_part_number, match_numbers))
    
    return match_part_numbers
    
def get_part_numbers(engine_schematic: str):
    match_part_numbers = get_match_part_numbers(engine_schematic)
    part_numbers = [int(mpn.group()) for mpn in match_part_numbers]

    return part_numbers


# Part Two

def is_adjacent(location: int, width: int, match_number: re.Match):
    start, final = match_number.span()

    if start - 1 <= location - width <= final:
        return True
    if (location == start - 1) or (location == final):
        return True
    if start - 1 <= location + width <= final:
        return True
    
    return False

def get_adjacent_part_numbers(location: int, match_part_numbers: Iterator[re.Match], width: int):
    adjacent_part_numbers = []

    for match_number in match_part_numbers:
        if is_adjacent(location, width, match_number):
            adjacent_part_numbers.append(int(match_number.group()))

    return adjacent_part_numbers

def get_gears(engine_schematic: str) -> list[dict]:
    lines = engine_schematic.split('\n')
    width = len(lines[0]) + 1 # because each line has '.' as the last character
    
    gear_candidates = re.finditer(r'\*', engine_schematic)
    
    match_part_numbers = get_match_part_numbers(engine_schematic)
    
    gears = []
    for gear_candidate in gear_candidates:
        adjacent_part_numbers = get_adjacent_part_numbers(
            location=gear_candidate.span()[0],
            match_part_numbers=match_part_numbers,
            width=width
        )
        
        if len(adjacent_part_numbers) == 2:
            gears.append({
                'location': gear_candidate.span()[0],
                'part_numbers': adjacent_part_numbers,
                'gear_ratio': adjacent_part_numbers[0] * adjacent_part_numbers[1]
            })

    return gears



if __name__ == '__main__':
    with open('engine_schematic.txt') as f:
        engine_schematic = f.read()

    part_numbers = get_part_numbers(engine_schematic)

    # Part numbers
    print(f'Part One: {sum(part_numbers)}')

    # Part Two
    gears = get_gears(engine_schematic)
    gear_ratios = [gear['gear_ratio'] for gear in gears]
    
    print(f'Part Two: {sum(gear_ratios)}')