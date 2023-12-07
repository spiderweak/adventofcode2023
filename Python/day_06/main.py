"""
    Skeleton to my solutions to Advent of Code 2023

    We usually need to parse a file, the file will be put in the Input/day_XX folder under input
"""

import argparse
import logging
from pprint import pprint

from typing import List, Dict, Union

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
    data = dict()
    with open(input_file) as file:
        for line in file:
            for k,v in process_line(line).items():
                data[k] = v

    return data
        


def process_line(line):
    """
        This is used to process a single line if necessary
    """
    data = dict()

    [header, values] = line[:-1].split(":")

    data[header] = [int(value) for value in values.split(" ") if value != ""]

    return data


def part_one(data: Dict[str, List]):
    """
        Part One Implementation

        Input:
            file(str): Input file path

        Output:
            result: Ouput value, usually str or integer
    """
    output = 1
    for race in range(len(data["Time"])):
        output *= break_record(data["Time"][race], data["Distance"][race])

    return output

def break_record(time, distance):
    speed_list = []
    for speed in range(time+1):
        if (time - speed)*speed > distance:
            speed_list.append(speed)
            break

    for speed in range(time+1, 0, -1):
        if (time - speed)*speed > distance:
            speed_list.append(speed)
            break

    return speed_list[1]-speed_list[0]+1


def part_two(data: dict) -> int:
    """
        Part Two Implementation

        Input:
            file(str): Input file path

        Output:
            result(str): Ouput value, usually str or integer
    """
    timer = ""
    distancer = ""
    for time in data["Time"]:
        timer += str(time)

    for distance in data["Distance"]:
        distancer += str(distance)

    return break_record(int(timer), int(distancer))


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
                        default="Input/day_06/input",
                        nargs='?')
    options = parser.parse_args()

    return options


if __name__ == '__main__':
    main()