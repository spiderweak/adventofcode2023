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

def parse_game(game_line: str) -> dict:
    """
        Converts a line describing a round to a dictionary
    """
    [game,content] = game_line.split(':')

    game_id = int(game[5:])

    content = content[:-1].split(':') # gets rid of the \n and split each round in list

    rounds = []

    for round in content[0].split(';'):
        elements = round.split(',')
        data = {}
        for element in elements:
            [value, color] = element[1:].split(' ')
            data[color] = data.get(color, 0) + int(value)
        rounds.append(data)

    return {"game_id": game_id,
            "rounds": rounds}



def part_one(input_file: str) -> int:
    """
        Part One Implementation

        Input:
            input_file(str): Input file path

        Output:
            result: Ouput value, usually str or integer
    """
    MAX_COLOR_VALUE = {'red': 12, 'green': 13, 'blue': 14}
    output = 0
    with open(input_file) as file:
        for line in file:
            game = parse_game(line)
            try:
                for round in game['rounds']:
                    for k,v in round.items():
                        if v>MAX_COLOR_VALUE[k]:
                            raise ValueError
                output += game['game_id']
            except ValueError:
                pass
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
            game = parse_game(line)
            for round in game['rounds']:
                for color,value in round.items():
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