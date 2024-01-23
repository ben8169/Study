import queue


myGraph = {
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

print(bfs(myGraph, "A"))    #bfs -  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']


def dfs(graph, start):
    visited = []
    stack = []
    

    stack.append(start)

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))

    return visited

print(dfs(myGraph, 'A'))       #dfs -  ['A', 'B', 'E', 'I', 'C', 'F', 'J', 'G', 'D', 'H’]


def dfs_recursive(graph, start, visited=[]):
    print(visited)
    visited.append(start)
    for nbr in graph[start]:
        if nbr not in visited:
            dfs_recursive(graph, nbr, visited)
    return visited

print(dfs_recursive(myGraph, 'A'))
