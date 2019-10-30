#  File: Boxes.py

#  Description:

#  Student Name: Adam Alam

#  Student UT EID: aba2288 

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: October 17 2019

#  Date Last Modified: October 18 2019


# determines whether box x can be nested in box y
def nestable(x, y):
    return (x[0] < y[0] and x[1] < y[1] and x[2] < y[2])


# determines whether the subset passed as the argument is truly nestable for all of the boxes in the subset. ss is short for subset as to avoid confusion with the function subset()
def all_nest(ss):
    for i in range(len(ss)-1):
        if nestable(ss[i], ss[i+1]) == False:
            return False
    return True


# subset function which only appends to list s_sub if all_nest() returns True. Argument b is initially passed as an empty list
def subset(a, b, lo, s_sub):
    hi = len(a)
    if lo == hi:
        if all_nest(b) == True:
            s_sub.append(b)
            return
    else:
        c = b.copy()
        b.append(a[lo])
        subset(a, b, lo + 1, s_sub)
        subset(a, c, lo + 1, s_sub)


def main():
    # Opens the file for reading, determines number of boxes, and sorts the list twice so each "box" is usable with the functions
    with open("boxes.txt") as f:
        boxes = f.readlines()
    for i in range(len(boxes)):
        boxes[i] = boxes[i].strip()
        boxes[i] = boxes[i].split()
        for j in range(len(boxes[i])):
            try:
                boxes[i][j] = int(boxes[i][j])
            except:
                pass
        boxes[i].sort()
    n_box = boxes[0][0]
    boxes.pop(0)
    boxes.sort()
    if n_box == 0:
        print("Largest Subset of Nesting Boxes")
        exit()
    # list of all of the subsets. Subsets are appended when the recursive subset() function is run
    subs = []
    subset(boxes, [], 0, subs)

    # subs are now created; finds the largest number of boxes in a subset. Starts at min size of 2.
    threshold = 2
    for i in subs:
        if len(i) > threshold:
            threshold = len(i)

    # appends the boxes which meet the threshold to an array for printing and sorts the array
    passed = []
    for i in range(len(subs)):
        if len(subs[i]) == threshold:
            passed.append(subs[i])
    passed.sort()

    print("Largest Subset of Nesting Boxes")
    for i in passed:
        for j in i:
            print(j)
        print()


main()
