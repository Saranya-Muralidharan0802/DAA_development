class Vertex:
    def __init__(self, data):
        self.data = data
        self.color = 0
        self.dt = 0
        self.ft = 0
        self.predecessor = None

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = {}
        self.time = 0

    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = [v]
        else:
            self.adj[u].append(v)

    def add_vertex(self, vertex):
        self.adj[vertex] = []

    def DFS(self):
        for v in self.adj.keys():
            v.color = 0
            v.predecessor = None
        self.time = 0
        for v in self.adj.keys():
            if v.color == 0:
                self.DFS_Visit(v)

    def DFS_Visit(self, vertex):
        self.time += 1
        vertex.dt = self.time
        vertex.color = 1
        for v in self.adj[vertex]:
            if v.color == 0:
                v.predecessor = vertex
                self.DFS_Visit(v)
        vertex.color = 2
        self.time += 1
        vertex.ft = self.time

    def __str__(self):
        print("\n ---Adjacency List ---")
        for v in self.adj.keys():
            print(v.data, end=": ")
            for j in self.adj[v]:
                print(j.data, end=" ")
            print("\b")
        return "---End of Adjacency List ---\n"

#figure 22.4 of Chapter 22 CLRS
if __name__ == "__main__":
    graph = Graph(6)
    u, v, w, x, y, z = Vertex('u'), Vertex('v'), Vertex('w'), Vertex('x'), Vertex('y'), Vertex('z')
    graph.add_edge(u, v)
    graph.add_edge(u, x)
    graph.add_edge(x, v)
    graph.add_edge(v, y)
    graph.add_edge(y, x)
    graph.add_edge(w, y)
    graph.add_edge(w, z)
    graph.add_edge(z, z)

    graph.DFS()
    print("DFS: ", end="")
    for i in graph.adj.keys():
        print(f"{i.data} ({i.dt}/{i.ft}),", end=" ")
