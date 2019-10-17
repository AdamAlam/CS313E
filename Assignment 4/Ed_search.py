#  File: WordSearch.py

#  Description: This programs returns a file with the coordinates of the first letter of the words to be found in a grid of letters.

#  Student Name: Edoardo Palazzi

#  Student UT EID: emp2587

#  Partner Name: Adam Alam

#  Partner UT EID: aba2288

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 09/11/19

#  Date Last Modified: 09/16/19

def main():
    # opening file in read mode
    words = open("hidden.txt.", "r")

    # creating variables for size of grid
    words_new = words.readlines()
    for x in range(len(words_new)):
        words_new[x] = words_new[x].replace("\n", "")
    dimensions = words_new[0].split()
    m = int(dimensions[0])
    n = int(dimensions[1])
    words.close()

    # creating the grid, nested lists
    grid = []
    for x in range(2, 2 + m):
        grid.append(words_new[x].split())

    # creating lists of strings of the rows (from left to right and from right to left --> reverse)
    rows = []
    rows_rev = []
    for x in grid:
        rows.append(''.join(x))
    for x in range(len(grid)):
        grid[x].reverse()
        rows_rev.append(''.join(grid[x]))
    org_grid = grid
    # creating lists of strings of the columns (from up to down and from down to up --> reverse)
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

    # creating list for diagonals
    diag_TR = []

    s_col = 1
    s_row = 1

    while s_row < m:
        new_diag = []
        to_mov = 0
        while s_row - to_mov > 0 and s_col + to_mov <= m:
            new_diag.append(org_grid[s_row - 1 - to_mov][s_col - 1 + to_mov])
            to_mov += 1
        diag_TR.append(new_diag)
        s_row += 1
    while s_col <= m:
        new_diag = []
        to_mov = 0
        while s_row - to_mov > 0 and s_col + to_mov <= m:
            new_diag.append(org_grid[s_row - 1 - to_mov][s_col - 1 + to_mov])
            to_mov += 1
        diag_TR.append(new_diag)
        s_col += 1

    diag_TL = []
    s_row = m
    s_col = 1
    while s_col != m:
        new_diag = []
        to_mov = 0
        while s_col - to_mov > 0 and s_row - to_mov > 0:
            new_diag.append(org_grid[s_row - 1 - to_mov][s_col - 1 - to_mov])
            to_mov += 1
        diag_TL.append(new_diag)
        s_col += 1
    while s_row > 0:
        new_diag = []
        to_mov = 0
        while s_col - to_mov > 0 and s_row - to_mov > 0:
            new_diag.append(org_grid[s_row - 1 - to_mov][s_col - 1 - to_mov])
            to_mov += 1
        diag_TL.append(new_diag)
        s_row -= 1

    diag_DR = []
    for x in diag_TL:
        diag_DR.append(x[::-1])
    diag_DL = []
    for x in diag_TR:
        diag_DL.append(x[::-1])

    # creating list of strings for the diagonals (diagonals pointing: TopLeft (TL), TopRight (TR), DownLeft (DL), DownRight (DR)
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

    # print(diag_DL_str, "Down Left", end="\n\n")
    # print(diag_TR_str, "Top Right", end="\n\n")
    # print(diag_TL_str, "Top Left", end="\n\n")
    # print(diag_DR_str, "Down Right", end="\n\n")

    word_list = []
    for x in range(m + 4, m + 4 + int(words_new[m + 3])):
        word_list.append(words_new[x].replace("\n", ""))

    # function to find words in rows and columns
    def find_straight(word):
        found = False
        check = word.upper()
        for x in range(m):
            if check in columns_rev[x]:
                f_col = m - x
                f_row = columns_rev[x].index(check) + 1
                found = True
            elif check in columns[x]:
                f_col = x + 1
                f_row = columns[x].index(check) + 1
                found = True
            elif check in rows_rev[x]:
                f_row = x + 1
                f_col = m - rows_rev[x].index(check)
                found = True
            elif check in rows[x]:
                found = True
                f_row = x + 1
                f_col = rows[x].index(check) + 1
        if found:
            coords = [f_row, f_col]
            return coords

    # function to find words in diagonals
    def find_diag(word):
        found = False
        check = word.upper()
        for x in range(2 * m - 1):
            if check in diag_DR_str[x]:
                found = True
                sec_idx = diag_DR_str[x].index(check)
                if x < m:
                    f_row = m - x + sec_idx
                    f_col = sec_idx + 1
                elif x >= m:
                    f_row = sec_idx + 1
                    f_col = x - m + 2 + sec_idx
            elif check in diag_DL_str[x]:
                found = True
                sec_idx = diag_DL_str[x].index(check)
                if x < m:
                    f_col = x - sec_idx + 1
                    f_row = sec_idx + 1
                elif x >= m:
                    f_col = m - sec_idx
                    f_row = x - m + sec_idx + 2
            elif check in diag_TR_str[x]:
                found = True
                sec_idx = diag_TR_str[x].index(check)
                if x < m:
                    f_col = sec_idx + 1
                    f_row = x - (sec_idx - 1)
                elif x >= m:
                    f_col = x - m + sec_idx + 2
                    f_row = m - sec_idx

            elif check in diag_TL_str[x]:
                found = True
                sec_idx = diag_TL_str[x].index(check)
                if x < m:
                    f_row = m - sec_idx
                    f_col = x - sec_idx + 1
                elif x >= m:
                    f_row = m - (x - m) - sec_idx - 1
                    f_col = m - sec_idx
            if found:
                coords = [f_row, f_col]
                return coords

    # creating list for words found in grid and lists for their corresponding first letter position (x and y)
    wordsFound = []
    xCoord = []
    yCoord = []
    for i in word_list:
        y = find_straight(i)
        z = find_diag(i)
        if y:
            wordsFound.append(i)
            xCoord.append(y[0])
            yCoord.append(y[1])
        elif z:
            wordsFound.append(i)
            xCoord.append(z[0])
            yCoord.append(z[1])

    # writing results to the found.txt file
    with open("found.txt", "w") as fileToWrite:
        fileToWrite.writelines(map("{} {} {}\n".format, wordsFound, xCoord, yCoord))



    fileToWrite.close()



main()



