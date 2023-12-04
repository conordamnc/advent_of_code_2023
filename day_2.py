import argparse

from icecream import ic

from utils import read_file, timer

parser = argparse.ArgumentParser(description="")
parser.add_argument("--input", default=".", type=str, help="Module input data")

MAX_AMOUNTS = {"red": 12, "green": 13, "blue": 14}
MAX_RED_AMOUNT = 12
MAX_GREEN_AMOUNT = 13
MAX_BLUE_AMOUNT = 14


# PART 1


def game_score_1(input_str: str) -> int:
    game_number, game_log = input_str.split(":")
    for game_round in game_log.split(";"):
        count = {"red": 0, "green": 0, "blue": 0}
        for phase in game_round.split(","):
            num, color = phase.strip().split(" ")
            current_count = count[color]
            if current_count + int(num) > MAX_AMOUNTS[color]:
                raise Exception()
            count[color] = current_count + int(num)
    round_num = game_number.split(" ")[1]
    return int(round_num)


@timer(1, 2, 2023)
def process_game_1(input_list: list) -> list:
    results = []
    for item in input_list:
        try:
            results.append(game_score_1(item))
        except Exception:
            pass
    return results


# PART 2


def game_score_2(input_str: str) -> int:
    game_number, game_log = input_str.split(":")
    min_count = {"red": 0, "green": 0, "blue": 0}
    for game_round in game_log.split(";"):
        for phase in game_round.split(","):
            num, color = phase.strip().split(" ")

            if int(num) > min_count[color]:
                min_count[color] = int(num)

    return compute_score(min_count)


@timer(2, 2, 2023)
def process_game_2(input_list: list) -> int:
    results = []
    for item in input_list:
        results.append(game_score_2(item))
    return results


def compute_score(count: dict):
    score = 1
    for color, num in count.items():
        score = score * num
    return score


def main():
    ic("Program Started")

    args = parser.parse_args()
    data = read_file(args.input)

    result_1 = process_game_1(data)
    ic(sum(result_1))

    result_2 = process_game_2(data)
    ic(sum(result_2))


if __name__ == "__main__":
    main()
