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

    # reverse the string
    x = x[::-1]
    y = y[::-1]

    for i in range(45):
        G.nodes[f"x{i:02}"]["value"] = int(x[i])
        G.nodes[f"y{i:02}"]["value"] = int(y[i])
    return


def check_Valid(G):
    # Test values in a smart way for a binary adder range with power of 2
    for xp in range(45):
        for yp in range(45):
            x = 2**xp
            y = 2**yp
            set_input(G, x, y)
            evaluate_graph(G)

            if get_output(G) != x + y:
                print(f"Error at {x} + {y}")
                print(f"Output: {get_output(G)} but should be {x+y}")

                # print x and y in binary
                print(f"x: {format(x, '045b')}")
                print(f"y: {format(y, '045b')}")

                print(xp, yp)
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

    # swaplist = [["z31", "ngr"], ["z06", "fkp"], ["mfm", "skt"]]
    # ["z11", "krj"]]
    # , ["z45", "bpt"]]

    # swaplist = [["z31", "ngr"]]
    swaplist = [["z06", "fkp"], ["z11", "ngr"], ["z31", "mfm"], ["krj", "bpt"]]
    for swap in swaplist:
        for idx, gate in enumerate(gates):
            if f"-> {swap[0]}" in gate:
                gates[idx] = gate.replace(swap[0], swap[1])
            if f"-> {swap[1]}" in gate:
                gates[idx] = gate.replace(swap[1], swap[0])

    print(gates)

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

        swaplist = ["z06", "fkp", "z11", "ngr", "z31", "mfm", "krj", "bpt"]
        swaplist.sort()
        return ",".join(swaplist)


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=24)

    data = """x00: 1
x01: 0
x02: 0
x03: 1
x04: 1
x05: 0
x06: 0
x07: 0
x08: 0
x09: 0
x10: 0
x11: 1
x12: 0
x13: 1
x14: 1
x15: 1
x16: 1
x17: 0
x18: 0
x19: 1
x20: 0
x21: 0
x22: 1
x23: 1
x24: 1
x25: 0
x26: 1
x27: 1
x28: 0
x29: 1
x30: 0
x31: 1
x32: 0
x33: 1
x34: 0
x35: 1
x36: 1
x37: 0
x38: 1
x39: 1
x40: 1
x41: 1
x42: 0
x43: 1
x44: 1
y00: 1
y01: 0
y02: 0
y03: 1
y04: 1
y05: 1
y06: 0
y07: 0
y08: 0
y09: 1
y10: 0
y11: 0
y12: 0
y13: 1
y14: 1
y15: 0
y16: 1
y17: 0
y18: 1
y19: 1
y20: 1
y21: 0
y22: 0
y23: 1
y24: 1
y25: 1
y26: 0
y27: 1
y28: 0
y29: 1
y30: 0
y31: 0
y32: 0
y33: 1
y34: 1
y35: 1
y36: 1
y37: 0
y38: 0
y39: 0
y40: 0
y41: 1
y42: 0
y43: 1
y44: 1

x36 AND y36 -> rpc
swn OR jrk -> kfm
x36 XOR y36 -> mvv
y28 XOR x28 -> rnh
bfp OR wqc -> rgb
tkc OR mfm -> brs
kmb XOR gfj -> z16
x25 AND y25 -> mdt
mpp AND hfd -> gjp
dhd AND mvb -> vrf
y14 XOR x14 -> qvt
shc OR bkk -> wvr
x29 AND y29 -> gdn
x11 XOR y11 -> jpp
rws OR fts -> mpp
wmq OR ngr -> knj
x24 XOR y24 -> gfg
tpf AND mgq -> tkc
wvr XOR jgw -> fkp
brs AND nmr -> qpb
x18 AND y18 -> qsw
pnb OR vjh -> sfh
x44 XOR y44 -> gcd
x22 AND y22 -> mhd
x37 XOR y37 -> dgg
vfj XOR dmh -> z15
x30 XOR y30 -> qgd
rpw OR gdn -> wrv
ptj OR vqm -> vjn
gfg AND pqf -> pnb
x17 XOR y17 -> rtv
y19 AND x19 -> wpt
sfp AND sbq -> tcv
hvv OR vmr -> kpq
pgc XOR fvj -> z02
knj AND ctw -> vqm
y42 XOR x42 -> vfb
y13 XOR x13 -> vdk
x43 AND y43 -> nhd
krg XOR dkw -> z43
y32 AND x32 -> vdm
hfd XOR mpp -> z08
nfq OR qgm -> cqq
x02 AND y02 -> nss
rvw XOR dtb -> z10
qvt AND qqv -> rgj
mvv XOR sgr -> z36
y11 AND x11 -> wmq
cnd XOR jqv -> z29
vdk XOR vjn -> z13
x34 AND y34 -> kjj
qvt XOR qqv -> z14
y18 XOR x18 -> mkt
bwk OR krn -> pqf
nhs XOR cqq -> z41
y31 AND x31 -> z31
y23 AND x23 -> bwk
sfh AND pmf -> ctp
rvw AND dtb -> sgv
tns AND chq -> dwv
rqt XOR snv -> z22
jqv AND cnd -> rpw
x33 AND y33 -> vtd
ctw XOR knj -> z12
bpp OR ghf -> z06
ffn AND rdj -> shc
cfw OR tnc -> sgr
wdm AND psv -> fwc
vwn OR wpt -> bvc
jkn OR gvk -> z45
x00 XOR y00 -> z00
qpf XOR mkt -> z18
y12 AND x12 -> ptj
dvq XOR rkm -> z04
x15 XOR y15 -> dmh
qrm OR nss -> wdm
mhv OR mnv -> rcs
qtq OR cqn -> nwk
x20 XOR y20 -> tpw
x04 AND y04 -> ptd
nhd OR pnk -> mdn
hjc OR hth -> pgc
x20 AND y20 -> qtq
gcd XOR mdn -> z44
mgq XOR tpf -> mfm
x30 AND y30 -> bbk
dmh AND vfj -> cpc
x44 AND y44 -> gvk
dwv OR jvf -> jjj
pkh AND fkp -> rws
x39 AND y39 -> wqc
fwc OR nbc -> rkm
bdc AND bbd -> dnc
x26 XOR y26 -> tns
csh AND mst -> vwn
x43 XOR y43 -> dkw
bvc XOR tpw -> z20
nwk XOR ngm -> z21
rtv XOR kfm -> z17
x06 AND y06 -> bpp
x10 XOR y10 -> dtb
y29 XOR x29 -> cnd
y08 XOR x08 -> hfd
y03 XOR x03 -> psv
rgj OR bph -> vfj
psv XOR wdm -> z03
dnc OR vtd -> mvb
gcn AND tqf -> krn
y38 XOR x38 -> krj
x24 AND y24 -> vjh
y41 AND x41 -> vmr
jgw AND wvr -> ghf
x09 XOR y09 -> sfp
y28 AND x28 -> wpw
x40 XOR y40 -> mkc
hsn AND dgg -> snc
jpp XOR stv -> ngr
mjb OR cpc -> gfj
rcs XOR rnh -> z28
sfp XOR sbq -> z09
rtv AND kfm -> jfr
tjh OR wpw -> jqv
x16 XOR y16 -> kmb
bgn OR wnm -> snv
nmr XOR brs -> z32
rpc OR dvm -> hsn
gfg XOR pqf -> z24
dkw AND krg -> pnk
kmb AND gfj -> jrk
skt XOR kjn -> z01
gcn XOR tqf -> z23
jjj XOR rhc -> z27
y07 AND x07 -> fts
y21 AND x21 -> wnm
kvd OR snc -> ntr
nht XOR hsp -> z39
wrv XOR qgd -> z30
y07 XOR x07 -> pkh
tdv OR krj -> hsp
stv AND jpp -> z11
x27 AND y27 -> mhv
bdc XOR bbd -> z33
x12 XOR y12 -> ctw
mvv AND sgr -> dvm
x27 XOR y27 -> rhc
x21 XOR y21 -> ngm
mhn XOR mdg -> z35
x19 XOR y19 -> csh
y35 XOR x35 -> mhn
snv AND rqt -> tfs
rkm AND dvq -> cjp
pgc AND fvj -> qrm
kpq XOR vfb -> z42
qgd AND wrv -> gqt
y26 AND x26 -> jvf
x39 XOR y39 -> nht
vdk AND vjn -> jqm
bvc AND tpw -> cqn
y32 XOR x32 -> nmr
x25 XOR y25 -> pmf
y09 AND x09 -> prs
y14 AND x14 -> bph
qpb OR vdm -> bdc
gqt OR bbk -> tpf
x40 AND y40 -> qgm
sfh XOR pmf -> z25
x22 XOR y22 -> rqt
rhc AND jjj -> mnv
csh XOR mst -> z19
x42 AND y42 -> krw
x34 XOR y34 -> dhd
x35 AND y35 -> tnc
ngm AND nwk -> bgn
tdh OR jqm -> qqv
y00 AND x00 -> skt
y41 XOR x41 -> nhs
ntr XOR bpt -> z38
vrf OR kjj -> mdg
kvf OR krw -> krg
x03 AND y03 -> nbc
dhd XOR mvb -> z34
qpf AND mkt -> rsd
y01 XOR x01 -> kjn
x17 AND y17 -> bvg
jfr OR bvg -> qpf
y13 AND x13 -> tdh
bpb OR gjp -> sbq
x16 AND y16 -> swn
x02 XOR y02 -> fvj
y15 AND x15 -> mjb
x23 XOR y23 -> tqf
rnh AND rcs -> tjh
x05 AND y05 -> bkk
hsn XOR dgg -> z37
qsw OR rsd -> mst
sgv OR qnf -> stv
y01 AND x01 -> hth
y38 AND x38 -> bpt
rgb AND mkc -> nfq
y33 XOR x33 -> bbd
tns XOR chq -> z26
ctp OR mdt -> chq
nhs AND cqq -> hvv
pkh XOR fkp -> z07
rdj XOR ffn -> z05
mhd OR tfs -> gcn
y10 AND x10 -> qnf
hsp AND nht -> bfp
gcd AND mdn -> jkn
ntr AND bpt -> tdv
prs OR tcv -> rvw
x05 XOR y05 -> ffn
y04 XOR x04 -> dvq
x31 XOR y31 -> mgq
y08 AND x08 -> bpb
mhn AND mdg -> cfw
y37 AND x37 -> kvd
rgb XOR mkc -> z40
cjp OR ptd -> rdj
x06 XOR y06 -> jgw
skt AND kjn -> hjc
vfb AND kpq -> kvf"""

    # puzzle.answer_a = part_a(puzzle.input_data)
    print(part_b(data))
