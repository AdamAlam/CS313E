#  File: Bridge.py 

#  Description:  

#  Student Name: Adam Alam

#  Student UT EID: aba2288

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: Oct 2 2019

#  Date Last Modified:

f = open("bridge.txt", "r")
f_lines = f.readlines()
f.close()
pop_list = []
for i in range(len(f_lines)):
    f_lines[i] = f_lines[i].replace("\n", "")
    try:
        f_lines[i] = int(f_lines[i])
    except:
        pop_list.append(i)

# print(f_lines)

num_cases = f_lines[0]
cases = [[0]] * num_cases
f_lines.pop(0)
pop_list = pop_list[:num_cases]
# print(cases)
for i in range(1,len(pop_list)):
    cases[i-1] = f_lines[pop_list[i-1]:pop_list[i]]
cases[-1] = f_lines[pop_list[-1]:len(f_lines)]


for i in range(len(cases)-1):
    cases[i].pop(-1)


for num in cases[-1]:
    try:
        cases[-1].remove("")
    except:
        pass

def simp(case, time=0):
    test_case = case.copy()
    test_case.sort()
    if (len(test_case)) == 1:
        return test_case[0]
    elif (len(test_case)) == 2:
        return test_case[-1]
    elif (len(test_case)) == 3:
        return sum(test_case)
    elif (len(test_case)) >= 4:
        while len(test_case) != 0:
            if len(test_case) == 2:
                time += test_case[-1]
                return time
            else:
                time += test_case[-1]
                time += test_case[0]
                test_case.pop(-1)

def comp(case, time = 0):
    test_case = case.copy()
    test_case.sort()
    first = test_case[0]
    second = test_case[1]
    time += second
    time += first
    time += test_case[-1]
    test_case.pop(-2)
    test_case.pop(-1)
    time += second
    if len(test_case) < 4:
        return time + simp(test_case)
    else:
        return comp(test_case, time)


for i in cases:
    people = i[0] 
    i.pop(0)
    if people <= 3:
        print(simp(i))
    elif people > 3:
        time2 = comp(i)
        time1 = simp(i)
        if time2 <= time1:
            print(time2)
        else:
            print(time1)
    print("")
