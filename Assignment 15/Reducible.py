#  File: Reducible.py

#  Description:

#  Student Name: Adam Alam

#  Student UT EID: aba2288

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: October 25 2019

#  Date Last Modified:

# takes as input a positive integer n
# returns True if n is prime and False otherwise
def is_prime (n):
    if (n == 1):
        return False

    limit = int (n ** 0.5) + 1
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
    hash_idx = 0
    for j in range (len(s)):
        letter = ord (s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx


# takes as input a string in lower case and the constant
# for double hashing and returns the step size for that 
# string
def step_size(s, const):
    return const - (hash_word(s, const) % const)

def removed(s, hash_table):
    pos = []
    for i in range(len(s)):
        r = s[:i] + s[i+1:]
        if find_word(r, hash_table):
            pos.append(r)
    return pos
            
        

# takes as input a string and a hash table and enters
# the string in the hash table, it resolves collisions
# by double hashing
def insert_word(s, hash_table):
    size = len(hash_table)
    idx = hash_word(s, size)
    while True:
        if hash_table[idx] == "":
            hash_table[idx] = s
            return
        else:
            step = step_size(s, 11)
            idx += step

# takes as input a string and a hash table and returns True
# if the string is in the hash table and False otherwise
def find_word(s, hash_table):
    return s == hash_table[hash_word(s, len(hash_table))]


# recursively finds if a word is reducible, if the word is reducible it enters it into the hash memo and returns True and False otherwise goes through a list of words and returns a list of words that have the maximum length
def is_reducible(s, hash_table, hash_memo):
    # check = list(s)
    # if "i" not in check and "o" not in check and "a" not in check:
    #     return False
    # if find_word(s, hash_memo):
    #     return True
    # if s == "a" or s == "i" or s == "o":
    #     insert_word(s, hash_memo)
    #     return True
    # else:
    #     t_list = removed(s, hash_table)
    #     for i in t_list:
    #         if find_word(i, hash_table):
    #             return is_reducible(i, hash_table, hash_memo)
    string_id = hash_word(s, len(hash_table))
    if s == "":
        return False
    elif s == "a" or s == "o" or s == "i":

        hash_memo[string_id] = s
        return True
    elif s in hash_table:
        return True



        
    
# goes through a list of words and returns a list of words that have the maximum length
def get_longest_words(string_list):
    if len(string_list) == 0:
        return []
    max_len = 0
    long = []
    for i in string_list:
        if len(i) > max_len:
            max_len = len(i)
            long = []
        if len(i) == max_len:
            long.append(i)
    return long


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
    for i in range((n*2)+1, n**4, 2):
        if is_prime(i):
            p2 = i
            break

    # create and empty hash_list
    # populate the hash_list with N blank strings
    hash_list = [""] * p2
    print(len(hash_list))

    

    # hash each word in word_list into hash_list
    for i in word_list:
        insert_word(i, hash_list)

        

    # for collisions use double hashing 

    # create an empty hash_memo
    for i in range(27000, 27000**2):
        if is_prime(i):
            m = i
            break
    hash_memo = [""] * m

    # populate the hash_memo with M blank strings

    # create and empty list reducible_words
    reducible_words = []

    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words
    # for i in word_list:
    #     if is_reducible(i, hash_list, hash_memo):
    #         reducible_words.append(i)
    # reducible_words.sort()
    # find words of the maximum length in reducible_words
    # print(removed("pit", hash_list))

    print(is_reducible("sprite", hash_list, hash_memo))
    # reducible_words = reducible_words.sort()
    # print(reducible_words)
    # print the words of maximum length in alphabetical order
    # check1 = get_longest_words(reducible_words)
    # for i in check1:
    #     print(i)
    # one word per line

main()
