#  File: MagicSquare.py

#  Description: Magic Square generator and verifier (Assignment 1)

#  Student's Name: Adam Alam

#  Student's UT EID: aba2288

#  Course Name: CS 313E 

#  Unique Number: 50205

#  Date Created: Aug 31 2019

#  Date Last Modified: Sep 4 2019

import numpy as np

def make_square(n):
    mid_index = n//2
    square_list = []
    for x in range(n):
        square_list.append([0] * n)
    square_list[n-1][mid_index] = 1
    row = n
    column = (n // 2) + 1
    next_num = 2
    while next_num <= n*n:
        if row+1 > n and column+1 <= n:
            row = 1
            column += 1
            square_list[row-1][column-1] = next_num
            next_num += 1
        elif row+1 <= n and column+1 > n:
            column = 1
            row += 1
            square_list[row-1][column-1] = next_num
            next_num += 1
        elif row+1 <=n and column+1 <=n:
            if square_list[row][column] != 0:
                row -= 1
                square_list[row-1][column-1] = next_num
                next_num +=1
            else:
                row+=1
                column+=1
                square_list[row-1][column-1] = next_num
                next_num +=1
        elif row+1 > n and column+1 > n:
            row -= 1
            square_list[row-1][column-1] = next_num
            next_num +=1

    return square_list


def check_square(test_sq):
    try:
        column = 1
        n = len(test_sq)
        theo_sum = n * (((n*n)+1)/2)
        sum_test = 0
        for z in range(n):
            sum_test = sum_test + test_sq[z][column-1]
        if sum_test != theo_sum:
            return False
        column = 2
        while column <= n:
            sum_new = 0
            for z in range(n):
                sum_new = sum_new +test_sq[z][column-1]
            if sum_new != sum_test:
                return False
            else:
                column += 1
        row = 1
        while row <= n:
            sum_new = 0
            for z in range(n):
                sum_new = sum_new + test_sq[row-1][z]
            if sum_new != sum_test:
                return False
            else:
                row += 1
        new_sum = 0
        for z in range(n):
            new_sum = new_sum + test_sq[z][z]
        if new_sum != sum_test:
            return False
        row = n
        column = n
        new_sum = 0
        while row > 0 and column > 0:
            new_sum = new_sum + test_sq[row-1][column-1]
            row -= 1
            column -= 1
        if new_sum != sum_test:
            return False
        print("")
        return True
    except:
        return False

def print_square(magic_array):
    n = len(magic_array)
    np_array = np.array(magic_array)
    print(f"Here is a {n} x {n} magic square:\n")
    for z in range(n):
        to_print = str(np_array[z]).replace("[", "").replace("]", "")
        print(to_print)



def main():
    dimension = 2
    while dimension % 2 != 1 or dimension < 1:
        try:
            dimension = int(input("Please enter an odd number: "))
        except:
            dimension = 2
    print('')
    canon_sum = int(dimension * (((dimension*dimension)+1)/2))
    square = make_square(dimension)
    print_square(square)
    if check_square(square):
        print(f"This is a magic square and the canonical sum is {canon_sum}")
    else:
        print("This is not a magic square")

if __name__ == "__main__":
    main()
