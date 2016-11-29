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
        self.nodes.append(value)                        #adding a node value to a list
        self.edges[value] = []                          #adding a node to a dictionary and creating an empty list for the edges

    def printVertices(self):
        return self.nodes                               #returning the nodes list

    def addEdges(self, node1, node2):
        if node1 not in self.nodes:                     #if nodes not in the nodes list, append the nodes to the list
            self.nodes.append(node1)

        if node2 not in self.nodes:
            self.nodes.append(node2)

        self.edges[node1].append(node2)                 #adding the edges to the dictionaries, the edges are being added to an empty list created earlier
        self.edges[node2].append(node1)

    def DFS(self, start):
        visited = []
        stack = Stack()
        stack.push(start)                               #pushing the starting node to the stack
        while stack.isEmpty() == False:                 #while stack is not empty
            u = stack.pop()                             #pop the node from the stack and make it = u
            if u not in visited:
                visited.append(u)                       #if the node is not in visited, append it to the visited
                for edge in self.edges[u]:              #for all the edges = the value of u
                    stack.push(edge)                    #push the edges to the stack
        dfsText = open("dfsTraversalOutput.txt", "w")   #open a new text document, and set it's mode to write
        dfsText.write("DFS Traversal: %s " % visited)   #write the list to the file
        dfsText.close()                                 #close the file

    def BFS(self, start):
        Q = Queue()
        visited = []
        Q.enqueue(start)                                #enqueuing the first node to the queue
        while Q.isEmpty() == False:                     #while queue is not empty
            u = Q.dequeue()                             #dequeue the node from queue and make it = u
            if u not in visited:
                visited.append(u)                       #if the node not in visited, append it to visited
                for edge in self.edges[u]:              #for all the edges = to the value of u
                    Q.enqueue(edge)                     #enqueue the edges to the queue
        bfsText = open("bfsTraversalOutput.txt", "w")   #open a new text document, and set it's mode to write
        bfsText.write("BFS Traversal: %s " % visited)   #write the list to the file
        bfsText.close()                                 #close the file




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



