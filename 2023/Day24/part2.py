import re


with open("2023/Day24/input.txt", "r") as puzzleInput:
    lines = puzzleInput.read().split("\n")

vectors = []
for line in lines:
    vectors.append(re.findall(r"-?\d+", line))
vectors = [list(map(int, vector)) for vector in vectors]

# Given that there are three hailstones we can fix the position and velocity of the hailstone being thrown since it has three degrees of freedom
# Assume hailstone 0 is at (0,0) and create a new reference frame for hailstones 1 and 2
px0, py0, pz0, vx0, vy0, vz0 = vectors[0]

px1, py1, pz1, vx1, vy1, vz1 = [
    vectors[1][i] - vectors[0][i] for i in range(6)]
px2, py2, pz2, vx2, vy2, vz2 = [
    vectors[2][i] - vectors[0][i] for i in range(6)]

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
p1_cross_p2 = [
    py1 * pz2 - pz1 * py2,
    pz1 * px2 - px1 * pz2,
    px1 * py2 - py1 * px2
]

# Cross product: v1 x p2
v1_cross_p2 = [
    vy1 * pz2 - vz1 * py2,
    vz1 * px2 - vx1 * pz2,
    vx1 * py2 - vy1 * px2
]

# Dot product: (p1 x p2) · v2
numerator = (
    p1_cross_p2[0] * vx2 +
    p1_cross_p2[1] * vy2 +
    p1_cross_p2[2] * vz2
)

# Dot product: (v1 x p2) · v2
denominator = (
    v1_cross_p2[0] * vx2 +
    v1_cross_p2[1] * vy2 +
    v1_cross_p2[2] * vz2
)

# Calculate t1
t1 = -numerator / denominator

# t2 = -((p1 x p2) * v1) / ((p1 x v2) * v1)

# Cross product: p1 x p2
p1_cross_p2 = [
    py1 * pz2 - pz1 * py2,
    pz1 * px2 - px1 * pz2,
    px1 * py2 - py1 * px2
]

# Cross product: p1 x v2
p1_cross_v2 = [
    py1 * vz2 - pz1 * vy2,
    pz1 * vx2 - px1 * vz2,
    px1 * vy2 - py1 * vx2
]

# Dot product: (p1 x p2) · v1
numerator = (
    p1_cross_p2[0] * vx1 +
    p1_cross_p2[1] * vy1 +
    p1_cross_p2[2] * vz1
)

# Dot product: (p1 x v2) · v1
denominator = (
    p1_cross_v2[0] * vx1 +
    p1_cross_v2[1] * vy1 +
    p1_cross_v2[2] * vz1
)

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
v = [
    (cx2 - cx1) / (t2 - t1),
    (cy2 - cy1) / (t2 - t1),
    (cz2 - cz1) / (t2 - t1)
]

# Calculate p = point1 - v * t1
p = [
    cx1 - v[0] * t1,
    cy1 - v[1] * t1,
    cz1 - v[2] * t1
]

# Output the results
print("v =", v)
print("p =", p)

print("Answer:", int(abs(p[0]) + abs(p[1]) + abs(p[2])))
