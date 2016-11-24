class Graph():

    def __init__(self):
        self.nodes = []
        self.edges = dict()
        self.weights = {}



    def addVertex(self,value):
        self.nodes.append(value)

        if value in self.nodes:
            self.edges[value] = []
        else:
            pass
    def printVertices(self):
        return self.nodes

    def addEdges(self, node1, node2, weight):
        if node1 not in self.nodes or node2 not in self.nodes:
            pass
        else:
            self.edges[node1].append(node2)
            self.edges[node2].append(node1)
            self.weights[(node1, node2)] = weight

    def dijsktra(self, start):
        visited = {start: 0}
        path = {}

        nodes = set(self.nodes)

        while nodes:
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node

            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = visited[min_node]

            for edge in self.edges[min_node]:
                print(path)
                weeights = current_weight + self.weights[(min_node, edge)]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weeights
                    path[edge] = min_node

        return visited, path






if __name__ == '__main__':
    g = Graph()
    g.addVertex(1)
    g.addVertex(5)
    g.addVertex(3)
    g.addVertex(4)
    g.addVertex(10)
    g.addVertex(7)
    g.addEdges(1,5,5)
    g.addEdges(1,3,2)
    g.addEdges(10,7,4)
    g.addEdges(4,10,3)
    g.addEdges(5,10,1)
    for node in g.edges:
       print(node, ":", g.edges[node])
    print(g.printVertices())
    for weight in g.weights:
        print(weight, ":", g.weights[weight])

    g.dijsktra(1)





