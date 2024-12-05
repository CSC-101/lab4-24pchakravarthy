import data
import lab4
import unittest

from lab4 import are_in_positive_quotient


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        indent = [[1,2], [3,4]]
        result = lab4.first_element(indent)
        expected = [1, 3]
        if expected == result:
            return True
        else:
            return False


    def test_first_element_2(self):
        indent = [[5,6], [7,8]]
        result = lab4.first_element(indent)
        expected = [5, 7]
        if expected == result:
            return True
        else:
            return False




    # Part 2
    def test_x_coordinates_1(self):
        p1 = [data.Point(4, 2), data.Point(5, 8), data.Point(6, 9)]
        if lab4.x_coordinates(p1) == [4, 5, 6]:
            return True
        else:
            return False

    def test_x_coordinates_2(self):
        p1 = [data.Point(8, 1), data.Point(-10, 12), data.Point(0, 2)]
        if lab4.x_coordinates(p1) == [8, -10, 0]:
            return True
        else:
            return False




    # Part 3
    def test_are_in_positive_quadrant1(self):
        points = [data.Point(4, 2), data.Point(-5, 8), data.Point(6, 9), data.Point(-1, 6)]
        if are_in_positive_quotient(points) == [data.Point(4, 2), data.Point(6, 9)]:
            return True
        else:
            return False

    def test_are_in_positive_quadrant2(self):
        points = [data.Point(-1, 2), data.Point(-5, -8), data.Point(6, -9), data.Point(-1, -6)]
        if lab4.are_in_positive_quotient(points) == []:
            return True
        else:
            return False

    # Part 4
    def testdistance_forsame(self):
        p1 = data.Point(0, 0)
        p2 = data.Point(0, 0)
        if (lab4.distance(p1, p2) == 0.0):
            return True
        else:
            return False

    def testdistance_fordifferent(self):
        p1 = data.Point(0, 0)
        p2 = data.Point(2, 0)
        if (lab4.distance(p1, p2) == 2.0):
            return True
        else:
            return False


    # Part 5
    def test_manhattan_distance1(self):
        p1 = data.Point(2, 3)
        p2 = data.Point(5, 7)
        if (lab4.manhattan_distance(p1, p2) == 7.0):
            return True
        else:
            return False

    def test_manhattan_distance2(self):
        p1 = data.Point(6, 8)
        p2 = data.Point(-4, -4)
        if (lab4.manhattan_distance(p1, p2) == 22.0):
            return True
        else:
            return False


    # Part 6
    def test_distance_all1(self):
        points = [data.Point(3, 4)]
        result = lab4.distance_all(points)
        answer = [5.0]
        if answer == result:
            return True
        else:
            return False

    def test_distance_all2(self):
        points = [data.Point(0, 0), data.Point(1, 1), data.Point(5, 12)]
        result = lab4.distance_all(points)
        answer = [0.0, 1.0, 13.0]
        if answer == result:
            return True
        else:
            return False




if __name__ == '__main__':
    unittest.main()
