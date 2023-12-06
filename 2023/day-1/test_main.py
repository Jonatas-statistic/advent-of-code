import pytest

from main import (
    get_calibration_value,
    get_calibration_value_part_two,
    sum_calibration_values,
    sum_calibration_values_part_two
)


@pytest.mark.parametrize(
        "text_value,value",
        [
            ('1abc2 ', 12),
            (' pqr3stu8vwx', 38),
            ('a1b2c3d4e5f', 15),
            ('treb7uchet', 77),
            ('   ', 0)
        ])
def test_get_calibration_value(text_value, value):
    assert get_calibration_value(text_value) == value


@pytest.fixture
def calibration_values_amended():
    return [
        '1abc2',
        'pqr3stu8vwx',
        'a1b2c3d4e5f',
        'treb7uchet'
    ]

@pytest.fixture
def calibration_values_parte_two():
    return [
        'two1nine',
        'eightwothree',
        'abcone2threexyz',
        'xtwone3four',
        '4nineeightseven2',
        'zoneight234',
        '7pqrstsixteen'
    ]


def test_sum_calibration_values(calibration_values_amended):
    assert sum_calibration_values(calibration_values_amended) == 142


@pytest.mark.parametrize(
        'text_value,value',
        [
            ('two1nine', 29),
            ('eightwothree', 83),
            ('abcone2threexyz', 13),
            ('xtwone3four', 24),
            ('4nineeightseven2', 42),
            ('zoneight234', 14),
            ('7pqrstsixteen', 76)
        ]
)
def test_get_calibration_value_part_two(text_value, value):
    assert get_calibration_value_part_two(text_value) == value


def test_sum_calibration_values_parte_two(calibration_values_parte_two):
    assert sum_calibration_values_part_two(calibration_values_parte_two) == 281
