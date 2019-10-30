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
    return

# takes as input a string and a hash table and enters
# the string in the hash table, it resolves collisions
# by double hashing
def insert_word(s, hash_table):
    return
# takes as input a string and a hash table and returns True
# if the string is in the hash table and False otherwise
def find_word(s, hash_table):
    return
# recursively finds if a word is reducible, if the word is
# reducible it enters it into the hash memo and returns True
# and False otherwise
def is_reducible(s, hash_table, hash_memo):
    return
# goes through a list of words and returns a list of words
# that have the maximum length
def get_longest_words(string_list):
    return
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

	

	# hash each word in word_list into hash_list
	for i in word_list:
		insert_word(i, hash_list)
		

	# for collisions use double hashing 

	# create an empty hash_memo

	# populate the hash_memo with M blank strings

	# create and empty list reducible_words

	# for each word in the word_list recursively determine
	# if it is reducible, if it is, add it to reducible_words

	# find words of the maximum length in reducible_words

	# print the words of maximum length in alphabetical order
	# one word per line

main()