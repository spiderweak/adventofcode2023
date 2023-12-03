"""
    Solution to day 1 of Advent of Code

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
        print(output_one)
        logging.info(f"Part 1 solution is : {output_one}")
    except NotImplementedError:
        logging.error("The part 1 solution is not implemented yet")

    try:
        output_two = part_two(input_file)
        print(output_two)
        logging.info(f"Part 2 solution is : {output_two}")
    except NotImplementedError:
        logging.error("The part 2 solution is not implemented yet")

def part_one(input_file: str) -> int:
    """
        Part One Implementation

        Input:
            file(str): Input file path

        Output:
            result: Ouput value, usually str or integer
    """
    a=0
    b=0
    c=0
    with open(input_file) as file:
        for line in file:
            first_digit = False
            for char in line:
                if char.isdigit() and not first_digit:
                    a=char
                    first_digit=True
                if char.isdigit():
                    b=char
            c+= int(f'{a}{b}')
    return c



def part_two(input_file: str) -> int:
    """
        Part Two Implementation

        Input:
            file(str): Input file path

        Output:
            result(str): Ouput value, usually str or integer
    """
    a=0
    b=0
    c=0

    digit_list = ['1','2','3','4','5','6', '7', '8', '9']
    letters_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    first_corresponding_dict = {}
    last_corresponding_dict = {}
    with open(input_file) as file:
        for line in file:
            a=0
            b=0

            first_corresponding_dict = {}
            last_corresponding_dict = {}
            for digit in digit_list:
                if line.find(digit) >= 0:
                    first_corresponding_dict[digit] = line.find(digit)
                if line.rfind(digit) >=0:
                    last_corresponding_dict[digit] = line.rfind(digit)

            for letters in letters_list:
                if line.find(letters) >= 0:
                    first_corresponding_dict[letters] = line.find(letters)
                if line.rfind(letters) >=0:
                    last_corresponding_dict[letters]  = line.rfind(letters)
            
            a=min(first_corresponding_dict, key=first_corresponding_dict.get) # type: ignore
           
            b=max(last_corresponding_dict, key=last_corresponding_dict.get)# type: ignore
            
            if not a.isdigit():
                a = str(letters_list.index(a))
            if not b.isdigit():
                b = str(letters_list.index(b))
            c+= int(f'{a}{b}')
    
    return c



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
                        default='Input/day_01/input',
                        nargs='?')
    options = parser.parse_args()

    return options


if __name__ == '__main__':
    main()
