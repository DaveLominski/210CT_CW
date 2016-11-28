import math
class Graph():

    def __init__(self):
        self.nodes = []
        self.edges = {}
        self.weights = {}
        self.prev = None

    def addVertex(self,value):
        self.nodes.append(value)

        if value in self.nodes:
            self.weights[value] = {}
            self.edges[value] = []
        else:
            pass
    def printVertices(self):
        return self.nodes

    def addEdges(self, node1, node2, weight):
        if node1 not in self.nodes or node2 not in self.nodes:
            pass
        else:
            #1st way of storing weights
            #self.edges[node1].append(node2)
            #self.edges[node2].append(node1)
            #self.weights[(node1, node2)] = weight

            #2nd way of storing weights
            edge1 = dict({node2: weight})
            edge2 = dict({node1: weight})
            self.weights[node1].update(edge1)
            self.weights[node2].update(edge2)

    def dijsktra(self, start, end):
        v = start
        previous = []
        for k, e in self.weights.items():
            self.weights[k] = math.inf
        self.weights[start] = 0
        visited = []
        while v != end:
            for u in self.weights:
                if (self.weights[v] + self.weights[v]) < self.weights[v]:
                    self.weights[u] =  (self.weights[v] + self.weights[v[u]])
                    previous.append(v)
                    previous[u] = v
            visited.append(v)
            min = math.inf
            for n in visited:
                if n not in visited:
                    v = n
                    min = self.weights[n]
        return visited, previous

if __name__ == '__main__':
    g = Graph()
    for i in (22, 33, 44, 55, 66, 77, 88):
        g.addVertex(i)
    g.addEdges(22,33,5)
    g.addEdges(33,55,2)
    g.addEdges(44,66,4)
    g.addEdges(55,88,3)
    g.addEdges(77,22,1)
    g.addEdges(55,44, 6)
    #for node in g.edges:
     #  print("EDGES " ,node, ":", g.edges[node])
    #print(g.printVertices())
    for nodes in g.weights:
        print("WEIGHTS " ,nodes, ":", g.weights[nodes])
    print(g.weights[33][22]) #How to access the weights in the dictionary
    print(g.weights[33])

    print((g.dijsktra(22,77)))





