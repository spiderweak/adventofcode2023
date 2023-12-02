"""
    Solution to day 2 of Advent of code

    We'll parse the file, and output the correct value for part_1 and part_2
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



def part_one(input_file: str) -> str:
    """
        Part One Implementation

        Input:
            file(str): Input file path

        Output:
            result: Ouput value, usually str or integer
    """
    MAX_COLOR_VALUE = {'red': 12, 'green': 13, 'blue': 14}
    output = 0
    with open(input_file) as file:
        for line in file:
            error = False
            data = line.split(':')
            data = [data[0]] + data[1][:-1].split(';') # gets rid of the \n and split each round in list
            #    Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
            game_id = int(data[0][5:])

            for round in data[1:]:
                elements = round.split(',')
                for element in elements:
                    [value, color] = element[1:].split(' ')
                    if MAX_COLOR_VALUE[color] < int(value):
                        error = True

            if not error:
                output += game_id

    return output


def part_two(input_file: str) -> int:
    """
        Part Two Implementation

        Input:
            file(str): Input file path

        Output:
            result(str): Ouput value, usually str or integer
    """
    output = 0
    with open(input_file) as file:
        for line in file:
            MAX_COLOR_VALUE = {'red': 0, 'green': 0, 'blue': 0}
            data = line.split(':')
            data = [data[0]] + data[1][:-1].split(';') # gets rid of the \n and split each round in list
            #    Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
            game_id = int(data[0][5:])

            for round in data[1:]:
                elements = round.split(',')
                for element in elements:
                    [value, color] = element[1:].split(' ')
                    if MAX_COLOR_VALUE[color] < int(value):
                        MAX_COLOR_VALUE[color] = int(value)

            temp_output = 1
            for k,v in MAX_COLOR_VALUE.items():
                temp_output = temp_output*v

            output+=temp_output


    return output


def parse_args():
    """
        This is an argument parser in case another input is necessary

        In the skeleton, by default, the parsed file is the input file in the day's folder
    """

    import datetime

    default_value=f"Input/day_{datetime.datetime.today().strftime('%d')}/input"
    parser = argparse.ArgumentParser(description='Process Day 02 input')
    parser.add_argument('input',
                        help='Input file',
                        default='Input/day_02/input',
                        nargs='?')
    options = parser.parse_args()

    return options


if __name__ == '__main__':
    main()