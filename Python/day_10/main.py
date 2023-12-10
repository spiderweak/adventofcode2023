"""
    Skeleton to my solutions to Advent of Code 2023

    We usually need to parse a file, the file will be put in the Input/day_XX folder under input
"""

import argparse
import logging
import networkx as nx
from typing import List, Union
from pprint import pprint
import matplotlib.pyplot as plt
from utils import GraphNode
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

    graph_data = create_graph(data)

    try:
        output_one = part_one(graph_data)
        logging.info(f"Part 1 solution is : {output_one}")
    except NotImplementedError:
        logging.error("The part 1 solution is not implemented yet")

    try:
        output_two = part_two(data, graph_data)
        logging.info(f"Part 2 solution is : {output_two}")
    except NotImplementedError:
        logging.error("The part 2 solution is not implemented yet")


def parse_file(input_file):
    """
        This is a pre_coded line parser in case it is needed
    """
    with open(input_file) as file:
        return [process_line(line.strip()) for line in file]


def process_line(line):
    """
        This is used to process a single line if necessary
    """
    return [None if char =="." else char for char in line]


def create_graph(matrix):
    G = nx.Graph()
    for y, row in enumerate(matrix):
        for x, cell in enumerate(row):
            graph_node = GraphNode(cell)
            if cell is not None:
                G.add_node((x, y), value = graph_node)

    for y, row in enumerate(matrix):
        for x, cell in enumerate(row):
            for n_x, n_y in get_neighbors(G, y, x):
                G.add_edge((x, y), (n_x, n_y))
    return G


def get_neighbors(graph, y, x):
    neighbors = []
    try:
        graph_node: GraphNode = graph.nodes[(x, y)]['value']

        match graph_node.value:
            case "|" :
                try:
                    if graph.nodes[(x, y-1)]['value'].south:
                        neighbors.append((x,y-1))
                except KeyError:
                    pass
                try:
                    if graph.nodes[(x, y+1)]['value'].north:
                        neighbors.append((x,y+1))
                except KeyError:
                    pass
            case "-":
                try:
                    if graph.nodes[(x-1, y)]['value'].east:
                        neighbors.append((x-1,y))
                except KeyError:
                    pass
                try:
                    if graph.nodes[(x+1, y)]['value'].west:
                        neighbors.append((x+1,y))
                except KeyError:
                    pass
            case "L":
                try:
                    if graph.nodes[(x, y-1)]['value'].south:
                        neighbors.append((x,y-1))
                except KeyError:
                    pass
                try:
                    if graph.nodes[(x+1, y)]['value'].west:
                        neighbors.append((x+1,y))
                except KeyError:
                    pass
            case "J":
                try:
                    if graph.nodes[(x, y-1)]['value'].south:
                        neighbors.append((x,y-1))
                except KeyError:
                    pass
                try:
                    if graph.nodes[(x-1, y)]['value'].east:
                        neighbors.append((x-1,y))
                except KeyError:
                    pass
            case "7":
                try:
                    if graph.nodes[(x, y+1)]['value'].north:
                        neighbors.append((x,y+1))
                except KeyError:
                    pass
                try:
                    if graph.nodes[(x-1, y)]['value'].east:
                        neighbors.append((x-1,y))
                except KeyError:
                    pass
            case "F":
                try:
                    if graph.nodes[(x, y+1)]['value'].north:
                        neighbors.append((x,y+1))
                except KeyError:
                    pass
                try:
                    if graph.nodes[(x+1, y)]['value'].west:
                        neighbors.append((x+1,y))
                except KeyError:
                    pass
            case "S" :
                try:
                    if graph.nodes[(x, y-1)]['value'].south:
                        neighbors.append((x,y-1))
                except KeyError:
                    pass
                try:
                    if graph.nodes[(x, y+1)]['value'].north:
                        neighbors.append((x,y+1))
                except KeyError:
                    pass
                try:
                    if graph.nodes[(x-1, y)]['value'].east:
                        neighbors.append((x-1,y))
                except KeyError:
                    pass
                try:
                    if graph.nodes[(x+1, y)]['value'].west:
                        neighbors.append((x+1,y))
                except KeyError:
                    pass
            case _:
                pass
    except:
        pass

    return neighbors


def link_exists(graph, x, y, n_x, n_y):
    graph_node: GraphNode = graph.nodes[(x, y)]['value']
    neighbor_node: GraphNode = graph.nodes[(n_x, n_y)]['value']

    return (graph_node.east and neighbor_node.west) or (graph_node.west and neighbor_node.east) or (graph_node.north and neighbor_node.south) or (graph_node.south and neighbor_node.north)

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

def part_one(graph_data) -> float:
    """
        Part One Implementation

        Input:
            file(str): Input file path

        Output:
            result: Ouput value, usually str or integer
    """

    S = []
    for c in nx.connected_components(graph_data):
        if (100,52) in c:
            S.append(graph_data.subgraph(c).copy())
            #visualize_graph(graph_data.subgraph(c).copy())
            return len(c)/2
    return 0.

def part_two(data, graph_data) -> float:
    """
        Part Two Implementation

        Input:
            file(str): Input file path

        Output:
            result(str): Ouput value, usually str or integer
    """
    d = []
    for c in nx.connected_components(graph_data):
        if (100,52) in c:
            d = c
            break

    matrix = []

    complementary = {"J":"F", "7": "L"}
    deletary = {"7": "F", "J": "L"}

    for y in range(len(data)):
        line = []
        prev = 0
        previous_tiles = deque()
        for x in range(len(data[0])):
            if (x,y) in d:
                tile = data[y][x]
                if tile == "-" or tile == "S":
                    pass
                elif tile == "|":
                    prev = 1-prev
                else:
                    if len(previous_tiles) == 0:
                        previous_tiles.append(tile)
                    else:
                        if previous_tiles[0] == complementary[tile]:
                            prev = 1-prev
                            previous_tiles.pop()
                        elif previous_tiles[0] == deletary[tile]:
                            previous_tiles.pop()
                        else:
                            raise ValueError
                line.append(0)
            else:
                line.append(prev)

        matrix.append(line)

    return sum(sum(line) for line in matrix)

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