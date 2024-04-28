def floyd_warshall(graph):
    n = len(graph)
    distances = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        distances[i][i] = 0
    for u in range(n):
        for v in range(n):
            distances[u][v] = graph[u][v]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i][k] != float('inf') and distances[k][j] != float('inf'):
                    distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    return distances


# Given graph
W = [
    [0, 3, 8, float('inf'), -4],
    [float('inf'), 0, float('inf'), 1, 7],
    [float('inf'), 4, 0, float('inf'), float('inf')],
    [2, float('inf'), -5, 0, float('inf')],
    [float('inf'), float('inf'), float('inf'), 6, 0]
]

shortest_distances = floyd_warshall(W)
print("Shortest distances between all pairs of vertices:")
for row in shortest_distances:
    print(row)
