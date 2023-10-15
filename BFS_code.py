from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

graph = {}
num_edges = int(input("Enter the number of edges: "))

for _ in range(num_edges):
    src, dest = input("Enter an edge (source destination): ").split()
    if src not in graph:
        graph[src] = []
    if dest not in graph:
        graph[dest] = []
    graph[src].append(dest)
    graph[dest].append(src)

start_node = input("Enter the starting node: ")

print("BFS traversal starting from node", start_node, ":")
bfs(graph, start_node)
