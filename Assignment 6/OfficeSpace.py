#  File: OfficeSpace.py

#  Description: Calculates the area of an employees office and if there are conflicts with other employees' office requests

#  Student Name: Adam Alam

#  Student UT EID: aba2288

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: Sep 22 2019

#  Date Last Modified: Sep 23 2019
import itertools


def area(rect):
    return (rect.ne.x - rect.sw.x) * (rect.ne.y - rect.sw.y)


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle():
    def __init__(self, sw_x, sw_y, ne_x, ne_y):
        self.sw = Point(sw_x, sw_y)
        self.ne = Point(ne_x, ne_y)
        self.area = (self.ne.x - self.sw.x) * (self.ne.y - self.sw.y)
        self.guar = self.area


o = open("office.txt", "r")
office = o.readlines()
o.close()
for i in range(len(office)):
    office[i] = office[i].replace("\n", "")
    office[i] = office[i].split()

for i in range(len(office)):
    for j in range(len(office[i])):
        try:
            office[i][j] = int(office[i][j])
        except:
            pass

to_split = []
for i in range(len(office)):
    if len(office[i]) == 1:
        to_split.append(i - 1)
to_split.append(len(office))
cases = []
for i in range(1, len(to_split)):
    try:
        cases.append(office[to_split[i - 1]: to_split[i]])
    except:
        pass


def case(off_list):
    office_dict = {}
    num_employees = off_list[1][0]
    for i in range(2, 2 + num_employees):
        office_dict[off_list[i][0]] = off_list[i][1:]

    def do_overlap(rect_1, rect_2):
        if rect_1.sw.x >= rect_2.ne.x or rect_2.sw.x >= rect_1.ne.x:
            return False
        if rect_1.sw.y >= rect_2.ne.y or rect_2.sw.y >= rect_1.ne.y:
            return False
        return True

    rect_list = []
    for x in office_dict.keys():
        to_append = office_dict[x]
        rect_list.append(Rectangle(to_append[0], to_append[1], to_append[2], to_append[3]))

    contested_space = 0

    def overlap_area(rect1, rect2):
        if do_overlap(rect1, rect2):
            r1 = rect1
            r2 = rect2
            left = max(r1.sw.x, r2.sw.x)
            right = min(r1.ne.x, r2.ne.x)
            bottom = max(r1.sw.y, r2.sw.y)
            top = min(r1.ne.y, r2.ne.y)
            if left < right and bottom < top:
                intersection = (right - left) * (top - bottom)
                return intersection
        return 0

    for a, b in itertools.combinations(rect_list, 2):
        cont = overlap_area(a, b)
        a.guar = a.guar - cont
        b.guar = b.guar - cont
        contested_space += cont

    total_area = off_list[0][0] * off_list[0][1]
    not_requested = total_area
    for i in range(len(rect_list)):
        not_requested = not_requested - rect_list[i].area
    not_requested = not_requested + contested_space
    print("Total", end=" ")
    print(total_area)
    print("Unallocated", end=" ")
    print(not_requested)
    print('Contested', end=" ")
    print(contested_space)
    names = list(office_dict.keys())
    for i in range(len(rect_list)):
        print(names[i], end=" ")
        print(rect_list[i].guar)
    print("")


def main():
    for i in range(len(cases)):
        case(cases[i])


main()
