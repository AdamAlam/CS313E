#  File: WordSearch.py

#  Description:

#  Student Name: Adam Alam

#  Student UT EID: aba2288

#  Partner Name: Edoardo Palazzi

#  Partner UT EID: emp2587

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 12 Sep 2019

#  Date Last Modified: 16 Sep 2019


def main():
    words = open("hidden.txt.", "r")
    words_new = words.readlines()
    for x in range(len(words_new)):
        words_new[x] = words_new[x].replace("\n", "")
    dimensions = words_new[0].split()
    m = int(dimensions[0])
    n = int(dimensions[1])
    words.close()

    grid = []
    for x in range(2, 2 + m):
        grid.append(words_new[x].split())

    rows = []
    rows_rev = []
    for x in grid:
        rows.append(''.join(x))
    for x in range(len(grid)):
        grid[x].reverse()
        rows_rev.append(''.join(grid[x]))
    org_grid = grid
    columns = []
    new_column = []
    columns_rev = []
    for x in range(m):
        for y in range(n):
            new_column.append(grid[y][x])
        columns.append(''.join(new_column))
        new_column.reverse()
        columns_rev.append(''.join(new_column))
        new_column = []
    columns.reverse()
    columns_rev.reverse()

    org_grid = []
    for x in range(2, 2 + m):
        org_grid.append(words_new[x].split())

    diag_TR = []

    s_col = 1
    s_row = 1

    while s_row < m:
        new_diag = []
        to_mov = 0
        while s_row - to_mov > 0 and s_col + to_mov <= m:
            new_diag.append(org_grid[s_row-1-to_mov][s_col-1+to_mov])
            to_mov += 1
        diag_TR.append(new_diag)
        s_row += 1
    while s_col <= m:
        new_diag = []
        to_mov = 0
        while s_row - to_mov > 0 and s_col + to_mov <= m:
            new_diag.append(org_grid[s_row-1-to_mov][s_col-1+to_mov])
            to_mov += 1
        diag_TR.append(new_diag)
        s_col += 1

    diag_TL = []
    s_row = m
    s_col = 1
    while s_col != m:
        new_diag = []
        to_mov = 0
        while s_col-to_mov > 0 and s_row - to_mov > 0:
            new_diag.append(org_grid[s_row-1-to_mov][s_col-1-to_mov])
            to_mov += 1
        diag_TL.append(new_diag)
        s_col += 1
    while s_row > 0:
        new_diag = []
        to_mov = 0
        while s_col-to_mov > 0 and s_row - to_mov > 0:
            new_diag.append(org_grid[s_row-1-to_mov][s_col-1-to_mov])
            to_mov += 1
        diag_TL.append(new_diag)
        s_row -= 1

    diag_DR = []
    for x in diag_TL:
        diag_DR.append(x[::-1])
    diag_DL = []
    for x in diag_TR:
        diag_DL.append(x[::-1])

    diag_TL_str = []
    diag_DR_str = []
    diag_TR_str = []
    diag_DL_str = []
    for x in diag_TL:
        diag_TL_str.append(''.join(x))
    for x in diag_DL:
        diag_DL_str.append(''.join(x))
    for x in diag_TR:
        diag_TR_str.append(''.join(x))
    for x in diag_DR:
        diag_DR_str.append(''.join(x))

    word_list = []
    for x in range(m+4, m+4+int(words_new[m+3])):
        word_list.append(words_new[x].replace("\n", ""))

    # finds words if they are not diagonal
    def find_straight(word):
        found = False
        check = word.upper()
        for x in range(m):
            if check in columns_rev[x]:
                f_col = m-x
                f_row = columns_rev[x].index(check)+1
                found = True
            elif check in columns[x]:
                f_col = x+1
                f_row = columns[x].index(check)+1
                found = True
            elif check in rows_rev[x]:
                f_row = x+1
                f_col = m - rows_rev[x].index(check)
                found = True
            elif check in rows[x]:
                found = True
                f_row = x+1
                f_col = rows[x].index(check)+1
        if found:
            if f_row < 10:
                return str(f_row) + "   " + str(f_col)
            elif f_row < 100 and f_row >= 10:
                return str(f_row) + "  " + str(f_col)
            elif f_row > 99:
                return str(f_row) + " " + str(f_col)

    # finds words in diagonals
    def find_diag(word):
        found = False
        check = word.upper()
        for x in range(2*m-1):
            if check in diag_DR_str[x]:
                found = True
                second_index = diag_DR_str[x].index(check)
                if x < m:
                    f_row = m-x+second_index
                    f_col = second_index+1
                elif x >= m:
                    f_row = second_index+1
                    f_col = x-m+2+second_index
            elif check in diag_DL_str[x]:
                found = True
                second_index = diag_DL_str[x].index(check)
                if x < m:
                    f_col = x-second_index+1
                    f_row = second_index + 1
                elif x >= m:
                    f_col = m - second_index
                    f_row = x-m + second_index + 2
            elif check in diag_TR_str[x]:
                found = True
                second_index = diag_TR_str[x].index(check)
                if x < m:
                    f_col = second_index + 1
                    f_row = x - (second_index - 1)
                elif x >= m:
                    f_col = x - m + second_index + 2
                    f_row = m - second_index
            elif check in diag_TL_str[x]:
                found = True
                second_index = diag_TL_str[x].index(check)
                if x < m:
                    f_row = m - second_index
                    f_col = x - second_index + 1
                elif x >= m:
                    f_row = m - (x-m) - second_index - 1
                    f_col = m - second_index
            if found:
                if f_row < 10:
                    return str(f_row) + "   " + str(f_col)
                elif f_row < 100 and f_row >= 10:
                    return str(f_row) + "  " + str(f_col)
                elif f_row > 99:
                    return str(f_row) + " " + str(f_col)

    f_file = open("found.txt", "w+")
    max_width = 0
    for x in word_list:
        if len(x) > max_width:
            max_width = len(x)
    for x in word_list:
        y = find_straight(x)
        z = find_diag(x)
        if y:
            f_file.write(x.ljust(max_width+1) + " " + y+"\n")
        elif z:
            f_file.write(x.ljust(max_width+1) + " " + z+"\n")
        elif y is None and z is None:
            f_file.write(x.ljust(max_width+1) + " 0   0"+"\n")

    f_file.close()


main()
