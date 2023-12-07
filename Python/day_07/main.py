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
    with open(input_file) as file:
        #face_cards = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        #sorted(hand, key=lambda value: int(value) if value.isdigit() else face_cards[value])
        # RIP unused lambda
        data_dict = dict()
        for line in file:
            [hand, bid] = process_line(line)
            data_dict[hand] = int(bid)
        return data_dict


def process_line(line):
    """
        This is used to process a single line if necessary
    """
    return line[:-1].split(" ")


def part_one(data: dict) -> int:
    """
        Part One Implementation

        Input:
            file(str): Input file path

        Output:
            result: Ouput value, usually str or integer
    """
    all_hands = [hand for hand in data.keys()]
    sorted_hands = sort_hands(all_hands)

    individual_score = 1
    output = 0
    for hand in sorted_hands:
        output += data[hand]*individual_score
        individual_score +=1

    return output


def sort_hands(hands, part = 1) -> list:
    if len(hands) < 2:
        return hands
    else:
        pivot = hands[-1]
        lhands = []
        rhands = []
    for hand in hands[:-1]:
        if rwin(hand, pivot, part = part):
            lhands.append(hand)
        else:
            rhands.append(hand)

    return sort_hands(lhands, part = part) + [pivot] + sort_hands(rhands, part = part)

def rwin(hand_1, hand_2, part = 1):
    if score(hand_1, part = part) < score(hand_2, part = part):
        return True
    elif score(hand_1, part = part) > score(hand_2, part = part):
        return False
    else:
        if part == 1:
            cards = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        elif part == 2:
            cards = {'T': 10, 'J': 0, 'Q': 12, 'K': 13, 'A': 14}
        else:
            raise ValueError("Part is either 1 or 2")
        for i in range(1,10):
            cards[str(i)] = i
        for a,b in zip(hand_1, hand_2):
            if cards[a] < cards[b]:
                return True
            elif cards[a] > cards[b]:
                return False

    raise ValueError("Hands are equal")

def score(hand, part = 1):
    cards = dict()
    j=0
    for card in hand:
        cards[card] = cards.get(card, 0) + 1

    if part == 2:
        j = cards.pop('J', 0)

    for card in cards.keys():
        cards[card] = str(cards[card])

    score = sorted(list(cards.values()))

    try:
        score[-1] = str(int(score[-1])+j)
    except IndexError:
        score = ['5']

    match ''.join(score):
        case "11111":
            return 1
        case "1112":
            return 2
        case "122":
            return 3
        case "113":
            return 4
        case "23":
            return 5
        case "14":
            return 6
        case "5":
            return 7
        case _:
            raise ValueError


def part_two(data) -> int:
    """
        Part Two Implementation

        Input:
            file(str): Input file path

        Output:
            result(str): Ouput value, usually str or integer
    """
    all_hands = [hand for hand in data.keys()]
    sorted_hands = sort_hands(all_hands, part = 2)

    individual_score = 1
    output = 0
    for hand in sorted_hands:
        output += data[hand]*individual_score
        individual_score +=1

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