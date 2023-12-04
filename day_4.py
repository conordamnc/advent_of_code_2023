import argparse
import math
from collections import Counter

from icecream import ic

from utils import read_file, timer

parser = argparse.ArgumentParser(description="")
parser.add_argument("--input", default=".", type=str, help="Module input data")


# PART 1


@timer(1, 4, 2023)
def process_scratchcards(scratchcards_list: list) -> list:
    scores = []
    for scratchcard in scratchcards_list:
        start_of_card, picked_numbers = scratchcard.split("|")
        winning_nums_str = start_of_card.split(":")[1]

        winning_nums = get_card_winning_nums(
            winning_nums_str.strip().split(" "),
            picked_numbers.strip().split(" "),
        )
        if winning_nums:
            scores.append(get_card_score(winning_nums))
    return scores


def get_card_score(winning_nums: list) -> int:
    return int(math.pow(2, len(winning_nums) - 1))


def get_card_winning_nums(winning_nums: list, picked_nums: list) -> list:
    picked_winning_nums = [
        num for num in picked_nums if num in winning_nums and num
    ]
    return picked_winning_nums


# PART 2


def get_scratchcard_scores(scratchcards_list: list) -> list:
    scratchcard_scores = []
    for scratchcard in scratchcards_list:
        start_of_card, picked_numbers = scratchcard.split("|")
        card_num, winning_nums_str = start_of_card.split(":")

        winning_nums = get_card_winning_nums(
            winning_nums_str.strip().split(" "),
            picked_numbers.strip().split(" "),
        )
        scratchcard_scores.append((card_num, winning_nums))

    return scratchcard_scores


@timer(2, 4, 2023)
def process_scratchcards_2(scratchcards_list: list) -> list:
    scratchcard_scores = get_scratchcard_scores(scratchcards_list)
    final_counts = Counter(i[0] for i in scratchcard_scores)

    for index, card in enumerate(scratchcard_scores):
        game_name = card[0]
        amount_won = len(card[1])

        won_cards = []
        for _ in range(0, final_counts[game_name]):
            if amount_won:
                won_cards = []
                for x in range(index + 1, index + amount_won + 1):
                    won_cards.append(scratchcard_scores[x][0])

            for won_card in won_cards:
                final_counts[won_card] += 1

    return final_counts.total()


def main():
    ic("Program Started")

    args = parser.parse_args()
    data = read_file(args.input)

    scratchcard_scores = process_scratchcards(data)
    ic(sum(scratchcard_scores))

    scratchcard_scores_2 = process_scratchcards_2(data)
    ic(scratchcard_scores_2)


if __name__ == "__main__":
    main()
