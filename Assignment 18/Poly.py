#  File: Poly.py

#  Description: Using linked lists, we can add and multiply polynomials.

#  Student Name: Adam Alam

#  Student UT EID: aba2288

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: November 10 2019

#  Date Last Modified: November 11 2019

class Link (object):
    def __init__ (self, coeff = 1, exp = 1, next = None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

    def __str__ (self):
        return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList(object):
    def __init__ (self):
        self.first = None

    # keep Links in descending order of exponents
    def insert_in_order (self, coeff, exp):
        newNode = Link(coeff, exp)
        cur = self.first
        prev = self.first
        if cur == None or cur.exp < exp:
            newNode.next = self.first
            self.first = newNode
            return
        while cur.next != None:
            if cur.exp < exp:
                newNode.next = prev.next
                prev.next = newNode
                return
            else:
                prev = cur
                cur = cur.next
        if cur.exp < exp:
            newNode.next = prev.next
            prev.next = newNode
        else:
            cur.next = newNode
        return
    # add polynomial p to this polynomial and return the sum
    def add (self, p):
        added = LinkedList()
        cur = self.first
        cur_p = p.first
        while True:
            if cur == None and cur_p == None:
                return added
            if cur_p and cur == None:
                exp = cur_p.exp
                coeff = cur_p.coeff
                cur_p = cur_p.next
            if cur and cur_p == None:
                exp = cur.exp
                coeff = cur.coeff
                cur = cur.next
            if cur and cur_p:
                if cur.exp > cur_p.exp:
                    exp = cur.exp
                    coeff = cur.coeff
                    cur = cur.next
                elif cur.exp < cur_p.exp:
                    exp = cur_p.exp
                    coeff = cur_p.coeff
                    cur_p = cur_p.next
                elif cur.exp == cur_p.exp:
                    coeff = cur.coeff + cur_p.coeff
                    exp = cur.exp
                    cur = cur.next
                    cur_p = cur_p.next
            added.insert_in_order(coeff, exp)

            
            
    # multiply polynomial p to this polynomial and return the product
    def mult (self, p):
        multiplied = LinkedList()
        cur = self.first
        while cur != None:
            pNode = p.first
            tempList = LinkedList()
            # Compares each node in self list to each node in other list and creates a temporary list which is added to returned list
            while pNode != None:
                tempList.insert_in_order(cur.coeff * pNode.coeff, cur.exp + pNode.exp)
                pNode = pNode.next
            cur = cur.next
            multiplied = multiplied.add(tempList)
        return multiplied

    # create a string representation of the polynomial
    def __str__ (self):
        cur = self.first
        st = ""
        if cur != None:
            st += f"({cur.coeff}, {cur.exp})"
            cur = cur.next
        while cur != None:
            st += f" + ({cur.coeff}, {cur.exp})"
            cur = cur.next
        return st.strip()


def main():
    # open file poly.txt for reading
    with open("poly.txt") as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        lines[i] = lines[i].split()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            try:
                lines[i][j] = int(lines[i][j])
            except:
                pass

    
    # create polynomial p

    # create polynomial q
    p = LinkedList()
    q = LinkedList()
    to_p = True
    for i in lines:
        if i == []:
            to_p = False
        if len(i) == 2:
            if to_p:
                p.insert_in_order(i[0], i[1])
            else:
                q.insert_in_order(i[0], i[1])
    
    
    # get sum of p and q and print sum
    print(f"Sum: {str(q.add(p))}")
    print()
    
    # get product of p and q and print product
    print(f"Product: {str(q.mult(p))}")

if __name__ == "__main__":
    main()