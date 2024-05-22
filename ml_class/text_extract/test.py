import queue

N, M, V = list(map(int, input().split()))

graph = dict()
for i in range(M):
    x, y = list(map(int, input().split()))
    if x not in graph:
        graph[x] = [y]
    else:
        graph[x].append(y)
    if y not in graph:
        graph[y] = [x]
    else:
        graph[y].append(x)
print(graph)

# def DFS(graph, start):
# 	stk = queue.LifoQueue()
# 	stk.put(start)
# 	visited = [start]

# 	while not stk.empty():
# 		node = stk.get()
# 		if node not in visited:
# 			visited.append(node)
# 			for n in graph[node]:
# 				stk.put(n)             

# 	print(*visited)
def DFS(graph, start):
    stk = queue.LifoQueue()
    stk.put(start)
    visited = []  # 방문한 노드를 저장할 리스트

    while not stk.empty():
        node = stk.get()
        if node not in visited:
            visited.append(node)  # 방문한 노드를 리스트에 추가
            if node in graph:  # 그래프에 현재 노드가 있는지 확인
                for n in reversed(graph[node]):  # 현재 노드와 연결된 노드들에 대해
                    stk.put(n)  # 스택에 추가하여 탐색 진행

    print(*visited)  # 탐색이 끝난 후 방문한 노드들을 출력

def BFS(graph, start):
    Q = queue.Queue()
    Q.put(start)
    visited = [start]

    while not Q.empty():
        tmp = Q.get()
        if tmp in graph:
            for node in graph[tmp]:
                if node not in visited:
                    Q.put(node)
                    visited.append(node)
    print(*visited)

DFS(graph, V)
BFS(graph, V)
