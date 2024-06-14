from itertools import permutations 
N, M = map(int, input().split())



num_list = list(range(1,N+1))

for i in permutations(num_list,M):
    for element in i:
        print(element, end=' ')
    print()

