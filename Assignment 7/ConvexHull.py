#  File: ConvexHull.py

#  Description: Finds the vertices of a convex hull given a set of points and computes its area

#  Student Name: Adam Alam

#  Student UT EID: aba2288

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: Sep 24 2019

#  Date Last Modified: Sep 27 2019

import math
import numpy as np


class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __eq__(self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

    def __ne__(self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

    def __lt__(self, other):
        tol = 1.0e-8
        if abs(self.x - other.x) < tol:
            if abs(self.y - other.y) < tol:
                return False
            else:
                return (self.y < other.y)
        return (self.x < other.x)

    def __le__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y <= other.y)
        return (self.x <= other.x)

    def __gt__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
            else:
                return (self.y > other.y)
        return (self.x > other.x)

    def __ge__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y >= other.y)
        return (self.x >= other.x)


def det(p, q, r):
    array1 = [
        [1, p.x, p.y],
        [1, q.x, q.y],
        [1, r.x, r.y]
    ]
    a = np.array(array1)
    return int(np.linalg.det(a))


def convex_hull(sorted_points):
    upper_hull = []
    upper_hull.append(sorted_points[0])
    upper_hull.append(sorted_points[1])
    for i in range(2, len(sorted_points)):
        upper_hull.append(sorted_points[i])
        while len(upper_hull) >= 3 and det(upper_hull[-3], upper_hull[-2], upper_hull[-1]) >= 0:
            upper_hull.pop(-2)

    lower_hull = []
    lower_hull.append(sorted_points[-1])
    lower_hull.append(sorted_points[-2])
    for i in range(len(sorted_points) - 3, -1, -1):
        lower_hull.append(sorted_points[i])
        while len(lower_hull) >= 3 and det(lower_hull[-3], lower_hull[-2], lower_hull[-1]) >= 0:
            lower_hull.pop(-2)
    lower_hull.pop(-1)
    lower_hull.pop(0)

    convex_hull = upper_hull + lower_hull
    return convex_hull


def area_poly(convex_poly):
    connected = convex_poly
    connected.append(connected[0])
    numerator = 0
    for i in range(len(connected) - 1):
        p_less = connected[i]
        p_more = connected[i + 1]
        numerator += ((p_less.x * p_more.y) - (p_less.y * p_more.x))
    area = abs(numerator) * .5
    return area


def main():
    # Create an empty list of Point objects
    p = []

    # Open file points.txt for reading
    f = open("points.txt", "r")

    # Read file line by line, create Point objects and store in a list
    points_list = f.readlines()
    f.close()
    for i in range(len(points_list)):
        points_list[i] = points_list[i].replace("\t", " ")
        points_list[i] = points_list[i].replace("\n", "")

    points_list.pop(0)

    for i in range(len(points_list)):
        points_list[i] = points_list[i].split()
        try:
            points_list[i][0] = int(points_list[i][0])
            points_list[i][1] = int(points_list[i][1])
        except:
            pass

    # sort the list according to x-coordinates
    points_list.sort()

    for i in points_list:
        p.append(Point(i[0], i[1]))

    # get the convex hull
    completed_hull = convex_hull(p)

    # print the convex hull
    print("Convex Hull")
    for x in completed_hull:
        print(x)
    print("")

    # get the area of the convex hull
    area_convex_hull = area_poly(completed_hull)

    # print the area of the convex hull
    print(f'Area of Convex Hull = {area_convex_hull}')
    print('')


if __name__ == "__main__":
    main()
