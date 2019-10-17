#  File: Work.py 

#  Description:

#  Student Name: Adam Alam

#  Student UT EID: aba2288

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: Sep 28 2019

#  Date Last Modified: 
import math

f = open("work.txt", "r")
f_lines = f.readlines()
f.close()
for i in range(len(f_lines)):
    f_lines[i] = f_lines[i].replace("\n", "")
    f_lines[i] = f_lines[i].split()

for i in range(len(f_lines)):
    for j in range(len(f_lines[i])):
        try:
            f_lines[i][j] = int(f_lines[i][j])
        except:
            pass

num_cases = f_lines[0][0]


# Honestly, I didn't realize we had to use binary search to solve this problem

def max_sleep(case):
    n = case[0]
    k = case[1]
    # bin_array = []
    # bin_array.extend(range(n//2, n))
    # v_list = []
    p = math.ceil(math.log(n, k))
    # for v in bin_array:
    #     total = 0
    #     for i in range(p):
    #         total = total + (v//(k**i))
    #         if total >= n:
    #             return v
    numerator = n * (k**p)
    denominator = 0
    for i in range(1, p+1):
        denominator += k**i
    v = numerator // denominator
    return v + 2

def main():
    for i in range(1, 1+num_cases):
        print(max_sleep(f_lines[i]))

if __name__ == "__main__":
    main()
