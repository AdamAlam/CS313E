#  File: TestLinkedList.py

#  Description: Various Test and Methods for a Linked List

#  Student Name: Adam Alam

#  Student UT EID: aba288

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: October 31 2019

#  Date Last Modified: November 1 2019


class Link (object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList(object):

    def __init__(self):
        self.first = None

    # get number of links
    def get_num_links(self):
        selected = self.first
        if selected == None:
            return 0
        c = 1
        while selected.next != None:
            selected = selected.next
            c += 1
        return c

    # add an item at the beginning of the list
    def insert_first(self, data):
        new_item = Link(data)
        new_item.next = self.first
        self.first = new_item

    # add an item at the end of a list
    def insert_last(self, data):
        new_item = Link(data)
        selected = self.first
        if selected == None:
            self.first = new_item
            return
        while selected.next != None:
            selected = selected.next
        selected.next = new_item

    # add an item in an ordered list in ascending order
    def insert_in_order(self, data):
        new_item = Link(data)
        selected = self.first
        previous = self.first
        if selected == None or selected.data >= data:
            new_item.next = self.first
            self.first = new_item
            return
        while selected.next != None:
            if selected.data > data:
                new_item.next = previous.next
                previous.next = new_item
                return
            else:
                previous = selected
                selected = selected.next

        if selected.data > data:
            new_item.next = previous.next
            previous.next = new_item
        else:
            selected.next = new_item
        return

    # search in an unordered list, return None if not found
    def find_unordered(self, data):
        selected = self.first
        if selected == None:
            return None
        while selected.data != data:
            if selected.next != None:
                selected = selected.next
            else:
                return None
        return selected.data

    # Search in an ordered list, return None if not found
    def find_ordered(self, data):
        selected = self.first
        if selected == None:
            return None
        while selected.data != data:
            if selected.next == None:
                return None
            elif selected.data > data:
                return None
            else:
                selected = selected.next
        return selected.data

    # Delete and return Link from an unordered list or None if not found
    def delete_link(self, data):
        selected = self.first
        previous = self.first
        if selected == None:
            return None

        while selected.data != data:
            if selected.next != None:
                previous = selected
                selected = selected.next
            else:
                return None
            if selected != self.first:
                previous.next = selected.next
            else:
                self.first = self.first.next

        return selected

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        string = ""
        selected = self.first
        n = 0
        while selected != None:
            string = string + str(selected.data) + "  "
            selected = selected.next
            n += 1
            if n == 10:
                string = string + "\n"
                n = 0
        return string.strip()

    # Copy the contents of a list and return new list
    def copy_list(self):
        copied = LinkedList()
        selected = self.first
        while selected != None:
            copied.insert_last(selected.data)
            selected = selected.next
        return copied

    # Reverse the contents of a list and return new list
    def reverse_list(self):
        rev = LinkedList()
        selected = self.first
        while selected != None:
            rev.insert_first(selected.data)
            selected = selected.next
        return rev

    # Sort the contents of a list in ascending order and return new list
    def sort_list(self):
        sor = LinkedList()
        selected = self.first
        while selected != None:
            sor.insert_in_order(selected.data)
            if selected.next == None:
                break
            else:
                selected = selected.next
        return sor

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        selected = self.first
        while selected.next != None:
            if selected.data > selected.next.data:
                return False
            else:
                selected = selected.next
        return True

    # Return True if a list is empty or False otherwise
    def is_empty(self):
        return self.first == None

    # Merge two sorted lists and return new list in ascending order
    def merge_list(self, other):
        merged = LinkedList()
        selected = self.first
        while selected != None:
            merged.insert_last(selected.data)
            selected = selected.next

        sel_other = other.first
        while sel_other != None:
            merged.insert_last(sel_other.data)
            sel_other = sel_other.next
        merged = merged.sort_list()

        return merged

    # Test if two lists are equal, item by item and return True
    def is_equal(self, other):
        n = self.get_num_links()
        m = other.get_num_links()
        if n != m:
            return False
        selected = self.first
        sel_other = other.first
        while selected != None:
            if selected.data != sel_other.data:
                return False
            else:
                selected = selected.next
                sel_other = sel_other.next
        return True

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates(self):
        no_dup = LinkedList()
        c = 0
        t_set = set([])
        selected = self.first
        n = self.get_num_links()
        if n == 0:
            return None
        while selected != None:
            t_set.add(selected.data)
            c += 1
            if len(t_set) != c:
                selected = selected.next
                c -= 1
            else:
                no_dup.insert_last(selected.data)
        return no_dup


def main():
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    l_1 = [32, 24, 54, 65, 12, 76, 42, 23, 13, 14, 26, 51]
    l_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    linked1 = LinkedList()
    for i in l_1:
        linked1.insert_first(i)
    print("Insert First: Linked1")
    print(linked1)

    # Test method insert_last()
    print("Insert Last: Linked2")
    linked2 = LinkedList()
    for i in l_2:
        linked2.insert_last(i)
    print(linked2)
    print()

    # Test method insert_in_order()
    print("Insert In Order:")
    linked3 = LinkedList()
    for i in l_1:
        linked3.insert_in_order(i)
    print(linked3)
    print()
    # Test method get_num_links()
    print("Num Links:")
    print(linked3.get_num_links())
    print()

    # Test method find_unordered()
    # Consider two cases - data is there, data is not there
    test3 = linked1.copy_list()
    print("Find Unordered: Data Present")
    print(test3.find_unordered(13) != None)
    print()
    print("Find Unordered: Data Not Present")
    print(test3.find_unordered(1213) != None)
    print()

    # Test method find_ordered()
    # Consider two cases - data is there, data is not there
    l_fo = linked1.copy_list().sort_list()
    print("Find Ordered: Data Present")
    print(l_fo.find_ordered(13) != None)
    print()
    print("Find Ordered: Data Not Present")
    print(l_fo.find_ordered(1051) != None)
    print()

    # Test method delete_link()
    # Consider two cases - data is there, data is not there
    test2 = linked1.copy_list()

    print("Delete Link: Data Present")
    print(test2.delete_link(13) != None)
    print()
    print("Delete Link: Data Not Present")
    print(test2.delete_link(104) != None)
    print()

    # Test method copy_list()
    print("Copy List:")
    linked4 = linked1.copy_list()
    print(linked1)
    print(linked4)
    print()

    # Test method reverse_list()
    print("Reverse List: linked1")
    linked_rev = linked1.reverse_list()
    print(linked_rev)
    print()

    # Test method sort_list()
    print("Sorted linked1:")
    print(linked1.sort_list())
    print()

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    print("Is sorted: False")
    print(linked1.is_sorted())
    print()
    print("Is sorted: True")
    print(linked1.sort_list().is_sorted())
    print()

    # Test method is_empty()
    emp = LinkedList()
    print("Is empty: True")
    print(emp.is_empty())
    print()
    print("Is empty: False")
    print(linked1.is_empty())
    print()

    # Test method merge_list()
    print("Merged List: linked1 and linked2")
    print(linked1.merge_list(linked2))
    print()

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    print("Is Equal: True")
    linked1_copy = linked1.copy_list()
    print(linked1_copy.is_equal(linked1))
    print()
    print("Is Equal: False")
    linked1_copy = linked2.copy_list()
    print(linked1.is_equal(linked1_copy))
    print()

    # Test remove_duplicates()
    print("Removed Duplicates:")
    dup = [1, 2, 3, 3, 4, 5, 6, 7, 8, 8, 9, 10]
    dup_list = LinkedList()
    for i in dup:
        dup_list.insert_last(i)
    print(dup_list.remove_duplicates())
    print()


if __name__ == "__main__":
    main()
