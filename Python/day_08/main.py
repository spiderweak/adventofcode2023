"""
    Skeleton to my solutions to Advent of Code 2023

    We usually need to parse a file, the file will be put in the Input/day_XX folder under input
"""

import argparse
import logging
import re
from pprint import pprint
from collections import deque

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
            data.append(process_line(line))
    return data


def process_line(line):
    """
        This is used to process a single line if necessary
    """
    # Regex pattern to match the line structure
    pattern = r'(\w+)\s*=\s*\((\w+),\s*(\w+)\)'

    # Using regex to search for the pattern in the line
    match = re.search(pattern, line)

    if match:
        # Extracting the matched groups
        id, left, right = match.groups()
        return {id : (left,right)}
    else:
        return line.split()

def part_one(data: list) -> int:
    """
        Part One Implementation

        Input:
            file(str): Input file path

        Output:
            result: Ouput value, usually str or integer
    """
    pattern = data[0][0]
    graph = dict()
    for line in data[2:]:
        for key,value in line.items():
            graph[key] = value

    count = 0

    current = "AAA"
    destination = "ZZZ"

    directions = deque()

    for char in pattern:
        directions.append(char)

    while current != destination:
        direction = directions.popleft()
        if direction == "L":
            current = graph[current][0]
        elif direction == "R":
            current = graph[current][1]
        count +=1
        directions.append(direction)

    return count

def part_two(data: list) -> int:
    """
        Part Two Implementation

        Input:
            file(str): Input file path

        Output:
            result(str): Ouput value, usually str or integer
    """

    pattern = data[0][0]
    graph = dict()
    for line in data[2:]:
        for key,value in line.items():
            graph[key] = value

    current = []
    for key in graph.keys():
        if key.endswith("A"):
            current.append(key)


    first_exits = []
    for node in current:
        current_node = node

        directions = deque()
        count = 0

        for char in pattern:
            directions.append(char)

        while not current_node.endswith("Z"):
            direction = directions.popleft()
            if direction == "L":
                current_node = graph[current_node][0]
            elif direction == "R":
                current_node = graph[current_node][1]
            count +=1
            directions.append(direction)

        first_exits.append(count)

    logging.info(f"first exits encountered : {first_exits}")
    import math
    logging.info(f"giving a shot to lcm {math.lcm(*first_exits)}")
    return math.lcm(*first_exits)

def keepgoing(current):
    for node in current:
        if not node.endswith("Z"):
            return True
    return False

    """
def keepgoing(current, cycle=0):

    Analysis implementation

    stop = []

    for node in current:
        if node.endswith("Z"):
            print("Z encountered on cycle :", cycle)
            stop.append(True)
        else:
            stop.append(False)

    if False in stop:
        return True
    """

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