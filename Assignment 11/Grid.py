#  File: Grid.py

#  Description:

#  Student Name: Adam Alam

#  Student UT EID: aba2288

#  Partner Name: Edoardo Palazzi

#  Partner UT EID: emp2587

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 10/07/19

#  Date Last Modified: 10/10/19

# counts all the possible paths in a grid recursively
def count_paths(n, row, col):
    if row == n-1 or col == n-1:
        return 1
    return count_paths(n, row+1, col) + count_paths(n, row, col+1)

# recursively gets the greatest sum of all the paths in the grid
def path_sum(grid, n, row, col): 
    if row == n-1 and col == n-1:
        return grid[n-1][n-1]
    if row == n-1 and col < n-1:
        return grid[row][col] + grid[row][col+1]
    if col == n-1 and row < n-1:
        return grid[row][col] + grid[row+1][col]
    else:
        return grid[row][col] + max(
            path_sum(grid, n, row+1, col),
            path_sum(grid, n, row, col+1)
        )


def main():
    # open file for reading
    in_file = open("./grid.txt", "r")

    # read the dimension of the grid
    dim = in_file.readline()
    dim = dim.strip()
    dim = int(dim)

    # create an empty grid
    grid = []

    # populate the grid
    for i in range(dim):
        line = in_file.readline()
        line = line.strip()
        row = line.split()
        for j in range(dim):
            row[j] = int(row[j])
        grid.append(row)
    # close the file
    in_file.close()

    # get the number of paths in the grid and print
    num_paths = count_paths(dim, 0, 0)
    print('Number of paths in a grid of dimension', dim, 'is', num_paths)
    print()

    sum_grid = [["l"]*dim]*dim
    # get the maximum path sum and print
    max_path_sum = path_sum(grid, dim, 0, 0)
    print('Greatest path sum is', max_path_sum)

main()
