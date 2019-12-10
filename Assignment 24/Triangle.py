#  File: Triangle.py

#  Description: We use and compare four programming approaches to find the greatest path sum in a triangle.

#  Student's Name: Adam Alam

#  Student's UT EID: aba2288

#  Course Name: CS 313E

#  Unique Number: 50305

#  Date Created: December 4 2019

#  Date Last Modified: December 9 2019

import time


# returns the greatest path sum using exhaustive search
def exhaustive_search(grid):
    empty = []
    exh_help(grid, 0, 0, 0, empty)
    return max(empty)


# helper function for exhaustive search
def exh_help(grid, vertical, horizontal, t_sum, empty):
    if vertical == len(grid):
        empty.append(t_sum)
    else:
        exh_help(grid, vertical + 1, horizontal, t_sum + grid[vertical][horizontal], empty)
        exh_help(grid, vertical + 1, horizontal + 1, t_sum + grid[vertical][horizontal], empty)
    return empty


# returns the greatest path sum using greedy approach
def greedy(grid):
    t_sum = 0
    horizontal = 0
    t_sum += grid[0][0]
    for vertical in range(len(grid) - 1):
        if grid[vertical + 1][horizontal] > grid[vertical + 1][horizontal + 1]:
            t_sum += grid[vertical + 1][horizontal]
        else:
            t_sum += grid[vertical + 1][horizontal + 1]
            horizontal += 1
    return t_sum


# returns the greatest path sum using divide and conquer(recursive) approach
def rec_search(grid):
    return rec_search_helper(grid, 0, 0)


def rec_search_helper(grid, vertical, horizontal):
    if vertical == len(grid) - 1:
        return grid[vertical][horizontal]
    else:
        same_horizontal = rec_search_helper(grid, vertical + 1, horizontal)
        diff_horizontal = rec_search_helper(grid, vertical + 1, horizontal + 1)
        return grid[vertical][horizontal] + max(same_horizontal, diff_horizontal)


# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog(grid):
    new_grid = grid[:]
    for vertical in range(len(new_grid) - 1, 0, -1):
        for horizontal in range(len(new_grid[vertical]) - 1):
            if new_grid[vertical][horizontal] <= new_grid[vertical][horizontal + 1]:
                new_grid[vertical - 1][horizontal] += new_grid[vertical][horizontal + 1]
            else:
                new_grid[vertical - 1][horizontal] += new_grid[vertical][horizontal]
    return new_grid[0][0], new_grid


# reads the file and returns a 2-D list that represents the triangle
def read_file():
    f = open("triangle.txt", "r")
    height = int(f.readline().strip())
    grid = []
    for i in range(height):
        line = f.readline().strip()
        vertical = line.split()
        for j in range(len(vertical)):
            vertical[j] = int(vertical[j])
        grid.append(vertical)
    return grid


def main():
    # read triangular grid from file
    grid = read_file()

    ti_exh = time.time()
    # output greates path from exhaustive search
    exh = exhaustive_search(grid)
    tf_exh = time.time()
    print(f"The greatest path sum through exhaustive search is {exh}.")
    del_t_exh = tf_exh - ti_exh
    # print time taken using exhaustive search
    print(f"The time taken for exhaustive search is {del_t_exh} seconds.\n")

    ti_greedy = time.time()
    # output greates path from greedy approach
    greedy_num = greedy(grid)
    tf_greedy = time.time()
    print(f"The greatest path sum through greedy search is {greedy_num}.")
    del_t_greedy = tf_greedy - ti_greedy
    # print time taken using greedy approach
    print(f"The time taken for greedy approach {del_t_greedy} seconds.\n")

    ti_dac = time.time()
    # output greates path from divide-and-conquer approach
    dac = rec_search(grid)
    print(f"The greatest path sum through recursive search is {dac}.")
    tf_dac = time.time()
    del_t_dac = tf_dac - ti_dac
    # print time taken using divide-and-conquer approach
    print(f"The time taken for recursive search is {del_t_dac} seconds.\n")

    ti_dyn = time.time()
    # output greates path from dynamic programming
    dyn, new_grid = dynamic_prog(grid)
    tf_dyn = time.time()
    print(f"The greatest path sum through dynamic programming is {dyn}.")
    del_t_dyn = tf_dyn - ti_dyn
    # print time taken using dynamic programming
    print(f"The time taken for dynamic programming is {del_t_dyn} seconds.")


if __name__ == "__main__":
    main()
