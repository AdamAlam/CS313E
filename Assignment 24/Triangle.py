#  File: Triangle.py

#  Description:

#  Student's Name:

#  Student's UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:

import time

class Triangle:
    def __init__(self):
        return

# returns the greatest path sum using exhaustive search
def exhaustive_search(grid):
    return


# returns the greatest path sum using greedy approach
def greedy(grid):
    return grid[0][0] + greed_helper(grid, 1, 0)

def greed_helper(grid, r, r_p):
    if r >= len(grid):
        return 0
    else:
        if grid[r][r_p] > grid[r][r_p+1]:
            return grid[r][r_p] + greed_helper(grid, r+1, r_p)
        else:
            return grid[r][r_p] + greed_helper(grid, r+1, r_p+1)


# returns the greatest path sum using divide and conquer(recursive) approach
def rec_search(grid):
    return


# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog(grid):
    return dynamic_helper(grid, 0, 0)

def dynamic_helper(grid, r, r_p):
    if r >= len(grid):
        return 0
    else:
        a = grid[r][r_p] + dynamic_helper(grid, r+1, r_p)
        b = grid[r][r_p] + dynamic_helper(grid, r+1, r_p+1)
        return max(a, b)


# reads the file and returns a 2-D list that represents the triangle
def read_file():
    return


def main():
    # read triangular grid from file
    tri = []
    f = open("triangle.txt", "r")
    levels = int(f.readline().strip())
    for line in range(levels):
        row = f.readline().strip().split()
        for i in range(len(row)):
            row[i] = int(row[i])
        tri.append(row)
    f.close()

    ti = time.time()
    # output greates path from exhaustive search
    tf = time.time()
    del_t = tf - ti
    # print time taken using exhaustive search

    ti_greedy = time.time()
    # output greates path from greedy approach
    print(f"Greedy: {greedy(tri)}")
    tf_greedy = time.time()
    del_t_greedy = tf_greedy - ti_greedy
    # print time taken using greedy approach
    print(f"Greedy Time: {del_t_greedy}s\n")

    ti = time.time()
    # output greates path from divide-and-conquer approach
    tf = time.time()
    del_t = tf - ti
    # print time taken using divide-and-conquer approach

    ti_dyn = time.time()
    # output greates path from dynamic programming
    print(f"Dynamic: {dynamic_prog(tri)}")
    tf_dyn = time.time()
    del_t_dyn = tf_dyn - ti_dyn
    # print time taken using dynamic programming
    print(f"Dynamic Time: {del_t_dyn}s")


if __name__ == "__main__":
    main()
