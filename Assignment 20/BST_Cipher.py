#  File: BST_Cipher.py

#  Description: Using a binary tree, we can encrypt and decrypt strings.

#  Student Name: Adam Alam

#  Student UT EID: aba2288

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: November 17 2019

#  Date Last Modified: November 18 2019


class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class Tree:
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__(self, encrypt_str):
        alpha = list("abcdefghijklmnopqrstuvwxyz ")
        self.root = None
        for char in encrypt_str:
            if char in alpha:
                self.insert(char)

    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert(self, ch):
        new = Node(ch)
        if self.root is None:
            self.root = new
            return
        if self.exists(ch) is False:
            cur = self.root
            par = self.root
            while cur is not None:
                par = cur
                if ch >= cur.data:
                    cur = cur.rchild
                else:
                    cur = cur.lchild
            if ch >= par.data:
                par.rchild = new
            else:
                par.lchild = new

    # Function to determine if a character is already in the tree.
    def exists(self, ch):
        cur = self.root
        dup = False
        while cur is not None:
            if cur.data == ch:
                return True
            if ch >= cur.data:
                cur = cur.rchild
            else:
                cur = cur.lchild
        return dup





    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search(self, ch):
        cur = self.root
        if self.exists(ch) is False:
            return ""
        if ch == cur.data:
            return "*"
        filtered = ""
        while cur.data != ch and cur is not None:
            if ch >= cur.data:
                cur = cur.rchild
                filtered += ">"
            else:
                cur = cur.lchild
                filtered += "<"
        return filtered

    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse(self, st):
        cur = self.root
        if st == "*":
            return cur.data
        for char in st:
            if cur is None:
                return ""
            else:
                if char == ">":
                    cur = cur.rchild
                elif char == "<":
                    cur = cur.lchild
        return cur.data

    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt(self, st):
        filtered = ""
        alpha = list("abcdefghijklmnopqrstuvwxyz ")
        for char in st.lower():
            if char in alpha:
                filtered += char
        enc = ""
        for char in filtered:
            enc += str(self.search(char)) + "!"
        return enc[:len(enc) - 1]

    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt(self, st):
        filtered = ""
        direction = ["<", ">", "!", "*"]
        for char in st:
            if char in direction:
                filtered += char
        pathList = filtered.split("!")
        decrypted = ""
        for path in pathList:
            decrypted += self.traverse(path)
        return decrypted


def main():
    key = str(input("Enter encryption key: ")).lower()
    print()
    # key = "the quick brown fox jumps over the lazy dog"
    tree = Tree(key)
    encode = str(input("Enter string to be encrypted: ")).lower()
    print(f"Encrypted string: {tree.encrypt(encode)}\n")
    decode = str(input("Enter string to be decrypted: ")).lower()
    print(f"Decrypted string: {tree.decrypt(decode)}")


if __name__ == "__main__":
    main()
