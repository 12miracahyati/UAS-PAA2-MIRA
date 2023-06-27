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
    0: {1: 2, 2: 4, 3: 1},
    1: {0: 2, 2: 3, 3: 4},
    2: {0: 4, 1: 3, 3: 2},
    3: {0: 1, 1: 4, 2: 2}
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
