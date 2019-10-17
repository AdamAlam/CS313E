#  File: Geom.py

#  Description: This program computes different geometric calculations based on values of points, circles and rectangles in a file.

#  Student's Name: Adam Alam

#  Student's UT EID: aba2288

#  Partner Name: Edoardo Palazzi

#  Patner EID: emp2587

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 9/16/19

#  Date Last Modified: 9/19/19

import math


class Point(object):
    # constructor
    # x and y are floats
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get distance
    # other is a Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # get a string representation of a Point object
    # takes no arguments
    # returns a string
    def __str__(self):
        return '(' + str(self.x) + ", " + str(self.y) + ")"

    # test for equality
    # other is a Point object
    # returns a Boolean
    def __eq__(self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))


class Circle(object):
    # constructor
    # x, y, and radius are floats
    def __init__(self, radius=1, x=0, y=0):
        self.radius = radius
        self.center = Point(x, y)

    # compute circumference
    def circumference(self):
        return 2.0 * math.pi * self.radius

    # compute area
    def area(self):
        return math.pi * self.radius * self.radius

    # determine if point is strictly inside circle
    def point_inside(self, p):
        return (self.center.dist(p) < self.radius)

    # determine if a circle is strictly inside this circle
    def circle_inside(self, c):
        distance = self.center.dist(c.center)
        return (distance + c.radius) < self.radius

    # determine if a circle c overlaps this circle (non-zero area of overlap)
    # but neither is completely inside the other
    # the only argument c is a Circle object
    # returns a boolean
    def circle_overlap(self, c):
        distance = self.center.dist(c.center)
        if (distance + c.radius) < self.radius:
            return False
        if self.center == c.center and self.radius != c.radius:
            return False
        if self.center == c.center and self.radius == c.radius:
            return True
        if (distance - c.radius) < self.radius:
            return True

    # determine the smallest circle that circumscribes a rectangle
    # the circle goes through all the vertices of the rectangle
    # the only argument, r, is a rectangle object
    def circle_circumscribe(self, r):
        radius = (r.ul.dist(r.lr)) / 2
        x = (r.ul.x + r.lr.x) / 2
        y = (r.ul.y + r.lr.y) / 2
        return Circle(radius, x, y)

    # string representation of a circle
    # takes no arguments and returns a string
    def __str__(self):
        return "Radius: " + str(self.radius) + ", Center: " + str(self.center)

    # test for equality of radius
    # the only argument, other, is a circle
    # returns a boolean
    def __eq__(self, other):
        tol = 1.0e-8
        return abs(self.radius - other.radius) < tol


class Rectangle(object):
    # constructor
    def __init__(self, ul_x=0, ul_y=1, lr_x=1, lr_y=0):
        if ((ul_x < lr_x) and (ul_y > lr_y)):
            self.ul = Point(ul_x, ul_y)
            self.lr = Point(lr_x, lr_y)
        else:
            self.ul = Point(0, 1)
            self.lr = Point(1, 0)

    # determine length of Rectangle (distance along the x axis)
    # takes no arguments, returns a float
    def length(self):
        return abs(self.ul.x - self.lr.x)

    # determine width of Rectangle (distance along the y axis)
    # takes no arguments, returns a float
    def width(self):
        return abs(self.ul.y - self.lr.y)

    # determine the perimeter
    # takes no arguments, returns a float
    def perimeter(self):
        return 2*abs(self.ul.x - self.lr.x) + 2*abs(self.ul.y - self.lr.y)

    # determine the area
    # takes no arguments, returns a float
    def area(self):
        return abs(self.ul.x - self.lr.x)*abs(self.ul.y - self.lr.y)

    # determine if a point is strictly inside the Rectangle
    # takes a point object p as an argument, returns a boolean
    def point_inside(self, p):
        return self.ul.x < p.x < self.lr.x and self.lr.y < p.y < self.ul.y

    # determine if another Rectangle is strictly inside this Rectangle
    # takes a rectangle object r as an argument, returns a boolean
    # should return False if self and r are equal
    def rectangle_inside(self, r):
        return self.point_inside(r.ul) and self.point_inside(r.lr)

    # determine if two Rectangles overlap (non-zero area of overlap)
    # takes a rectangle object r as an argument returns a boolean
    def rectangle_overlap(self, r):
        if self.ul.x >= r.lr.x:
            return False
        if self.ul.y <= r.lr.y:
            return False
        if self.rectangle_inside(r):
            return False
        if r.rectangle_inside(self):
            return False
        return True

    # determine the smallest rectangle that circumscribes a circle
    # sides of the rectangle are tangents to circle c
    # takes a circle object c as input and returns a rectangle object
    def rectangle_circumscribe(self, c):
        ul_x = c.center.x - c.radius
        ul_y = c.center.y + c.radius
        lr_x = c.center.x + c.radius
        lr_y = c.center.y - c.radius
        return Rectangle(ul_x, ul_y, lr_x, lr_y)

    # give string representation of a rectangle
    # takes no arguments, returns a string
    def __str__(self):
        return "UL: " + str(self.ul) + ", LR: " + str(self.lr)

    # determine if two rectangles have the same length and width
    # takes a rectangle other as argument and returns a boolean
    def __eq__(self, other):
        return self.length() == other.length() and self.width() == other.width

