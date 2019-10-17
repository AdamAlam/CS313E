#  File: EvenMagicSquare.py

#  Description: Prints the first 10 permuatations of magic square where n = 4

#  Student Name: Adam Alam

#  Student UT EID: ab2288

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: OCtober 15 2019

#  Date Last Modified: October 16 2019
j = 0


# checks to see if a sqaure is a magic sqaure. Copied from assignment 1.
def check_square(test_sq):
    try:
        column = 1
        n = len(test_sq)
        theo_sum = n * (((n * n) + 1) / 2)
        sum_test = 0
        for z in range(n):
            sum_test = sum_test + test_sq[z][column - 1]
        if sum_test != theo_sum:
            return False
        column = 2
        while column <= n:
            sum_new = 0
            for z in range(n):
                sum_new = sum_new + test_sq[z][column - 1]
            if sum_new != sum_test:
                return False
            else:
                column += 1
        row = 1
        while row <= n:
            sum_new = 0
            for z in range(n):
                sum_new = sum_new + test_sq[row - 1][z]
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
            new_sum = new_sum + test_sq[row - 1][column - 1]
            row -= 1
            column -= 1
        if new_sum != sum_test:
            return False
        return True
    except:
        return False


# converts a 1 dimensional list into a two dimensional list
def make4x4(arr):
    t = []
    t.append(arr[:4])
    t.append(arr[4:8])
    t.append(arr[8:12])
    t.append(arr[12:])
    return t


def permute(arr, lo):
    global j
    hi = len(arr)
    if lo == hi:
        # checks to make sure the sqaure we are printing is in fact magical
        if check_square(make4x4(arr)):
            print(arr)
            j += 1
            # makes sure we only print 10
            if j >= 10:
                exit()
    else:
        for x in range(lo, hi):
            arr_len = len(arr)
            arr[lo], arr[x] = arr[x], arr[lo]
            # each if statement in this block checks if the row sum == 34
            if lo == arr_len - 1 - 12:
                if sum(arr[:4]) == 34:
                    permute(arr[:16], lo + 1)
            elif lo == arr_len - 1 - 8:
                if sum(arr[4:8]) == 34:
                    permute(arr[:16], lo + 1)
            elif lo == arr_len - 1 - 4:
                if sum(arr[8:12]) == 34:
                    permute(arr[:16], lo + 1)
            elif lo == arr_len - 1:
                if sum(arr[12:16]) == 34:
                    twoD = make4x4(arr)
                    # checks the columns as well as the two long diagonals
                    if twoD[0][0] + twoD[1][0] + twoD[2][0] + twoD[3][0] == 34 and twoD[0][1] + twoD[1][1] + twoD[2][1] + twoD[3][1] == 34 and twoD[0][2] + twoD[1][2] + twoD[2][2] + twoD[3][2] == 34 and twoD[0][3] + twoD[1][3] + twoD[2][3] + twoD[3][3] == 34 and twoD[0][0] + twoD[1][1] + twoD[2][2] + twoD[3][3] == 34 and twoD[0][3] + twoD[1][2] + twoD[2][1] + twoD[3][0] == 34:
                        permute(arr, lo + 1)
            else:
                permute(arr, lo + 1)
            arr[lo], arr[x] = arr[x], arr[lo]


def main():
    grid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    permute(grid, 0)


main()
