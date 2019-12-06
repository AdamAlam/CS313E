class Edge:
    def __init__(self, from_v, to_v, weight=1):
        self.from_v = from_v
        self.to_v = to_v
        self.weight = weight
     
        
class Vertex:
    def __init__(self, label):
        self.label = label
        self.visited = False
    
    def __str__(self):
        return str(self.label)

class Graph:
    def __init__(self):
        self.Vertices = []
        self.edges = []
        self.matrix = []

    def get_index(self, s_label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if self.Vertices[i].label == s_label:
                return i
        return -1
    
    def add_vertex(self, n_label):
        if not self.has_label(n_label):
            self.Vertices.append(Vertex(n_label))
            for i in range(len(self.Vertices)-1):
                self.matrix[i].append(0)
            new_row = [0] * len(self.Vertices)
            self.matrix.append(new_row)

            
    def has_label(self, s_label):
        for vertex in self.Vertices:
            if s_label == vertex.label:
                return True
        return False
    
    # start and finished are indexes
    def add_directed_edge(self, start, finish, weight=1):
        self.matrix[start][finish] = weight
        edge = Edge(self.Vertices[start], self.Vertices[finish], weight)
        self.edges.append(edge)
    
def main():
    f = open("mat.txt", "r")
    nVert = int(f.readline().strip())
    graph = Graph()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in range(nVert):
        graph.add_vertex(alpha[i])
    for i in range(nVert):
        row = f.readline().strip().split()
        for j in range(len(row)):
            if int(row[j]) != 0:
                graph.add_directed_edge(i, j, int(row[j]))
    
    for i in graph.matrix:
        for j in i:
            print(j, end=" ")
        print()
    print()
    
main()