class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

class Vertex():

    def __init__(self):
        self.vertices = []


class Graph():

    def __init__(self):
        self.edges = []
        self.v = Vertex()

    def addVertex(self, node):
        self.v.vertices.append(node)

    def addEdge(self, node1, node2):
        if node1 in self.v.vertices and node2 in self.v.vertices:
            edge = [node1, node2]
            self.edges.append(edge)
            return self.edges
        else:
            pass


    def DFS(self, start):
        S =

if __name__ == "__main__":
    g = Graph()
    v = Vertex()
    g.addVertex(1)
    g.addVertex(2)
    g.addVertex(10)
    g.addVertex(6)
    g.addVertex(8)
    g.addVertex(15)
    g.addVertex(9)
    g.addVertex(11)
    g.addEdge(1,2)
    g.addEdge(9,11)
    g.addEdge(10,6)
    g.addEdge(8, 15)
    g.addEdge(6,2)
    print(g.edges)