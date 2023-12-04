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
        output_two = part_two(graph_data)
        logging.info(f"Part 2 solution is : {output_two}")
    except NotImplementedError:
        logging.error("The part 2 solution is not implemented yet")


def parse_file(input_file) -> List[List[Union[str,int, None]]]:
    """
        Parses the file and transforms it into a matrix of char and integers (or None)
    """

    with open(input_file) as file:
        return [process_line(line.strip()) for line in file]

def process_line(line) -> List[Union[str,int, None]]:
    """
        Parses each line and transforms it into a list of either char, integer or None
    """
    return [int(char) if char.isdigit() else None if char =="." else char for char in line]


def create_graph(matrix):
    G = nx.Graph()
    for y, row in enumerate(matrix):
        for x, cell in enumerate(row):
            if cell is not None:
                G.add_node((x, y), value = cell)
                for n_x, n_y in get_neighbors(matrix, y, x):
                    G.add_edge((x, y), (n_x, n_y))
    G = update_graph(G, matrix)
    return G

def get_neighbors(matrix, y, x):
    neighbors = []
    for n_y in [y-1,y,y+1]:
        for n_x in [x-1,x,x+1]:
            try:
                if matrix[n_y][n_x] is not None:
                    neighbors.append((n_x,n_y))
            except IndexError:
                pass
    neighbors.remove((x,y))
    return neighbors


def update_graph(G, matrix):
    # Updates graph based on the matrix
    # This is not good with iterating over the cc of the graph, but this method is quite efficient (but not pretty)
    for y, row in enumerate(matrix):
        x = 0
        while x < len(row):
            if isinstance(row[x], int):
                # Start of a potential multi-digit number
                num = str(row[x])
                original_x = x

                # Find the full extent of this number, break links along the way
                neighbors = get_neighbors(matrix, y, x)
                current_nodes = [(x,y)]

                x += 1
                while x < len(row) and isinstance(row[x], int):
                    num += str(row[x])
                    neighbors += get_neighbors(matrix, y, x)
                    current_nodes.append((x,y))
                    x += 1

                num = int(num)

                for node in current_nodes:
                    G.remove_node(node)

                # Update graph: remove digit nodes, add new number node
                new_node = (original_x, y)
                G.add_node(new_node, value=num)

                # Restaures edges
                for node in neighbors:
                    if node not in current_nodes:
                        G.add_edge(new_node, node)

            else:
                x += 1

    return G

def is_symbol(node, G):
    return isinstance(G.nodes[node]['value'], str)  # or any other condition that defines a symbol

def get_nodes_connected_to_symbols(G, specific_symbol=None):
    connected_nodes = list()
    
    for node in G.nodes():
        for k in G.nodes[node].keys():
            if specific_symbol is None:
                if not isinstance(G.nodes[node][k], int):
                    for connected_node in nx.dfs_preorder_nodes(G, source=node):  # or bfs
                        if connected_node != node:  # Exclude the symbol node itself
                            connected_nodes.append(connected_node)
            else:
                if G.nodes[node][k] == specific_symbol:
                    correct_nodes = list()
                    for connected_node in nx.dfs_preorder_nodes(G, source=node):
                        if connected_node != node:  # Exclude the symbol node itself
                            correct_nodes.append(connected_node)
                        if len(correct_nodes) == 2:
                            connected_nodes.append(correct_nodes)
    return connected_nodes


def part_one(graph_data) -> int:
    """
        Part One Implementation

        Input:
            file(str): Input file path

        Output:
            result: Ouput value, usually str or integer
    """
    connected_nodes = get_nodes_connected_to_symbols(graph_data)

    # Could have been done with list comprehension : 
    #return sum(graph_data.nodes[node]['value'] for node in connected_nodes if isinstance(graph_data.nodes[node]['value'], int))
    # But for some reasons, it doesn't know the key "value"
    output = 0

    for node in connected_nodes:
        for key in graph_data.nodes[node]: #type:ignore
            if isinstance(graph_data.nodes[node][key], int): # type:ignore
                output += graph_data.nodes[node][key] # type:ignore

    return output

def part_two(graph_data) -> int:
    """
        Part Two Implementation

        Input:
            file(str): Input file path

        Output:
            result(str): Ouput value, usually str or integer
    """
    connected_nodes = get_nodes_connected_to_symbols(graph_data, specific_symbol="*")

    # Could have been done with list comprehension : 
    #return sum(graph_data.nodes[node]['value'] for node in connected_nodes if isinstance(graph_data.nodes[node]['value'], int))
    # But for some reasons, it doesn't know the key "value"
    output = 0

    for node_pair in connected_nodes:
        out = 1
        for node in node_pair:
            for key in graph_data.nodes[node]: #type:ignore
                if isinstance(graph_data.nodes[node][key], int): # type:ignore
                    out *= graph_data.nodes[node][key] # type:ignore
                else:
                    out = 0 # should not arrive but we might have a key pair with int and symbol
        output += out

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
                        default="Input/day_03/input",
                        nargs='?')
    options = parser.parse_args()

    return options


if __name__ == '__main__':
    main()