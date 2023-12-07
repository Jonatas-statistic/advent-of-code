import re

from functools import partial


re_id = re.compile(r'Game (\d*)')
re_red = re.compile(r'(\d*) red')
re_green = re.compile(r'(\d*) green')
re_blue = re.compile(r'(\d*) blue')


def get_game_data(game: str):
    # take the id
    id = re_id.findall(game)[0]
    # take a list with combinatio of red, green and blue quantities    
    handfuls_text = game.split(';')
    handfuls = []
    for handful_text in handfuls_text:
        red = re_red.findall(handful_text)
        green = re_green.findall(handful_text)
        blue = re_blue.findall(handful_text)
        
        handful = {
            'red': int(red[0]) if red else 0,
            'green': int(green[0]) if green else 0,
            'blue': int(blue[0]) if blue else 0
        }
        handfuls.append(handful)

    return {'id': int(id), 'handfuls': handfuls}


def is_possible(game:dict, lim_red: int, lim_green: int, lim_blue: int):
    for handful in game['handfuls']:
        if handful['red'] > lim_red or handful['green'] > lim_green or handful['blue'] > lim_blue:
            return False
    return True

def get_possible_ids(games: str, lim_red: int, lim_green: int, lim_blue: int):
    game_data = list(map(get_game_data, games.split('\n')))

    that_is_possible = partial(is_possible, lim_red=lim_red, lim_green=lim_green, lim_blue=lim_blue)
    possible_games = list(filter(that_is_possible, game_data))
    possible_ids = [game['id'] for game in possible_games]

    return possible_ids


def calculate_power(game:dict):
    handfuls = game['handfuls']
    
    min_red = max([handful['red'] for handful in handfuls])
    min_green = max([handful['green'] for handful in handfuls])
    min_blue = max([handful['blue'] for handful in handfuls])
    
    return min_red * min_green * min_blue

def get_powers(games:str):
    game_data = list(map(get_game_data, games.split('\n')))

    powers = [calculate_power(game) for game in game_data]
    return powers


if __name__ == '__main__':
    with open('games.txt') as f:
        games = f.read()

    possible_ids = get_possible_ids(
        games,
        lim_red=12,
        lim_green=13,
        lim_blue=14 
    )
    result = sum(possible_ids)

    print(f'Part One: {result}')

    # Part Two
    powers = get_powers(games)

    print(f'Part Two: {sum(powers)}')