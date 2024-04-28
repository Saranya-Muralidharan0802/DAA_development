import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {v: [] for v in vertices}

    def add_edge(self, source, destination, weight):
        self.adjacency_list[source].append((destination, weight))

def initialize_single_source(vertices, source):
    distance = {v: float('inf') for v in vertices}
    distance[source] = 0
    predecessor = {v: None for v in vertices}
    return distance, predecessor

def relax(u, v, weight, distance, predecessor):
    if distance[v] > distance[u] + weight:
        distance[v] = distance[u] + weight
        predecessor[v] = u

def dijkstra(graph, source):
    vertices = graph.vertices
    distance, predecessor = initialize_single_source(vertices, source)
    pq = [(0, source)]  # Priority queue with tuple (distance, vertex)
    visited = set()

    while pq:
        dist_u, u = heapq.heappop(pq)
        visited.add(u)
        for v, weight in graph.adjacency_list[u]:
            if v not in visited:
                relax(u, v, weight, distance, predecessor)
                heapq.heappush(pq, (distance[v], v))

    return distance, predecessor

# Example usage:
vertices = [0, 1, 2, 3, 4]  # s: 0, t: 1, x: 2, y: 3, z: 4
graph = Graph(vertices)
graph.add_edge(0, 1, 10)
graph.add_edge(0, 3, 5)
graph.add_edge(1, 2, 1)
graph.add_edge(1, 3, 2)
graph.add_edge(2, 4, 4)
graph.add_edge(3, 1, 3)
graph.add_edge(3, 2, 9)
graph.add_edge(3, 4, 2)
graph.add_edge(4, 0, 7)
graph.add_edge(4, 2, 6)

source = 0

distance, predecessor = dijkstra(graph, source)
print("Shortest distances from vertex", source)
for v in vertices:
    print("Vertex:", v, "Distance:", distance[v], "Predecessor:", predecessor[v])
