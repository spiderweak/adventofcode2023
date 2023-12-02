"""
    Skeleton to my solutions to Advent of Code 2023

    We usually need to parse a file, the file will be put in the Input/day_XX folder under input
"""

import argparse
import logging

def main():
    """
        This is the entry point in the program

        The default function is getting the puzzle, trying to out
    """
    logging.basicConfig(level=logging.INFO)

    options = parse_args()

    input_file = options.input

    parse_file(input_file)

    try:
        output_one = part_one(input_file)
        logging.info(f"Part 1 solution is : {output_one}")
    except NotImplementedError:
        logging.error("The part 1 solution is not implemented yet")

    try:
        output_two = part_two(input_file)
        logging.info(f"Part 2 solution is : {output_two}")
    except NotImplementedError:
        logging.error("The part 2 solution is not implemented yet")


def parse_file(input_file):
    """
        This is a pre_coded line parser in case it is needed
    """
    with open(input_file) as file:
        for line in file:
            process_line(line)


def process_line(line):
    """
        This is used to process a single line if necessary
    """
    raise NotImplementedError


def part_one(file: str) -> int:
    """
        Part One Implementation

        Input:
            file(str): Input file path

        Output:
            result: Ouput value, usually str or integer
    """
    raise NotImplementedError


def part_two(file: str) -> int:
    """
        Part Two Implementation

        Input:
            file(str): Input file path

        Output:
            result(str): Ouput value, usually str or integer
    """
    raise NotImplementedError


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