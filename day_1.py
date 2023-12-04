import argparse
import re

from icecream import ic

from utils import read_file  # , timer

parser = argparse.ArgumentParser(description="")
parser.add_argument("--input", default=".", type=str, help="Module input data")

DIGIT_NAMES = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


# @timer(1, 1, 2023)
def find_calibration_digits(input_str: str) -> int:
    digit_regex = r"\d"
    first_digit = re.search(digit_regex, input_str)
    last_digit = re.search(digit_regex, input_str[::-1])
    return int(first_digit.group() + last_digit.group())


# @timer(2, 1, 2023)
def find_calibration_numbers_names(input_str: str) -> int:
    input_str_reverse = input_str[::-1]
    number_name = [(re.compile(x), y) for x, y in DIGIT_NAMES.items()]

    regex_matches = [(rx[0].search(input_str), rx[1]) for rx in number_name]
    only_numbers = [
        (r[0].group(), r[0].start(), r[1])
        for r in regex_matches
        if r[0] is not None
    ]

    number_name_rev = [
        (re.compile(a[::-1]), b) for a, b in DIGIT_NAMES.items()
    ]
    last_matches = [
        (rx[0].search(input_str_reverse), rx[1]) for rx in number_name_rev
    ]
    only_numbers_rev = [
        (r[0].group(), len(input_str_reverse) - r[0].start() - 1, r[1])
        for r in last_matches
        if r[0] is not None
    ]

    only_numbers.extend(only_numbers_rev)

    digit_regex = r"\d"
    first_digit_match = re.search(digit_regex, input_str)
    if first_digit_match:
        only_numbers.append(
            (first_digit_match.group(), first_digit_match.start())
        )

        last_digit_match = re.search(digit_regex, input_str_reverse)
        last_digit_match_pos = (
            len(input_str_reverse) - last_digit_match.start() - 1
        )
        only_numbers.append((last_digit_match.group(), last_digit_match_pos))

    sorted_by_pos = sorted(only_numbers, key=lambda tup: tup[1])

    first_number_value = sorted_by_pos[0][0]
    if first_number_value.isdigit():
        first_number = first_number_value
    else:
        first_number = sorted_by_pos[0][2]

    last_number_value = sorted_by_pos[-1][0]
    if last_number_value.isdigit():
        last_number = last_number_value
    else:
        last_number = sorted_by_pos[-1][2]

    return int(first_number + last_number)


def main():
    ic("Program Started")

    args = parser.parse_args()
    data = read_file(args.input)
    result = []
    for item in data:
        result.append(find_calibration_numbers_names(item))
    ic(sum(result))


if __name__ == "__main__":
    main()
