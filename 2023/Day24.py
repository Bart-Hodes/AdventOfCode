from aocd import data
from aocd.models import Puzzle

import re


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        raise Exception("lines do not intersect")

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


def part_a(data):
    lines = data.split("\n")

    testArea = [(200000000000000, 200000000000000), (400000000000000, 400000000000000)]
    # testArea = [(7,7),(27,27)]

    count = 0
    vectors = []
    for line in lines:
        vectors.append(re.findall(r"-?\d+", line))

    for idx, vector1 in enumerate(vectors):
        for vector2 in vectors[idx + 1 :]:
            line1 = [
                (int(vector1[0]), int(vector1[1])),
                (int(vector1[0]) + int(vector1[3]), int(vector1[1]) + int(vector1[4])),
            ]
            line2 = [
                (int(vector2[0]), int(vector2[1])),
                (int(vector2[0]) + int(vector2[3]), int(vector2[1]) + int(vector2[4])),
            ]

            try:
                x, y = line_intersection(line1, line2)
            except:
                # print("Lines do not intersect")
                continue

            # Check if intersection is in the future
            if (
                ((int(vector1[0]) - x) > 0 and int(vector1[3]) > 0)
                or ((int(vector1[0]) - x) < 0 and int(vector1[3]) < 0)
                or ((int(vector1[1]) - y) > 0 and int(vector1[4]) > 0)
                or ((int(vector1[1]) - y) < 0 and int(vector1[4]) < 0)
            ):
                futureHailstoneA = False
            else:
                futureHailstoneA = True

            if (
                ((int(vector2[0]) - x) > 0 and int(vector2[3]) > 0)
                or ((int(vector2[0]) - x) < 0 and int(vector2[3]) < 0)
                or ((int(vector2[1]) - y) > 0 and int(vector2[4]) > 0)
                or ((int(vector2[1]) - y) < 0 and int(vector2[4]) < 0)
            ):
                futureHailstoneB = False
            else:
                futureHailstoneB = True

            # Check if the intersection is within the test area
            if futureHailstoneA and futureHailstoneB:
                if (
                    x >= testArea[0][0]
                    and x <= testArea[1][0]
                    and y >= testArea[0][1]
                    and y <= testArea[1][1]
                ):
                    # print(f"Hailstones' intersection at {x},{y} within the test area")
                    count += 1
                # else:
                #     print(
                #         f"Hailstones' intersection at {x},{y} is outside the test area"
                #     )
            # else:
            # print(f"Hailstones' intersection at {x},{y} is in the past")

    # print(f"Total intersections within the test area: {count}")
    return count


def part_b(data):
    lines = data.split("\n")

    vectors = []
    for line in lines:
        vectors.append(re.findall(r"-?\d+", line))
    vectors = [list(map(int, vector)) for vector in vectors]

    # Given that there are three hailstones we can fix the position and velocity of the hailstone being thrown since it has three degrees of freedom
    # Assume hailstone 0 is at (0,0) and create a new reference frame for hailstones 1 and 2
    px0, py0, pz0, vx0, vy0, vz0 = vectors[0]

    px1, py1, pz1, vx1, vy1, vz1 = [vectors[1][i] - vectors[0][i] for i in range(6)]
    px2, py2, pz2, vx2, vy2, vz2 = [vectors[2][i] - vectors[0][i] for i in range(6)]

    # Let t1 and t2 be the times that the rock colides with hailstones 1 and 2 respectively
    # p1 + t1 * v1
    # p2 + t2 * v2
    # Since the colisions are in a straight line the vectors must be colinear
    # (p1 + t1 * v1) x (p2 + t2 * v2) = 0
    # This can be expanded into
    # (p1 x p2) + t1 * (v1 x p2) + t2 * (p1 x v2) + t1 * t2 * (v1 x v2) = 0
    # Weird interaction between dot and cross product gives (a x b) * a = (a x b) * b = 0
    # Lets mutliply the equation by v1
    # (p1 x p2) * v1 + t2 * (p1 x v2) * v1 = 0
    # t2 = -((p1 x p2) * v1) / ((p1 x v2) * v1)
    # Lets mutliply the equation by v2
    # (p1 x p2) * v2 + t1 * (v1 x p2) * v2 = 0
    # t1 = -((p1 x p2) * v2) / ((v1 x p2) * v2)

    # Cross product: p1 x p2
    p1_cross_p2 = [py1 * pz2 - pz1 * py2, pz1 * px2 - px1 * pz2, px1 * py2 - py1 * px2]

    # Cross product: v1 x p2
    v1_cross_p2 = [vy1 * pz2 - vz1 * py2, vz1 * px2 - vx1 * pz2, vx1 * py2 - vy1 * px2]

    # Dot product: (p1 x p2) · v2
    numerator = p1_cross_p2[0] * vx2 + p1_cross_p2[1] * vy2 + p1_cross_p2[2] * vz2

    # Dot product: (v1 x p2) · v2
    denominator = v1_cross_p2[0] * vx2 + v1_cross_p2[1] * vy2 + v1_cross_p2[2] * vz2

    # Calculate t1
    t1 = -numerator / denominator

    # t2 = -((p1 x p2) * v1) / ((p1 x v2) * v1)

    # Cross product: p1 x p2
    p1_cross_p2 = [py1 * pz2 - pz1 * py2, pz1 * px2 - px1 * pz2, px1 * py2 - py1 * px2]

    # Cross product: p1 x v2
    p1_cross_v2 = [py1 * vz2 - pz1 * vy2, pz1 * vx2 - px1 * vz2, px1 * vy2 - py1 * vx2]

    # Dot product: (p1 x p2) · v1
    numerator = p1_cross_p2[0] * vx1 + p1_cross_p2[1] * vy1 + p1_cross_p2[2] * vz1

    # Dot product: (p1 x v2) · v1
    denominator = p1_cross_v2[0] * vx1 + p1_cross_v2[1] * vy1 + p1_cross_v2[2] * vz1

    # Calculate t2
    t2 = -numerator / denominator

    # Now that we know the colision times we can calculate the initial position and velocity of the rock
    cx1 = vectors[1][0] + t1 * vectors[1][3]
    cy1 = vectors[1][1] + t1 * vectors[1][4]
    cz1 = vectors[1][2] + t1 * vectors[1][5]

    cx2 = vectors[2][0] + t2 * vectors[2][3]
    cy2 = vectors[2][1] + t2 * vectors[2][4]
    cz2 = vectors[2][2] + t2 * vectors[2][5]

    # Calculate v = (point2 - point1) / (t2 - t1)
    v = [(cx2 - cx1) / (t2 - t1), (cy2 - cy1) / (t2 - t1), (cz2 - cz1) / (t2 - t1)]

    # Calculate p = point1 - v * t1
    p = [cx1 - v[0] * t1, cy1 - v[1] * t1, cz1 - v[2] * t1]

    # Output the results
    print("v =", v)
    print("p =", p)

    print("Answer:", int(abs(p[0]) + abs(p[1]) + abs(p[2])))
    return int(abs(p[0]) + abs(p[1]) + abs(p[2]))


if __name__ == "__main__":
    puzzle = Puzzle(2023, 24)
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
    # puzzle.answer_b = part_b(data)
