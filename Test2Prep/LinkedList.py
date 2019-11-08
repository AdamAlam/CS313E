class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()
    
    def append(self, data):
        newNode = Node(data)
        cur = self.head
 
        # Find where the next node == None as that means you are at the end of the list
        while cur.next != None:
            # If not found, traverse through the list
            cur = cur.next
        # When cur.next == None, you have reached the last point of the list and now you can append the new node onto the list
        cur.next = newNode

    # Find the numbers of items in a linked list
    def length(self):
        cur = self.head
        links = 0
        while cur.next != None:
            links += 1
            cur = cur.next
        return links

    def display(self):
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        for i in elems:
            print(i, end=" ")

    def get(self, index):
        if index >= self.length():
            print('Error: "GET" index out of range')
            return
        cur_idx = 0
        cur = self.head
        while True:
            cur = cur.next
            if cur_idx == index:
                return cur.data
            cur_idx += 1

    def delete(self, index):
        if index >= self.length():
            print('Error: "DELETE" index out of range')
            return
        cur_idx = 0
        cur = self.head
        while True:
            last_node = cur
            cur = cur.next
            if cur_idx == index:
                last_node.next = cur.next
                return
            cur_idx += 1


my_list = LinkedList()
for i in range(7):
    my_list.append(i)

my_list.delete(1)
my_list.display()
