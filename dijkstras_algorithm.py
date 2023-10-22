import sys

# Function to find the vertex with the minimum distance value
def min_distance(dist, visited):
    min_dist = sys.maxsize
    min_vertex = None

    for v in range(len(dist)):
        if dist[v] < min_dist and not visited[v]:
            min_dist = dist[v]
            min_vertex = v

    return min_vertex

# Function to print the result of Dijkstra's algorithm
def print_solution(dist):
    print("Vertex \t Distance from Source")
    for i in range(len(dist)):
        print(f"{i}\t {dist[i]}")

# Dijkstra's algorithm
def dijkstra(graph, source):
    num_vertices = len(graph)
    dist = [sys.maxsize] * num_vertices  # Initialize distances
    dist[source] = 0  # Distance from source to itself is 0
    visited = [False] * num_vertices

    for _ in range(num_vertices - 1):
        u = min_distance(dist, visited)
        visited[u] = True

        for v in range(num_vertices):
            if not visited[v] and graph[u][v] > 0 and dist[u] != sys.maxsize and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

    print_solution(dist)

# Example graph represented as an adjacency matrix
graph = [
    [0, 2, 0, 1, 0],
    [2, 0, 3, 2, 0],
    [0, 3, 0, 0, 1],
    [1, 2, 0, 0, 2],
    [0, 0, 1, 2, 0]
]

# Find and print the shortest paths from source vertex 0
dijkstra(graph, 0)
