#  File: Reducible.py

#  Description:

#  Student Name: Adam Alam

#  Student UT EID: aba2288

#  Partner Name: Mijolae Wright

#  Partner UT EID: mew3425

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: October 25 2019

#  Date Last Modified: October 30 2019


# takes as input a positive integer n
# returns True if n is prime and False otherwise
def is_prime(n):
    if (n == 1):
        return False
    limit = int(n ** 0.5) + 1
    div = 2
    while (div < limit):
        if (n % div == 0):
            return False
        div += 1
    return True


# takes as input a string in lower case and the size
# of the hash table and returns the index the string
# will hash into
def hash_word(s, size):
    hashIndex = 0
    for j in range(len(s)):
        letter = ord(s[j]) - 96
        hashIndex = (hashIndex * 26 + letter) % size
    return hashIndex


# takes as input a string in lower case and the constant
# for double hashing and returns the step size for that
# string
def step_size(s, const):
    n = len(s)
    idx = 0
    for j in range(n):
        letter = ord(s[j]) - 96
        idx = const - (idx * 26 + letter) % const
    return idx


# takes as input a string and a hash table and enters
# the string in the hash table, it resolves collisions
# by double hashing
def insert_word(s, hash_table):
    n = len(hash_table)
    init_insert_idx = hash_word(s, n)
    if hash_table[init_insert_idx] == "":
        hash_table[init_insert_idx] = s
    else:
        coll_step = step_size(s, 11)
        s_count = 0
        coll_idx = init_insert_idx + s_count * coll_step
        while hash_table[coll_idx] != "":
            s_count += 1
            coll_idx = (init_insert_idx + s_count * coll_step) % n
        hash_table[coll_idx] = s


# takes as input a string and a hash table and returns True
# if the string is in the hash table and False otherwise
def find_word(s, hash_table):
    idx = hash_word(s, len(hash_table))
    if hash_table[idx] != s:
        idx_2 = step_size(s, 11)
        s_count = 0
        coll_idx = idx + s_count * idx_2
        if hash_table[coll_idx] == s:
            return True
        while hash_table[coll_idx] != s:
            s_count += 1
            coll_idx = (idx + s_count * idx_2) % len(hash_table)
            if hash_table[coll_idx] == "":
                return False
        if hash_table[coll_idx] == s:
            return True
        return False
    return True


# recursively finds if a word is reducible, if the word is
# reducible it enters it into the hash memo and returns True
# and False otherwise
def is_reducible(s, hash_table, hash_memo):
    test = list(s)
    if ("a" not in test and "i" not in test) and "o" not in test:
        return False
    if len(s) == 1 and (s == "a" or s == "i" or s == "o"):
        return True
    elif find_word(s, hash_memo):
        return True
    elif find_word(s, hash_table):
        for i in range(len(s)):
            temp = s[:i] + s[i + 1:]
            if is_reducible(temp, hash_table, hash_memo):
                insert_word(s, hash_memo)
                return True
    return False


# goes through a list of words and returns a list of words
# that have the maximum length
def get_longest_words(string_list):
    longest = []
    max_len = len(max(string_list, key=len))
    for i in string_list:
        if len(i) == max_len:
            longest.append(i)
    return longest


def main():
    # create an empty word_list
    word_list = []

    # open the file words.txt
    with open("words.txt") as f:
        # read words from words.txt and append to word_list
        data = f.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip()
        word_list.append(data[i])

    # find length of word_list
    n = len(word_list)

    # determine prime number N that is greater than twice
    # the length of the word_list
    for i in range((n * 2) + 1, n**4, 2):
        if is_prime(i):
            p2 = i
            break

    # create and empty hash_list
    # populate the hash_list with N blank strings
    hash_list = [""] * p2

    # hash each word in word_list into hash_list
    # for collisions use double hashing
    for i in word_list:
        insert_word(i, hash_list)

    # create an empty hash_memo
    # populate the hash_memo with M blank strings
    for i in range(27001, 27000**2, 2):
        if is_prime(i):
            hash_memo = [""] * i
            break

    # create and empty list reducible_words
    reducible_words = []

    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words
    for word in word_list:
        if is_reducible(word, hash_list, hash_memo):
            reducible_words.append(word)

    reducible_words.sort()
    # find words of the maximum length in reducible_words
    to_print = get_longest_words(reducible_words)

    # print the words of maximum length in alphabetical order
    for i in to_print:
        print(i)
    # one word per line


if __name__ == "__main__":
    main()
