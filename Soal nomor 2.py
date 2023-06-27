import time

# Implementasi algoritma TSP

def tsp(graph, start):
    nodes = list(graph.keys())
    visited = [False] * len(nodes)
    visited[start] = True
    path = [start]
    total_distance = 0

    while len(path) < len(nodes):
        current_node = path[-1]
        min_distance = float('inf')
        next_node = None

        for neighbor, distance in graph[current_node].items():
            if not visited[neighbor] and distance < min_distance:
                min_distance = distance
                next_node = neighbor

        if next_node is None:
            break

        path.append(next_node)
        visited[next_node] = True
        total_distance += min_distance

        print(f"Iterasi {len(path)-1}: Path = {path}, Distance = {total_distance}")

    # Kembali ke node awal
    path.append(start)
    total_distance += graph[path[-2]][start]

    print(f"Shortest Path: {path}, Distance = {total_distance}")
    return path, total_distance


# Implementasi algoritma Dijkstra

def dijkstra(graph, start):
    nodes = list(graph.keys())
    distance = {node: float('inf') for node in nodes}
    distance[start] = 0
    visited = [False] * len(nodes)

    while True:
        min_distance = float('inf')
        min_node = None

        for node in nodes:
            if not visited[node] and distance[node] < min_distance:
                min_distance = distance[node]
                min_node = node

        if min_node is None:
            break

        visited[min_node] = True

        for neighbor, edge_weight in graph[min_node].items():
            new_distance = distance[min_node] + edge_weight
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance

        print(f"Visited node: {min_node}, Distance = {distance}")

    return distance


# Contoh penggunaan

graph = {
    'A': {'B': 12, 'C': 10, 'G': 12},
    'B': {'C': 8, 'D': 12},
    'C': {'D': 11, 'E': 3, 'G': 9},
    'D': {'C': 11, 'E': 11, 'F': 10},
    'E': {'G': 7, 'F': 6},
    'G': {'A': 12, 'C': 9, 'E': 7, 'F': 9},
    'F': {}
}

choice = input("Pilih algoritma (TSP/Dijkstra): ")

if choice.lower() == "tsp":
    start = int(input("Masukkan node awal: "))
    start_time = time.time()
    tsp(graph, start)
    end_time = time.time()
elif choice.lower() == "dijkstra":
    start = int(input("Masukkan node awal: "))
    start_time = time.time()
    shortest_distances = dijkstra(graph, start)
    end_time = time.time()
    print("Shortest distances:", shortest_distances)
else:
    print("Pilihan tidak valid.")

execution_time = end_time - start_time
print("Waktu komputasi:", execution_time)
