import random
import time
import math
import matplotlib.pyplot as plt
import networkx as nx

# Latitude and Longitude coordinates of the 5 cities
cities = {
    'New York City, NY': (40.7128, -74.0060),
    'Los Angeles, CA': (34.0522, -118.2437),
    'Chicago, IL': (41.8781, -87.6298),
    'Houston, TX': (29.7604, -95.3698),
    'Phoenix, AZ': (33.4484, -112.0740)
}

def calculate_distance(city1, city2):
    lat1, lon1 = city1
    lat2, lon2 = city2
    R = 6371  # Radius of the Earth in kilometers

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

def generate_random_graph():
    graph = {}
    for city1, coord1 in cities.items():
        distances = {}
        for city2, coord2 in cities.items():
            if city1 != city2:
                distances[city2] = calculate_distance(coord1, coord2)
        graph[city1] = distances
    return graph

def nearest_neighbor_tsp(graph, start_city):
    tour = [start_city]
    current_city = start_city
    unvisited_cities = set(graph.keys()) - {start_city}

    while unvisited_cities:
        nearest_city = min(unvisited_cities, key=lambda city: graph[current_city][city])
        tour.append(nearest_city)
        unvisited_cities.remove(nearest_city)
        current_city = nearest_city

    tour.append(start_city)  # Complete the cycle
    return tour

def dp_tsp(graph):
    n = len(graph)
    memo = {}

    def tsp_dp(curr, remaining):
        if not remaining:
            return graph[curr][start_city]  # Return to the starting city

        if (curr, remaining) in memo:
            return memo[(curr, remaining)]

        min_tour_length = float('inf')

        for next_city in remaining:
            new_remaining = tuple(city for city in remaining if city != next_city)
            tour_length = graph[curr][next_city] + tsp_dp(next_city, new_remaining)
            min_tour_length = min(min_tour_length, tour_length)

        memo[(curr, remaining)] = min_tour_length
        return min_tour_length

    start_city = next(iter(graph.keys()))  # Select the first city as the starting city
    remaining_cities = tuple(city for city in graph.keys() if city != start_city)
    shortest_tour_length = tsp_dp(start_city, remaining_cities)

    tour = [start_city]
    curr = start_city
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda city: graph[curr][city])
        tour.append(next_city)
        remaining_cities = tuple(city for city in remaining_cities if city != next_city)
        curr = next_city

    tour.append(start_city)

    return tour, shortest_tour_length

def benchmark_nearest_neighbor(graph_generator, iterations):
    total_time = 0
    for _ in range(iterations):
        graph = graph_generator()
        start_time = time.time()
        tour = nearest_neighbor_tsp(graph, 'New York City, NY')  # Start from New York City
        total_time += time.time() - start_time
    return total_time / iterations

def benchmark_dp_tsp(graph_generator, iterations):
    total_time = 0
    for _ in range(iterations):
        graph = graph_generator()
        start_time = time.time()
        tour, _ = dp_tsp(graph)
        total_time += time.time() - start_time
    return total_time / iterations

def visualize_tour(graph, tour):
    G = nx.Graph()
    for city1, distances in graph.items():
        for city2, distance in distances.items():
            G.add_edge(city1, city2, weight=distance)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edges(G, pos, edgelist=[(tour[i], tour[i+1]) for i in range(len(tour)-1)], edge_color='r', width=2)
    plt.show()

iterations = 1000
average_time_nn = benchmark_nearest_neighbor(generate_random_graph, iterations)
average_time_dp = benchmark_dp_tsp(generate_random_graph, iterations)

print("Average Runtime for Nearest Neighbor Algorithm (over", iterations, "iterations):", average_time_nn, "seconds")
print("Average Runtime for Dynamic Programming Approach (over", iterations, "iterations):", average_time_dp, "seconds")

graph = generate_random_graph()

# Nearest Neighbor Algorithm
tour_nn = nearest_neighbor_tsp(graph, 'New York City, NY')  # Start from New York City
print("Tour found by Nearest Neighbor Algorithm:", tour_nn)
visualize_tour(graph, tour_nn)

# Dynamic Programming Approach
tour_dp, _ = dp_tsp(graph)
print("Tour found by Dynamic Programming Approach:", tour_dp)
visualize_tour(graph, tour_dp)

iterations_range = [1, 10, 100, 1000,10000,100000]

# Benchmarking
average_times_nn = [benchmark_nearest_neighbor(generate_random_graph, it) for it in iterations_range]
average_times_dp = [benchmark_dp_tsp(generate_random_graph, it) for it in iterations_range]

plt.plot(iterations_range, average_times_nn, label='Nearest Neighbor')
plt.plot(iterations_range, average_times_dp, label='Dynamic Programming')
plt.xscale('log')  # Set logarithmic scale for x-axis
plt.xlabel('Number of Iterations (log scale)')
plt.ylabel('Average Runtime (seconds)')
plt.title('Benchmarking TSP Algorithms')
plt.legend()
plt.grid(True)
plt.show()
