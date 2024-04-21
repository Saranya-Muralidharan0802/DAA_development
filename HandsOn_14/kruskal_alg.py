class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal_mst(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        return result


# Figure 23.4 with labeled vertices
g = Graph(9)
g.add_edge(0, 1, 4)  # a-b
g.add_edge(0, 7, 8)  # a-h
g.add_edge(1, 7, 11)  # b-h
g.add_edge(1, 2, 8)  # b-c
g.add_edge(7, 8, 7)  # h-i
g.add_edge(6, 7, 1)  # g-h
g.add_edge(6, 8, 6)  # g-i
g.add_edge(2, 8, 2)  # c-i
g.add_edge(2, 5, 4)  # c-f
g.add_edge(2, 3, 7)  # c-d
g.add_edge(5, 3, 14)  # f-d
g.add_edge(5, 4, 10)  # f-e
g.add_edge(3, 4, 9)  # d-e

mst = g.kruskal_mst()

vertex_labels = {
    0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e',
    5: 'f', 6: 'g', 7: 'h', 8: 'i'
}

print("Minimum Spanning Tree:")
for u, v, w in mst:
    print(f"{vertex_labels[u]} -- {vertex_labels[v]} == {w}")
