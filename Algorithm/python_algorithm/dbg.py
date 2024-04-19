# #6
# def square_matrix(M,n):
#     if n>=len(M): return n**2
#     if M[n-1][n-1] == 1: 
#         for i in range(n+1):
#             for j in range(n+1):
#                 print(i,j)
#                 if M[n-j][n-i]==0:
#                     break
#         else:
#           square_matrix(M,n+1)

#     return n**2
# M = [[1,1],[1,1]]

# square_matrix(M,1)


# 주어진 인접 리스트
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

# 노드의 수
num_nodes = len(myGraph)

# 인접 행렬 초기화
adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]

# 노드와 인덱스 매핑
node_index = {node: index for index, node in enumerate(myGraph)}

# 인접 행렬 채우기
for node, neighbors in myGraph.items():
    for neighbor in neighbors:
        adj_matrix[node_index[node]][node_index[neighbor]] = 1

# 인접 행렬 출력
for row in adj_matrix:
    print(row)
