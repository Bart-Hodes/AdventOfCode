from aocd.models import Puzzle

import networkx as nx
import matplotlib.pyplot as plt


def DFS(G, N, start, pos, cycle, cycles):

    if N == 0:
        if G.has_edge(pos, start):
            sorted_cycle = tuple(sorted(cycle))
            cycles.add(sorted_cycle)
        return

    # Search every possible path of length (n-1)
    for node in G.adj[pos]:
        if node not in cycle:
            cycle.add(node)
            DFS(G, N - 1, start, node, cycle, cycles)
            cycle.remove(node)

    return cycles


def findLanParties(G):
    lanParties = set()

    for start_node in G.nodes():
        lanParties.update(DFS(G, 2, start_node, start_node, set([start_node]), set()))

    return lanParties


def part_a(data):
    lines = data.split("\n")

    G = nx.Graph()

    for line in lines:
        nodes = line.split("-")

        # Check if the nodes are already in the graph
        if not G.has_node(nodes[0]):
            G.add_node(nodes[0])
        if not G.has_node(nodes[1]):
            G.add_node(nodes[1])
        G.add_edge(nodes[0], nodes[1])

    lanParties = findLanParties(G)

    count = 0
    for party in lanParties:
        if any(node.startswith("t") for node in party):
            count += 1
    return count


def part_b(data):
    lines = data.split("\n")

    G = nx.Graph()

    for line in lines:
        nodes = line.split("-")

        # Check if the nodes are already in the graph
        if not G.has_node(nodes[0]):
            G.add_node(nodes[0])
        if not G.has_node(nodes[1]):
            G.add_node(nodes[1])
        G.add_edge(nodes[0], nodes[1])

    cliques = list(nx.find_cliques(G))

    largest_clique = max(cliques, key=len)

    largest_clique.sort()
    return ",".join(largest_clique)


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=23)
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
