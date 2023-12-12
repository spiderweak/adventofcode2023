"""
    Skeleton to my solutions to Advent of Code 2023

    We usually need to parse a file, the file will be put in the Input/day_XX folder under input
"""

import argparse
import logging

import matplotlib.pyplot as plt
import networkx as nx

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
        return [process_line(line) for line in file]


def process_line(line):
    """
        This is used to process a single line if necessary
    """
    return [char for char in line[:-1]]

def part_one(data) -> int:
    """
        Part One Implementation

        Input:
            file(str): Input file path

        Output:
            result: Ouput value, usually str or integer
    """
    return(processing(data, part = 1))

def processing(data, part = 1) -> int:
    data, lines, columns = expand_galaxy(data)
    graph_data = create_graph(data)
    source_nodes = []
    for node in graph_data.nodes():
        if graph_data.nodes()[node]['value'] == "#":
            source_nodes.append(node)

    output = 0

    for (x_0,y_0) in source_nodes:
        for (x_1,y_1) in source_nodes:
            output += (abs(y_1 - y_0) + abs(x_1 - x_0) + (spaces(x_0, x_1, y_0, y_1, lines, columns) * (1 if part == 1 else 999999)))

    return int(output/2)

def spaces(x_0, x_1, y_0, y_1, lines, columns):
    output = 0
    for column in columns:
        if min(x_0, x_1) < column < max(x_0, x_1):
            output +=1
    for line in lines:
        if min(y_0, y_1) < line < max(y_0, y_1):
            output +=1
    return output


def create_graph(matrix):
    G = nx.Graph()
    for y, row in enumerate(matrix):
        for x, cell in enumerate(row):
            G.add_node((x, y), value = matrix[y][x])
            for n_x, n_y in get_neighbors(matrix, y, x):
                G.add_edge((x, y), (n_x, n_y))

    return G


def visualize_graph(G):
    """
    Visualizes a NetworkX graph.

    Args:
    G (nx.Graph): A NetworkX graph.

    Returns:
    None: Displays the graph using Matplotlib.
    """
    pos = {node: node for node in G.nodes()}

    # Draw the graph using the specified positions
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue")

    plt.show()

def get_neighbors(matrix, y, x):
    neighbors = []
    coords = []
    if (x-1) >= 0:
        coords.append((x-1,y))
    if (y-1) >= 0:
        coords.append((x, y-1))
    if x+1 <= len(matrix):
        coords.append((x+1,y))
    if y+1 <= len(matrix):
        coords.append((x,y+1))
    for n_x, n_y in coords:
        try:
            if matrix[n_y][n_x] in [".", "#" ]:
                neighbors.append((n_x,n_y))
        except IndexError:
            pass
        except KeyError:
            pass
    return neighbors

def expand_galaxy(data):
    data, expand_line = expand_lines(data)
    data = transpose(data)
    data, expand_column = expand_lines(data)
    data = transpose(data)
    return data, expand_line, expand_column

def expand_lines(data):
    rows = []
    new_data = []
    for i, line in enumerate(data):
        count = len([x for x in line if x == "."])
        if count == len(line):
            rows.append(i)
        new_data.append(line)

    return new_data, rows

def transpose(data):
    columns = list(zip(*data))
    return [list(sublist) for sublist in columns]

def part_two(data) -> int:
    """
        Part Two Implementation

        Input:
            file(str): Input file path

        Output:
            result: Ouput value, usually str or integer
    """
    return(processing(data, part = 2))


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