#  File: ExpressionTree.py

#  Description: Using the tree data structure, we can reorder infix expression into postfix or prefix expression

#  Student's Name: Adam Alam

#  Student's UT EID: aba2288

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: November 12 2019

#  Date Last Modified: November 15 2019


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


class Node:
    def __init__(self, data=None):
        self.data = data
        self.lchild = None
        self.rchild = None


class Tree(object):
    def __init__(self):
        self.root = Node()

    def create_tree(self, expr):
        eq = expr.split()
        cur = self.root
        parentheses = Stack()
        operators = ['+', '-', '*', '/', '//', '%', '**']
        for token in eq:
            if token == "(":
                parentheses.push(cur)
                cur.lchild = Node()
                cur = cur.lchild
            elif token in operators:
                cur.data = token
                parentheses.push(cur)
                cur.rchild = Node()
                cur = cur.rchild
            elif is_num(token):
                cur.data = token
                cur = parentheses.pop()
            elif token == ")":
                if parentheses.is_empty() is False:
                    cur = parentheses.pop()
                else:
                    break

    def evaluate(self, aNode):
        if aNode.data == "+":
            return self.evaluate(aNode.lchild) + self.evaluate(aNode.rchild)
        elif aNode.data == "-":
            return self.evaluate(aNode.lchild) - self.evaluate(aNode.rchild)
        elif aNode.data == "*":
            return self.evaluate(aNode.lchild) * self.evaluate(aNode.rchild)
        elif aNode.data == "/":
            return self.evaluate(aNode.lchild) / self.evaluate(aNode.rchild)
        elif aNode.data == "//":
            return self.evaluate(aNode.lchild) // self.evaluate(aNode.rchild)
        elif aNode.data == "%":
            return self.evaluate(aNode.lchild) % self.evaluate(aNode.rchild)
        elif aNode.data == "**":
            return self.evaluate(aNode.lchild) ** self.evaluate(aNode.rchild)
        elif is_num(aNode.data):
            return float(aNode.data)

    def pre_order(self, aNode):
        if aNode is not None:
            print(aNode.data, end=" ")
            self.pre_order(aNode.lchild)
            self.pre_order(aNode.rchild)

    def post_order(self, aNode):
        if aNode is not None:
            self.post_order(aNode.lchild)
            self.post_order(aNode.rchild)
            print(aNode.data, end=' ')


def is_num(token):
    if token:
        return (token.isdigit() or '.' in token)
    return False


def main():
    with open("expression.txt") as f:
        expression = f.readline()
    expression = expression.strip()
    tree = Tree()
    tree.create_tree(expression)
    print(f"{expression} = {tree.evaluate(tree.root)}\n")
    print("Prefix Expression: ", end='')
    tree.pre_order(tree.root)
    print()
    print()
    print(f"Postfix Expression: ", end='')
    tree.post_order(tree.root)


main()
