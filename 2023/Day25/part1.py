import networkx as nx
import matplotlib.pyplot as plt
import re

with open("2023/Day25/input.txt", "r") as puzzleInput:
    lines = puzzleInput.read().split("\n")


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

print(len(partition[0]) * len(partition[1]))

# # Draw the graph
# nx.draw(graph, with_labels=True)

# # Show the graph
# plt.plot()
# plt.savefig("graph.png")
