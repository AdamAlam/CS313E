#  File: BabyNames.py

#  Description:

#  Student Name:  Adam Alam

#  Student UT EID:  aba2288

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: Sep 10 2019

#  Date Last Modified:

menu_choices = [
    "Enter 1 to search for names.",
    "Enter 2 to display data for one name.",
    "Enter 3 to display all names that appear in only one decade.",
    "Enter 4 to display all names that appear in all decades.",
    "Enter 5 to display all names that are more popular in every decade.",
    "Enter 6 to display all names that are less popular in every decade.",
    "Enter 7 to quit."
]
names_dict = {}
year_list = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000]
names = open("names.txt", "r")
names_list = names.readlines()
for x in range(len(names_list)):
    names_list[x].replace("\n", "")
    names_list[x] = names_list[x].split()
    for y in range(len(names_list[x])):
        try:
            names_list[x][y] = int(names_list[x][y])
        except:
            pass
for x in range(len(names_list)):
    names_dict[names_list[x][0]] = names_list[x][1:]


# checks if name exists in dictionary
def name_exists(name):
    for x in names_dict.keys():
        if x == name:
            return True
    return False


# Prints the data of a partcilar name and their most popular decade
def name_data():
    name = str(input("Enter a name: ")).capitalize()
    if name_exists(name):
        print("")
        print("The matches with their highest ranking decade are:")
        min_ranking = 1000
        for x in names_dict[name]:
            if x < min_ranking and x > 0:
                min_ranking = x
        min_index = names_dict[name].index(min_ranking)
        print(name, year_list[min_index])
        print("")
    else:
        print("")
        print(f"{name} does not appear in any decade.")
        print("")


# Prints all of the rankings for a particular name
def name_ranking():
    name = str(input("Enter a name: ")).capitalize()
    print("")
    if name_exists(name):
        # return name, names_dict[name]
        print(name + ":", end=" ")
        for x in names_dict[name]:
            print(x, end=" ")
        print("")
        year = 1900
        for x in names_dict[name]:
            print(str(year) + ": " + str(x))
            year += 10
        print("")
    else:
        print(f"{name} does not appear in any decade.")
        print("")


# Prints all of the names if they are ranked in a decade
def one_decade():
    dec = "rand"
    while dec not in year_list:
        try:
            dec = int(input("Enter decade: "))
        except:
            pass
    name_index = year_list.index(dec)
    this_list = []
    for x in names_dict.keys():
        name_rank = names_dict[x][name_index]
        if name_rank != 0:
            to_conv = [name_rank, x]
            this_list.append(tuple(to_conv))
    this_list.sort()
    print("The names are in order of rank")
    for x in range(len(this_list)):
        print(this_list[x][1] + ": " + str(this_list[x][0]))
    print("")


# Prints the names that appear in every decade
def all_rank():
    all_decades = []
    for x in names_dict.keys():
        if 0 not in names_dict[x]:
            all_decades.append(x)
    print(f"{len(all_decades)} names appear in every decade. The names are:")
    for x in all_decades:
        print(x)
    print("")


# Prints the names that have only been getting more popular
def more_pop():
    this_list = []
    for x in names_dict.keys():
        check = True
        min_val = names_dict[x][0]
        for y in range(1, len(names_dict[x])):
            if names_dict[x][y] < min_val and names_dict[x][y] > 0:
                min_val = names_dict[x][y]
            else:
                check = False
                break
        if check:
            this_list.append(x)
    print(f"{len(this_list)} names are more popular every decade.")
    for x in this_list:
        print(x)
    print("")


# Prints the names that have only been getting less popular
def less_pop():
    this_list = []
    for x in names_dict.keys():
        name = x
        check = True
        max_val = names_dict[name][0]
        for y in range(1, len(names_dict[name])):
            if names_dict[name].count(0) > 1:
                check = False
                break
            if names_dict[name].count(0) == 1 and names_dict[name][-1] != 0:
                check = False
                break
            elif names_dict[name].count(0) == 1 and names_dict[name][-1] == 0:
                names_dict[name][-1] = 1001
            if names_dict[name][y] > max_val and names_dict[name][y] != 0:
                max_val = names_dict[name][y]
            else:
                check = False
                break
        if check:
            this_list.append(x)
    print(f"{len(this_list)} names are less popular every decade.")
    for i in this_list:
        print(i)
    print("")


def main():
    choice = "rand"
    while choice != 7: 
        print("Options:")
        for x in menu_choices:
            print(x)
        print("")
        while choice not in range(1, 8):
            try:
                choice = int(input("Enter choice: "))
            except:
                pass
        if choice == 1:
            name_data()
        elif choice == 2:
            name_ranking()
        elif choice == 3:
            one_decade()
        elif choice == 4:
            all_rank()
        elif choice == 5:
            more_pop()
        elif choice == 6:
            less_pop()
        if choice == 7:
            break
        choice = "rand"
    print("Goodbye")

main()

names.close()
