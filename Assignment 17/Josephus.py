#  File: Josephus.py

#  Description: Using the circular linked list data structure, we solve the Josephus problem

#  Student Name: Adam Alam

#  Student UT EID: aba2288

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: November 3 2019

#  Date Last Modified: November 4 2019


class Link(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = None

    # Insert an element in the list
    def insert(self, item):

        new_item = Link(item)
        current = self.first

        if (current == None):
            self.first = new_item
            new_item.next = new_item
            return

        while (current.next != self.first):
            current = current.next

        current.next = new_item
        new_item.next = self.first

    # Find the link with the given data (value)
    def find(self, data):
        current = self.first

        while current.data != data:
            current = current.next

        return current

    # Delete a link with a given data (value)
    def delete(self, data):
        current = self.first
        previous = self.first

        if current == None:
            return None

        while previous.next != self.first:
            previous = previous.next

        while current.data != data:
            previous = current
            current = current.next

        if self.first != self.first.next:
            self.first = current.next
        else:
            self.first = None

        previous.next = current.next

    # Delete the nth link starting from the Link start
    # Return the next link from the deleted Link
    def deleteAfter(self, start, n):

        current = self.find(start)

        for i in range(1, n):
            current = current.next

        print(str(current.data))

        self.delete(current.data)

        return current.next

    # Return a string representation of a Circular List
    def __str__(self):
        s_rep = ""
        current = self.first
        while current.next != self.first:
            s_rep = s_rep + str(current.data) + " "
            current = current.next
        return s_rep


def main():

    with open("josephus.txt") as f:
        lines = f.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        lines[i] = int(lines[i])

    num_soldiers = lines[0]
    start = int(lines[1])
    n = int(lines[2])

    circ_list = CircularList()

    for i in range(1, num_soldiers + 1):
        circ_list.insert(i)

    for i in range(1, num_soldiers):
        start = circ_list.deleteAfter(start, n)
        start = start.data

    for i in range(num_soldiers + 1, num_soldiers + 2):
        start = circ_list.deleteAfter(start, n)
        start = start.data


main()
