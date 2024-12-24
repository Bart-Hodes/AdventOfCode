from aocd.models import Puzzle
import networkx as nx
import matplotlib.pyplot as plt


def part_a(data):
    inputs = data.split("\n\n")
    inputVariables = inputs[0].split("\n")
    inputLogicGates = inputs[1].split("\n")

    # Create a directed graph
    G = nx.DiGraph()

    # Add variables to the graph as nodes with no outgoing edges
    for line in inputVariables:
        name, value = line.split(":")
        G.add_node(name, type="variable", value=int(value))

    # Add logic gates to the graph as nodes and their dependencies as edges
    for line in inputLogicGates:
        parts = line.split(" -> ")
        gate = parts[0]
        target = parts[1]

        if "AND" in gate:
            a, b = gate.split(" AND ")
            G.add_node(target, type="gate", operation="AND")
            G.add_edge(a, target)
            G.add_edge(b, target)
        elif "XOR" in gate:
            a, b = gate.split(" XOR ")
            G.add_node(target, type="gate", operation="XOR")
            G.add_edge(a, target)
            G.add_edge(b, target)
        elif "OR" in gate:
            a, b = gate.split(" OR ")
            G.add_node(target, type="gate", operation="OR")
            G.add_edge(a, target)
            G.add_edge(b, target)

    # nx.draw(G, with_labels=True)
    # plt.show()

    # Evaluate the graph using topological sort
    for node in nx.topological_sort(G):
        print(node)
        if G.nodes[node]["type"] == "gate":
            a, b = list(G.predecessors(node))
            operation = G.nodes[node]["operation"]
            if operation == "AND":
                G.nodes[node]["value"] = G.nodes[a]["value"] & G.nodes[b]["value"]
            elif operation == "XOR":
                G.nodes[node]["value"] = G.nodes[a]["value"] ^ G.nodes[b]["value"]
            elif operation == "OR":
                G.nodes[node]["value"] = G.nodes[a]["value"] | G.nodes[b]["value"]

    # Get all variables starting with z
    keys = [key for key in G.nodes if key.startswith("z")]
    keys.sort(reverse=True)
    result = "".join([str(G.nodes[key]["value"]) for key in keys])
    # Convert binary to decimal
    result = int(result, 2)
    return result


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=24)

    data = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""
    print(part_a(data))
    puzzle.answer_a = part_a(puzzle.input_data)
