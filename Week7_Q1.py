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


class Graph():

    def __init__(self):
        self.nodes = []
        self.edges = dict()



    def addVertex(self,value):
        self.nodes.append(value)

        if value in self.nodes:
            self.edges[value] = []
        else:
            pass
    def printVertices(self):
        return self.nodes

    def addEdges(self, node1, node2):
        if node1 not in self.nodes:
            self.nodes.append(node1)

        if node2 not in self.nodes:
            self.nodes.append(node2)

        self.edges[node1].append(node2)
        self.edges[node2].append(node1)

    def DFS(self, start):
        S = Stack()
        visited = []
        S.push(start)
        print(S.items)
        while S != None:
            u = S.pop()
            print("LOL" , S.items)
            print("LEL",u)
            if u not in visited:
                visited.append(u)
                print("visited" ,visited)
                for self.edges in range(u):
                    S.push(self.edges)
        return visited


if __name__ == '__main__':
    g = Graph()
    g.addVertex(1)
    g.addVertex(5)
    g.addVertex(3)
    g.addVertex(4)
    g.addVertex(10)
    g.addVertex(7)
    g.addEdges(1,5)
    g.addEdges(1,3)
    g.addEdges(10,7)
    g.addEdges(4,10)
    g.addEdges(5,10)
    for node in g.edges:
        print(node, ":", g.edges[node])
    print(g.printVertices())
    g.DFS(1)




