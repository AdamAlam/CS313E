#  File: Intervals.py

#  Description: Checks a list of intervals to see which are collapsible and collapses them into non-intersecting intervals

#  Student Name: Adam Alam

#  Student UT EID: aba2288

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: Sep 6 2019

#  Date Last Modified: Sep 9 2019


# Determines collapsible tuples and returns list of them
def collapse(a_list):
    collapsed = []
    for next_pair in a_list:
        if not collapsed:
            collapsed.append(next_pair)
        else:
            current_pair = collapsed[-1]
            if next_pair[0] <= current_pair[1]:
                upper_point = max(current_pair[1], next_pair[1])
                collapsed[-1] = (current_pair[0], upper_point)
            else:
                collapsed.append(next_pair)
    return collapsed


# Prints the tuples in the order they are already in
def print_tuples(a_list):
    print("Non-intersecting Intervals:")
    for x in a_list:
        print(x)


# Prints the tuples in asceding order of the size of the interval
def print_by_size(a_list):
    print("Non-intersecting Intervals in order of size:")
    difference = []
    for x in a_list:
        difference.append(x[1]-x[0])
    while difference != []:
        min_val = difference.index(min(difference))
        print(a_list[min_val])
        difference.pop(min_val)
        a_list.pop(min_val)


# Main function, calls appropriate functions
def main():
    intervals = open("intervals.txt", "r")
    intervals_list = intervals.readlines()
    for x in range(len(intervals_list)):
        intervals_list[x] = intervals_list[x].replace("\n", "")
        intervals_list[x] = intervals_list[x].split()
        intervals_list[x][0] = int(intervals_list[x][0])
        intervals_list[x][1] = int(intervals_list[x][1])
        intervals_list[x] = tuple(intervals_list[x])
    intervals_list.sort()
    collapsed_list = collapse(intervals_list)
    print_tuples(collapsed_list)
    print("")
    print_by_size(collapsed_list)
    intervals.close()


main()
