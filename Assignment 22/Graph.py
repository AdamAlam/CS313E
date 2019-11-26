#  File: Graph.py

#  Description: Wrote functions for DFS and BFS anf various methods for the graph class

#  Student Name: Adam Alam

#  Student UT EID: aba2288

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: November 23 2019

#  Date Last Modified: November 25 2019


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return(self.queue.pop(0))

    def is_empty(self):
        return self.queue == []


class Vertex:
    def __init__(self, label):
        self.label = label
        self.visited = False

    def get_label(self):
        return self.label

    def __str__(self):
        return str(self.label)


class Edge:
    def __init__(self, fromVertex, toVertex, weight):
        self.u = fromVertex
        self.v = toVertex
        self.weight = weight


class Graph (object):
    def __init__(self):
        self.Vertices = []
        self.edges = []
        self.adj_mat = []

    # check if a vertex is already in the graph
    def has_vertex(self, label):
        num_vert = len(self.Vertices)
        exists = False
        for i in range(num_vert):
            if label == self.Vertices[i].label:
                exists = True
        return exists

    # get the index from the vertex label
    def get_index(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1

    # Sets all vertices' visited attribute to false
    def visit_reset(self):
        nVert = len(self.Vertices)
        for i in range(nVert):
            self.Vertices[i].visited = False

    # add a Vertex object with a given label to the graph
    def add_vertex(self, label):
        if not self.has_vertex(label):
            self.Vertices.append(Vertex(label))
            nVert = len(self.Vertices)
            for i in range(nVert - 1):
                self.adj_mat[i].append(0)
            new_row = []
            for i in range(nVert):
                new_row.append(0)
            self.adj_mat.append(new_row)

    # add weighted directed edge to graph
    def add_directed_edge(self, start, finish, weight=1):
        self.adj_mat[start][finish] = weight
        edge = Edge(self.Vertices[start], self.Vertices[finish], weight)
        self.edges.append(edge)

    # add weighted undirected edge to graph
    def add_undirected_edge(self, start, finish, weight=1):
        self.adj_mat[start][finish] = weight
        self.adj_mat[finish][start] = weight
        edge1 = Edge(self.Vertices[start], self.Vertices[finish], weight)
        edge2 = Edge(self.Vertices[finish], self.Vertices[start], weight)
        self.edges.append(edge1)
        self.edges.append(edge2)

    # get edge weight between two vertices
    # return -1 if edge does not exist
    def get_edge_weight(self, fromVertexLabel, toVertexLabel):
        i = self.get_index(fromVertexLabel)
        j = self.get_index(toVertexLabel)
        if self.adj_mat != 0:
            return self.adj_mat[i][j]
        return -1

    # get a list of immediate neighbors that you can go to from a vertex
    # return a list of indices or an empty list if there are none
    def get_neighbors(self, vertexLabel):
        neighbors = []
        idx = self.get_index(vertexLabel)
        vert = self.adj_mat[idx]
        for i in range(len(vert)):
            if vert[i] != 0:
                neighbors.append(self.Vertices[i])
        return neighbors

    # return an index to an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if self.adj_mat[v][i] > 0 and not self.Vertices[i].visited:
                return i
        return -1

    # get a copy of the list of Vertex objects
    def get_vertices(self):
        return self.Vertices.copy()

    # do a depth first search in a graph starting at vertex v (index)
    def dfs(self, v):
        dfs_stack = Stack()
        self.Vertices[v].visited = True
        print(self.Vertices[v])
        dfs_stack.push(v)

        while not dfs_stack.is_empty():
            u = self.get_adj_unvisited_vertex(dfs_stack.peek())
            if u == -1:
                u = dfs_stack.pop()
            else:
                self.Vertices[u].visited = True
                print(self.Vertices[u])
                dfs_stack.push(u)
        self.visit_reset()

    # do a breadth first search in a graph starting at vertex v (index)
    def bfs(self, v):
        q = Queue()
        self.Vertices[v].visited = True
        print(self.Vertices[v])
        q.enqueue(v)
        while not q.is_empty():
            v1 = q.dequeue()
            v2 = self.get_adj_unvisited_vertex(v1)
            while v2 != -1:
                self.Vertices[v2].visited = True
                print(self.Vertices[v2])
                q.enqueue((v2))
                v2 = self.get_adj_unvisited_vertex(v1)
        self.visit_reset()

    # delete an edge from the adjacency matrix
    # delete a single edge if the graph is directed
    # delete two edges if the graph is undirected
    def delete_edge(self, fromVertexLabel, toVertexLabel):
        f_idx = self.get_index(fromVertexLabel)
        t_idx = self.get_index(toVertexLabel)
        if f_idx != -1 and t_idx != -1 and self.adj_mat[f_idx][t_idx] != 0:
            self.adj_mat[f_idx][t_idx] = 0
            self.adj_mat[t_idx][f_idx] = 0

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex(self, vertexLabel):
        idx = self.get_index(vertexLabel)
        self.Vertices.pop(idx)
        del self.adj_mat[idx]
        cols = len(self.adj_mat)
        for row in range(cols):
            del self.adj_mat[row][idx]


def main():
    cities = Graph()

    in_file = open("graph.txt", "r")

    nVert = int(in_file.readline().strip())

    for i in range(nVert):
        city = in_file.readline().strip()
        cities.add_vertex(city)

    num_edges = int(in_file.readline().strip())
    for i in range(num_edges):
        edge = in_file.readline().strip()
        edge = edge.split()
        cities.add_directed_edge(int(edge[0]), int(edge[1]), int(edge[2]))

    start_vertex = (in_file.readline().strip())
    start_idx = cities.get_index(start_vertex)

    # test depth first search
    print("Depth First Search")
    cities.dfs(start_idx)
    print()

    # test breadth first search
    print("Breadth First Search")
    cities.bfs(start_idx)
    print()

    # test deletion of an edge
    edges = in_file.readline().strip()
    edges = edges.split()
    print("Deletion of an edge\n")
    cities.delete_edge(edges[0], edges[1])
    print("Adjacency Matrix")
    for i in range(nVert):
        for j in range(nVert):
            print(cities.adj_mat[i][j], end=" ")
        print()
    print()

    # test deletion of a vertex
    print("Deletion of a vertex\n")
    del_vert = in_file.readline().strip()
    cities.delete_vertex(del_vert)
    nVert -= 1
    print("List of Vertices")
    for i in cities.Vertices:
        print(i)
    print()
    print("Adjacency Matrix")
    for i in range(nVert):
        for j in range(nVert):
            print(cities.adj_mat[i][j], end=" ")
        print()
    print()

    in_file.close()


if __name__ == "__main__":
    main()
