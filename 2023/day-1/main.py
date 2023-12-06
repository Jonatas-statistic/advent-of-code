MAP_REPLACES = [
    ('oneight', '18'),
    ('twone', '21'),
    ('threeight', '38'),
    ('fiveight', '58'),
    ('sevenine', '79'),
    ('eightwo', '82'),
    ('eighthree', '83'),
    ('nineight', '98'),
    ('one', '1'),
    ('two', '2'),
    ('three', '3'),
    ('four', '4'),
    ('five', '5'),
    ('six', '6'),
    ('seven', '7'),
    ('eight', '8'),
    ('nine', '9')
]


def is_decimal(text_num:str):
    return text_num.isdecimal()

def get_calibration_value(value: str):
    numbers = list(filter(is_decimal, value))

    if numbers:
        return int(f'{numbers[0]}{numbers[-1]}')
    return 0


def sum_calibration_values(values: list[str]):
    numbers = list(map(get_calibration_value, values))
    result = sum(numbers)
    
    return result

# Part Two

def get_calibration_value_part_two(value: str):
    for map_replace in MAP_REPLACES:
        value = value.replace(*map_replace)
    
    numbers = list(filter(is_decimal, value))

    if numbers:
        return int(f'{numbers[0]}{numbers[-1]}')
    return 0


def sum_calibration_values_part_two(values: list[str]):
    numbers = list(map(get_calibration_value_part_two, values))
    result = sum(numbers)
    
    return result


if __name__ == '__main__':
    with open('calibration_values.txt') as f:
        lines = f.readlines()
        
        result = sum_calibration_values(lines)
        print(f'Part One: {result}')

        # Part Two
        result2 = sum_calibration_values_part_two(lines)
        print(f'Part Two: {result2}')