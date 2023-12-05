"""
    Day 4 solution to Advent of Code 2023

    Scratch card
"""

import argparse
import logging
from pprint import pprint

def main():
    """
        This is the entry point in the program

        The default function is getting the puzzle, trying to out
    """
    logging.basicConfig(level=logging.INFO)

    options = parse_args()

    input_file = options.input

    data = parse_file(input_file)

    try:
        output_one = part_one(data)
        logging.info(f"Part 1 solution is : {output_one}")
    except NotImplementedError:
        logging.error("The part 1 solution is not implemented yet")

    try:
        output_two = part_two(data)
        logging.info(f"Part 2 solution is : {output_two}")
    except NotImplementedError:
        logging.error("The part 2 solution is not implemented yet")


def parse_file(input_file):
    """
        This is a pre_coded line parser in case it is needed
    """
    data = []
    with open(input_file) as file:
        for line in file:
            data.append(process_line(line[:-1]))
    return data


def process_line(line):
    """
        This is used to process a single line if necessary
    """
    processed_data = dict()
    [card, data] = line.split(":")
    [victory, numbers] = data.split("|")

    card_id = card.split(" ")[-1]
    victory_set = set(victory.split(" "))
    victory_set.remove("")
    numbers_set = set(numbers.split(" "))
    numbers_set.remove("")

    processed_data['card_id'] = int(card_id)
    processed_data['victory'] = victory_set
    processed_data['numbers'] = numbers_set

    return processed_data


def part_one(data: dict) -> int:
    """
        Part One Implementation

        Input:
            file(str): Input file path

        Output:
            result: Ouput value, usually str or integer
    """
    output = 0
    for game in data:
        count = len(game['numbers'].intersection(game['victory']))
        if count > 0:
            output += 2**(count-1)

    return output


def part_two(data: dict) -> int:
    """
        Part Two Implementation

        Input:
            file(str): Input file path

        Output:
            result(str): Ouput value, usually str or integer
    """
    cards_number = dict()
    for game in data:
        cards_number[game['card_id']] = 1

    for game in data:
        count = len(game['numbers'].intersection(game['victory']))
        current_game_id = game['card_id']
        current_number_cards = cards_number[current_game_id]
        for i in range(1, count+1):
            cards_number[current_game_id+i] += current_number_cards

    return sum(v for _,v in cards_number.items())

def parse_args():
    """
        This is an argument parser in case another input is necessary

        In the skeleton, by default, the parsed file is the input file in the day's folder
    """

    import datetime

    default_value=f"Input/day_{datetime.datetime.today().strftime('%d')}/input"
    parser = argparse.ArgumentParser(description='Process Day 1 input')
    parser.add_argument('input',
                        help='Input file',
                        default=default_value,
                        nargs='?')
    options = parser.parse_args()

    return options


if __name__ == '__main__':
    main()