def main():


# open the file geom.txt
    fileToOpen = open("geom.txt", "r")
    values = []
    counter = 0
    for line in fileToOpen:
        line = line.strip()
        line = line.split()
        if counter < 2:
            line = line[:2]
        if 2 <= counter < 4:
            line = line[:3]
        if 4 <= counter < 6:
            line = line[:4]
        values.append(line)
        counter += 1

# create Point objects P and Q
    P = Point(eval(values[0][0]), eval(values[0][1]))
    Q = Point(eval(values[1][0]), eval(values[1][1]))
# print the coordinates of the points P and Q
    print("Coordinates of P:", P)
    print("Coordinates of Q:", Q)
# find the distance between the points P and Q
    print("Distance between P and Q:", P.dist(Q))
# create two Circle objects C and D
    C = Circle(eval(values[2][0]), eval(values[2][1]), eval(values[2][2]))
    D = Circle(eval(values[3][0]), eval(values[3][1]), eval(values[3][2]))
# print C and D
    print("Circle C:", C)
    print("Circle D:", D)
# compute the circumference of C
    print("Circumference of C:", C.circumference())
# compute the area of D
    print("Area of D:", D.area())
# determine if P is strictly inside C
    if C.point_inside(P):
        print("P is inside C")
    else:
        print("P is not inside C")
# determine if C is strictly inside D
    if D.circle_inside(C):
        print("C is inside D")
    else:
        print("C is not inside D")
# determine if C and D intersect (non zero area of intersection)
    if C.circle_overlap(D):
        print("C does intersect D")
    else:
        print("C does not intersect D")
# determine if C and D are equal (have the same radius)
    if C.__eq__(D):
        print("C is equal to D")
    else:
        print("C is not equal to D")
# create two rectangle objects G and H
    G = Rectangle(eval(values[4][0]), eval(values[4][1]), eval(values[4][2]), eval(values[4][3]))
    H = Rectangle(eval(values[5][0]), eval(values[5][1]), eval(values[5][2]), eval(values[5][3]))
# print the two rectangles G and H
    print("Rectangle G:", G)
    print("Rectangle H:", H)
# determine the length of G (distance along x axis)
    print("Length of G:", G.length())
# determine the width of H (distance along y axis)
    print("Width of H:", H.width())
# determine the perimeter of G
    print("Perimeter of G:", G.perimeter())
# determine the area of H
    print("Area of H:", H.area())
# determine if point P is strictly inside rectangle G
    if G.point_inside(P):
        print("P is inside G")
    else:
        print("P is not inside G")
# determine if rectangle G is strictly inside rectangle H
    if H.rectangle_inside(G):
        print("G is inside H")
    else:
        print("G is not inside H")
# determine if rectangles G and H overlap (non-zero area of overlap)
    if H.rectangle_overlap(G):
        print("G does overlap H")
    else:
        print("G does not overlap H")
# find the smallest circle that circumscribes rectangle G
# goes through the four vertices of the rectangle
    print("Circle that circumscribes G: ", end="")
    print(Circle.circle_circumscribe(None, G).__str__())
# find the smallest rectangle that circumscribes circle D
# all four sides of the rectangle are tangents to the circle
    print("Rectangle that circumscribes D: ", end="")
    print(Rectangle.rectangle_circumscribe(None, D).__str__())
# determine if the two rectangles have the same length and width
    if H.__eq__(G):
        print("Rectangle G is equal to H")
    else:
        print("Rectangle H is not equal to G")
# close the file geom.txt
    fileToOpen.close()
# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
