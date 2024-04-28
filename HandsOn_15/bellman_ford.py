class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

def initialize_single_source(vertices, source):
    distance = {v: float('inf') for v in vertices}
    distance[source] = 0
    predecessor = {v: None for v in vertices}
    return distance, predecessor

def relax(u, v, weight, distance, predecessor):
    if distance[v] > distance[u] + weight:
        distance[v] = distance[u] + weight
        predecessor[v] = u

def bellman_ford(vertices, edges, source):
    distance, predecessor = initialize_single_source(vertices, source)
    for _ in range(len(vertices) - 1):
        for edge in edges:
            relax(edge.source, edge.destination, edge.weight, distance, predecessor)
    for edge in edges:
        if distance[edge.destination] > distance[edge.source] + edge.weight:
            return False
    return distance, predecessor

# Example usage:
vertices = ['s', 't', 'x', 'y', 'z']
edges = [
    Edge('s', 't', 6),
    Edge('s', 'y', 7),
    Edge('t', 'x', 5),
    Edge('t', 'y', 8),
    Edge('t', 'z', -4),
    Edge('x', 't', -2),
    Edge('y', 'x', -3),
    Edge('y', 'z', 9),
    Edge('z', 'x', 7),
    Edge('z', 's', 2)
]
source = 's'

result = bellman_ford(vertices, edges, source)
if result:
    distance, predecessor = result
    print("Shortest distances from", source)
    for v in vertices:
        print("Vertex:", v, "Distance:", distance[v], "Predecessor:", predecessor[v])
else:
    print("Negative cycle detected")
