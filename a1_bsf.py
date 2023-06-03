# Recursive Breadth-First Search (BFS)
def bfs(graph, queue=None, visited=None):
    if queue is None:
        queue = []
    if visited is None:
        visited = []

    if len(queue) == 0:
        return

    current_node = queue.pop(0)
    visited.append(current_node)
    print(current_node)  # Process the vertex

    for neighbor in graph[current_node]:
        if neighbor not in visited and neighbor not in queue:
            queue.append(neighbor)

    bfs(graph, queue, visited)


# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("\nBFS traversal:")
bfs(graph, ['A'], [])
