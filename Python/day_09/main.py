"""
    Skeleton to my solutions to Advent of Code 2023

    We usually need to parse a file, the file will be put in the Input/day_XX folder under input
"""

import argparse
import logging
from pprint import pprint
from typing import Tuple

def main():
    """
        This is the entry point in the program

        The default function is getting the puzzle, trying to out
    """
    logging.basicConfig(level=logging.INFO)

    options = parse_args()

    input_file = options.input

    data = parse_file(input_file)

    output_one, output_two = process(data)

    try:
        logging.info(f"Part 1 solution is : {output_one}")
    except NotImplementedError:
        logging.error("The part 1 solution is not implemented yet")

    try:
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
            data.append(process_line(line))

    return data


def process_line(line):
    """
        This is used to process a single line if necessary
    """
    return [int(a) for a in line[:-1].split(" ")]


def process(data: list) -> Tuple[int,int]:
    output = 0
    output_2 = 0
    for history in data:
        data_matrix = []
        data_matrix.append(history)
        data_list = history

        while not all_zeroes(data_list):
            data_list = two_pair_diff(data_list)
            data_matrix.append(data_list)
        print(data_matrix)

        output += part_one(data_matrix)
        output_2 += part_two(data_matrix)

    return output,output_2

def two_pair_diff(data_list: list):
    return [b-a for (b,a) in zip(data_list[1:],data_list[:-1])]

def all_zeroes(data_list: list) -> bool:
    for element in data_list:
        if element != 0:
            return False

    return True

def part_one(data_matrix):
    """
        Part One Implementation

        Input:
            file(str): Input file path

        Output:
            result: Ouput value, usually str or integer
    """
    value = 0
    output = 0
    for data_list in reversed(data_matrix):
        value = data_list[-1] + value

    output += value

    return output

def part_two(data_matrix):
    """
        Part Two Implementation

        Input:
            file(str): Input file path

        Output:
            result(str): Ouput value, usually str or integer
    """
    value = 0
    output = 0
    for data_list in reversed(data_matrix):
        value = data_list[0] - value

    output += value

    return output


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