import argparse
from collections import Counter
import re

from icecream import ic

parser = argparse.ArgumentParser(description="")
parser.add_argument("--input", default=".", type=str, help="Module input data")


def read_file(file: str) -> list:
    with open(file, "r", encoding="utf-8") as f:
        input_data = f.readlines()
    return [i.strip() for i in input_data]


# PART 1
def find_symbols(matrix: list) -> None:
    symbols = []
    for x in matrix:
        for y in x:
            if not y.isdigit() and y != "." and y not in symbols:
                symbols.append(y)
    ic(symbols)


def get_symbol_locations(schematic: str) -> list:
    symbol_regex = re.compile(r"[=+\-*/$&%#@]")

    symbol_locations = {}
    for index, line in enumerate(schematic):
        for num in symbol_regex.finditer(line):
            symbol_locations[(index, num.start())] = num.group()
    return symbol_locations


def find_correspoding_symbol(
    digit_match: re.Match, line_num: int, symbol_locations: dict
) -> bool:
    symbol_found = False
    for lines in range(-1, 2):
        for x in range(digit_match.start() - 1, digit_match.end() + 1):
            if symbol_locations.get((line_num + lines, x)):
                symbol_found = True
                break
    return symbol_found


def find_part_numbers(schematic: str) -> list:
    digit_regex = re.compile(r"\d+")
    symbol_locations = get_symbol_locations(schematic)

    scores = []
    for index, item in enumerate(schematic):
        for num in digit_regex.finditer(item):
            if find_correspoding_symbol(num, index, symbol_locations):
                scores.append(int(num.group()))
    ic(scores)
    return scores

# PART 2

def find_adjcent_symbols(
    digit_match: re.Match, line_num: int, symbol_locations: dict
) -> list:
    symbol_found = []
    for lines in range(-1, 2):
        for x in range(digit_match.start() - 1, digit_match.end() + 1):
            if symbol_locations.get((line_num + lines, x)):
                symbol_found.append((line_num + lines, x))

    return symbol_found


def get_star_locations(schematic: str) -> list:
    symbol_regex = re.compile(r"[*]")
    star_locations = {}
    for index, line in enumerate(schematic):
        for num in symbol_regex.finditer(line):
            star_locations[(index, num.start())] = num.group()
    return star_locations


def compute_gear_ratio(a: str, b: str) -> int:
    return int(a) * int(b)


def find_gear_ratios(schematic: str) -> list:
    digit_regex = re.compile(r"\d+")
    star_locations = get_star_locations(schematic)
    hits = Counter()
    gear_star_map = {}
    gear_ratios = []
    for index, item in enumerate(schematic):
        for num in digit_regex.finditer(item):
            adjcent_symbols = find_adjcent_symbols(num, index, star_locations)
            for symbol_loc in adjcent_symbols:
                if hits[symbol_loc] > 0:
                    gear_ratios.append(compute_gear_ratio(num.group(), gear_star_map[symbol_loc]))
                    break
                gear_star_map[symbol_loc] = num.group()
                hits[symbol_loc] =  hits[symbol_loc] + 1
            


    breakpoint()
    return gear_ratios

def main():
    ic("Program Started")

    args = parser.parse_args()
    data = read_file(args.input)
    result_1 = []

    # part_numbers = find_part_numbers(data)
    # breakpoint()
    # ic(sum(part_numbers))

    gear_ratios = find_gear_ratios(data)
    ic(sum(gear_ratios))


if __name__ == "__main__":
    main()
