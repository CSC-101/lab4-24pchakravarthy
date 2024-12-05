import data

# Write your functions for each part in the space below.

# Part 1
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
def first_element(lista : list) -> list:
    answer = []
    for i in range(len(lista)-1):
        if (len(lista) == 0):
            break
        answer.append(lista[i][0])
    return answer

# Part 2
def x_coordinates(listb : list) -> list:
    answer = []
    for i in range(len(listb)):
        answer.append(listb[i].x)
    return answer

# Part 3
def are_in_positive_quotient(points : list[Point]) -> list[Point]:
    for i in range(len(points)):
        if (points[i].x > 0 and points[i].y > 0):
            return points[i]


# Part 4
import math
def distance(p1 : Point, p2 : Point) -> float:
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)


# Part 5
def manhattan_distance(p3 : Point, p4 : Point) -> float:
    return math.sqrt(abs(p4.x - p3.x) + abs(p4.y - p3.y))


# Part 6
def distance_all(multipoints : list[Point]) -> list:
    updated = []
    p2 = Point(0, 0)
    for i in range(len(multipoints)):
        updated.append(distance(multipoints[i], p2))
    return updated


