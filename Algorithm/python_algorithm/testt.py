import queue


graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['A', 'H'],
    'E': ['B', 'I'],
    'F': ['C', 'J'],
    'G': ['C'],
    'H': ['D'],
    'I': ['E'],
    'J': ['F']
}

def bfs(graph, start):
    Q = queue.Queue()
    visited = []
    Q.put(start)
    visited.append(start)

    while not Q.empty():
        current = Q.get()

        for nbr in graph[current]:
            if nbr not in visited:
                Q.put(nbr)
                visited.append(nbr)
    return visited

print(bfs(graph, "A"))    #bfs -  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']