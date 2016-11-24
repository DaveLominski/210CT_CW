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

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

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
        visited = []
        stack = Stack()
        stack.push(start)
        while stack.isEmpty() == False:
            u = stack.pop()
            if u not in visited:
                visited.append(u)
                for edge in self.edges[u]:
                    stack.push(edge)
        return(visited)

    def BFS(self, start):
        Q = Queue()
        visited = []
        Q.enqueue(start)
        while Q.isEmpty() == False:
            u = Q.dequeue()
            if u not in visited:
                visited.append(u)
                for edge in self.edges[u]:
                    Q.enqueue(edge)
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
    print(g.DFS(7))
    print(g.BFS(7))



