from aocd.models import Puzzle
import networkx as nx
import matplotlib.pyplot as plt


def parse_data(data):
    sections = data.split("\n\n")
    variables = [line.split(": ") for line in sections[0].splitlines()]
    gates = sections[1].splitlines()
    return variables, gates


def build_graph(variables, gates):
    G = nx.DiGraph()

    # Add variables as nodes
    for name, value in variables:
        G.add_node(name, type="variable", operation=None, value=int(value))

    # Add gates and connections
    for gate in gates:
        logic, target = gate.split(" -> ")
        if "AND" in logic:
            a, b = logic.split(" AND ")
            G.add_node(target, type="gate", operation="AND")
            G.add_edge(a, target)
            G.add_edge(b, target)
        elif "XOR" in logic:
            a, b = logic.split(" XOR ")
            G.add_node(target, type="gate", operation="XOR")
            G.add_edge(a, target)
            G.add_edge(b, target)
        elif "OR" in logic:
            a, b = logic.split(" OR ")
            G.add_node(target, type="gate", operation="OR")
            G.add_edge(a, target)
            G.add_edge(b, target)

    return G


def evaluate_graph(G):
    for node in nx.topological_sort(G):
        if G.nodes[node]["type"] == "gate":
            a, b = list(G.predecessors(node))
            operation = G.nodes[node]["operation"]
            if operation == "AND":
                G.nodes[node]["value"] = G.nodes[a]["value"] & G.nodes[b]["value"]
            elif operation == "XOR":
                G.nodes[node]["value"] = G.nodes[a]["value"] ^ G.nodes[b]["value"]
            elif operation == "OR":
                G.nodes[node]["value"] = G.nodes[a]["value"] | G.nodes[b]["value"]


def get_output(G):
    # Get all variables starting with z
    keys = [key for key in G.nodes if key.startswith("z")]
    keys.sort(reverse=True)
    result = "".join([str(G.nodes[key]["value"]) for key in keys])
    # Convert binary to decimal
    return int(result, 2)


def set_input(G, x, y):
    # x and y are 45 bit wide
    x = format(x, "045b")
    y = format(y, "045b")
    for i in range(45):
        G.nodes[f"x{i:02}"]["value"] = int(x[i])
        G.nodes[f"y{i:02}"]["value"] = int(y[i])
    return


def check_Valid(G):
    for x in range(128):
        for y in range(128):
            set_input(G, x, y)
            evaluate_graph(G)
            if get_output(G) != x + y:
                print(f"Error at {x} + {y}")
                print(f"Output: {get_output(G)} but should be {x+y}")
                return False
    return True


def part_a(data):
    variables, gates = parse_data(data)

    G = build_graph(variables, gates)
    evaluate_graph(G)
    get_output(G)
    return get_output(G)


def part_b(data):
    variables, gates = parse_data(data)
    G = build_graph(variables, gates)

    valid = False
    while not valid:
        valid = check_Valid(G)

        swaplist = []
        for node in G.nodes:
            foundError = False
            if node.startswith("z"):
                if G.nodes[node]["operation"] != "XOR":
                    print(
                        f"Wrong connection {node}: {G.nodes[node]['operation'] } Should be XOR"
                    )
                    swaplist.append(node)
                    continue

                nodes = list(G.predecessors(node))
                XOR_Gate = None
                OR_Gate = None
                for node in nodes:
                    print(XOR_Gate, OR_Gate)

                    if not XOR_Gate and G.nodes[node]["operation"] == "XOR":
                        XOR_Gate = node
                    elif not OR_Gate and G.nodes[node]["operation"] == "OR":
                        OR_Gate = node
                    else:
                        print(f"Wrong connection {node}: {G.nodes[node]['operation'] }")
                        swaplist.append(node)
                        foundError = True

                if foundError:
                    continue

                if XOR_Gate:
                    for node in G.predecessors(XOR_Gate):
                        if node.startswith("x"):
                            continue
                        elif node.startswith("y"):
                            continue
                        else:
                            print(
                                f"Wrong connection {node}: {G.nodes[node]['operation'] } Shoulde be x of y"
                            )
                            swaplist.append(node)
                            foundError = True

                if foundError:
                    continue

                if OR_Gate:
                    for node in G.predecessors(OR_Gate):
                        if G.nodes[node]["operation"] == "AND":
                            continue
                        else:
                            print(
                                f"Wrong connection {node}: {G.nodes[node]['operation'] } Should be AND"
                            )
                            swaplist.append(node)

        print(swaplist)
        print(len(swaplist))
        quit()


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=24)

    # puzzle.answer_a = part_a(puzzle.input_data)
    print(part_b(puzzle.input_data))
