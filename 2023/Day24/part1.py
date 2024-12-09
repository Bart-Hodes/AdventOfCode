import re

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

with open("input.txt", "r") as puzzleInput:
    lines = puzzleInput.read().split("\n")
    
testArea = [(200000000000000,200000000000000),(400000000000000,400000000000000)]
# testArea = [(7,7),(27,27)]
    
count = 0
vectors = []
for line in lines:
    vectors.append(re.findall(r"-?\d+", line))

for idx, vector1 in enumerate(vectors):
    for vector2 in vectors[idx+1:]:
        line1 = [(int(vector1[0]), int(vector1[1])), (int(vector1[0]) + int(vector1[3]), int(vector1[1]) + int(vector1[4]))]
        line2 = [(int(vector2[0]), int(vector2[1])), (int(vector2[0]) + int(vector2[3]), int(vector2[1]) + int(vector2[4]))]

        try:
            x,y = line_intersection(line1, line2)
        except:
            print("Lines do not intersect")
            continue
        
        # Check if intersection is in the future
        if  (((int(vector1[0]) - x) > 0 and int(vector1[3]) > 0) or ((int(vector1[0]) - x) < 0 and int(vector1[3]) < 0) or ((int(vector1[1]) - y) > 0 and int(vector1[4]) > 0) or ((int(vector1[1]) - y) < 0 and int(vector1[4]) < 0)):
            futureHailstoneA = False
        else:
            futureHailstoneA = True
        
        if (((int(vector2[0]) - x) > 0 and int(vector2[3]) > 0) or ((int(vector2[0]) - x) < 0 and int(vector2[3]) < 0) or ((int(vector2[1]) - y) > 0 and int(vector2[4]) > 0) or ((int(vector2[1]) - y) < 0 and int(vector2[4]) < 0)):
            futureHailstoneB = False
        else:
            futureHailstoneB = True
            
        # Check if the intersection is within the test area
        if futureHailstoneA and futureHailstoneB:
            if x >= testArea[0][0] and x <= testArea[1][0] and y >= testArea[0][1] and y <= testArea[1][1]:
                print(f"Hailstones' intersection at {x},{y} within the test area")
                count +=1
            else:
                print(f"Hailstones' intersection at {x},{y} is outside the test area")
        else:
            print(f"Hailstones' intersection at {x},{y} is in the past")
                
print(f"Total intersections within the test area: {count}")

    



