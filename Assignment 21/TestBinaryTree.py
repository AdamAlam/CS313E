#  File: TestBinaryTree.py

#  Description: In this assignment, we work with binary trees and write methods and classes to utilize them.

#  Student Name: Adam Alam

#  Student UT EID: aba2288

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: November 19 2019

#  Date Last Modified: November 22 2019
from random import shuffle

class Node:
    def __init__(self, data):
        self.data = data
        self.rchild = None
        self.lchild = None


class Tree:
    def __init__(self):
        self.root = None
        
    # Insert function used to add data to the tree
    def insert(self, data):
        new_node = Node(data)
        cur = self.root
        if cur is None:
            self.root = new_node
        else:
            par = self.root
            while cur is not None:
                par = cur
                if data >= cur.data:
                    cur = cur.rchild
                else:
                    cur = cur.lchild
            if data >= par.data:
                par.rchild = new_node
            else:
                par.lchild = new_node
            

    # Returns true if two binary trees are similar
    def is_similar(self, pNode):
        if self.root is None and pNode.root is None:
            return True
        elif self.root is None or pNode.root is None:
            return False
        else:
            return self.similar_helper(self.root, pNode.root)

    # Helper function for is_similar()
    def similar_helper(self, r1, r2):
        if r1 is None and r2 is None:
            return True
        elif r1 is None or r2 is None:
            return False
        else:
            return (r1.data == r2.data) and self.similar_helper(r1.rchild, r2.rchild) and self.similar_helper(r1.lchild, r2.lchild)


    # Prints out all nodes at the given level
    def print_level(self, level):
        if level > self.get_height() + 1:
            return
        items = []
        if self.root is None:
            print()
            return
        elif level == 1:
            items.append(self.root.data)
            print(items[0])
        else:
            self.print_help(self.root, level, items)
            for item in items[::-1]:
                print(item, end=" ")
            print()


    # Helper function for print_level()
    def print_help(self, aNode, level, arr):
        if level == 1 and aNode is not None:
            arr.append(aNode.data)
            return
        elif aNode is not None:
            self.print_help(aNode.rchild, level-1, arr)
            self.print_help(aNode.lchild, level-1, arr)
        return


    # Returns the height of the tree
    def get_height(self):
        if self.root is None:
            return 0
        else:
            return self.get_height_helper(self.root)

    # Helper function for get_height()
    def get_height_helper(self, node):
        if node is None:
            return 0
        else:     
            r_height = self.get_height_helper(node.rchild)
            l_height = self.get_height_helper(node.lchild)
        return max(l_height, r_height) + 1

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes(self):
        if self.root is None:
            return 0
        else:
            return self.num_nodes_helper(self.root)

    # Helper function for num_nodes()
    def num_nodes_helper(self, root):
        if root is None:
            return 0
        else:
            return self.num_nodes_helper(root.rchild) + self.num_nodes_helper(root.lchild) + 1

def main():
        # Create three trees - two are the same and the third is different
        l1 = []
        l2 = []
        for i in range(1,32):
            if i < 16:
                l1.append(i)
            l2.append(i)
        # I shuffle the lists to get a different tree without having to hardcode the data that is inserted.
        shuffle(l1)
        shuffle(l2)
        print(f"Tree 1 Insert order: {l1}")
        print(f"Tree 2 Insert order: {l2}\n")
        t1 = Tree()
        t1_dup = Tree()
        t2 = Tree()
        for i in l1:
            t1.insert(i)
            t1_dup.insert(i)
        for i in l2:
            t2.insert(i)
        

        # Test your method is_similar()
        # Should return 'True' as trees are identical
        print(f"Similar Trees: {t1.is_similar(t1_dup)}")
        
        # Should return 'False' as trees are not similar
        print(f"Not similar Trees: {t1.is_similar(t2)}\n")
        
        # Print the various levels of two of the trees that are different
        for i in range(1,t1.get_height()+1):
            print(f"Tree 1 level {i}: ", end="")
            t1.print_level(i)
        print()
        for i in range(1,t2.get_height()+1):
            print(f"Tree 2 level {i}: ", end="")
            t2.print_level(i)
        print()

        # Get the height of the two trees that are different
        print(f"Height of tree 1: {t1.get_height()-1}")
        print(f"Height of tree 2: {t2.get_height()-1}\n")

        # Get the total number of nodes a binary search tree
        print(f"Nodes in tree 1: {t1.num_nodes()}")
        print(f"Nodes in tree 2: {t2.num_nodes()}")

if __name__ == "__main__":
    main()
    