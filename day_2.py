import argparse

from icecream import ic

parser = argparse.ArgumentParser(description="")
parser.add_argument("--input", default=".", type=str, help="Module input data")

MAX_AMOUNTS = {"red": 12, "green": 13, "blue": 14}
MAX_RED_AMOUNT = 12
MAX_GREEN_AMOUNT = 13
MAX_BLUE_AMOUNT = 14


def read_file(file: str) -> list:
    with open(file, "r", encoding="utf-8") as f:
        input_data = f.readlines()
    return [i.strip() for i in input_data]

# PART 1

def process_game_1(input_str: str) -> int:
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

# PART 2

def process_game_2(input_str: str) -> int:
    game_number, game_log = input_str.split(":")

    min_count = {"red": 0, "green": 0, "blue": 0}
    for game_round in game_log.split(";"):
        for phase in game_round.split(","):
            num, color = phase.strip().split(" ")

            if int(num) > min_count[color]:
                min_count[color] = int(num)

    return compute_score(min_count)


def compute_score(count: dict):
    score = 1
    for color, num in count.items():
        score = score * num
    return score


def main():
    ic("Program Started")

    args = parser.parse_args()
    data = read_file(args.input)
    result_1 = []

    for item in data:
        try:
            result_1.append(process_game_1(item))
        except Exception:
            pass

    ic(sum(result_1))

    result_2 = []
    for item in data:
        result_2.append(process_game_2(item))
    ic(sum(result_2))


if __name__ == "__main__":
    main()
