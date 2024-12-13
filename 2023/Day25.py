from aocd import data
from aocd.models import Puzzle

import re
import networkx as nx


def part_a(data):
    lines = data.split("\n")

    # Create an empty graph
    graph = nx.Graph()

    for line in lines:
        for idx, node in enumerate(re.finditer(r"[a-z]+", line)):
            if idx == 0:
                graph.add_node(node.group())
                lastNode = node.group()
            else:
                graph.add_node(node.group())
                graph.add_edge(node.group(), lastNode)
    partition = nx.community.edge_betweenness_partition(graph, 2)

    return len(partition[0]) * len(partition[1])


if __name__ == "__main__":
    puzzle = Puzzle(2023, 25)
    # for example in puzzle.examples:
    #     if example.answer_a:
    #         if int(example.answer_a) != part_a(example.input_data):
    #             print("Example part A failed!")
    #             print(f"Expected: {example.answer_a}")
    #             print(f"Got: {part_a(example.input_data)}")
    # if example.answer_b:
    #     if int(example.answer_b) != part_b(example.input_data):
    #         print("Example part B failed!")
    #         print(example)
    #         print(f"Expected: {example.answer_b}")
    #         print(f"Got: {part_b(example.input_data)}")
    puzzle.answer_a = part_a(data)
