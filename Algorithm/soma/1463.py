# N = int(1000)
# def process(N):
#     tbl = [None]*(N+1)
#     tbl[0] = 0
#     if N == 1: return tbl[0]
#     if N%3 ==0 :
#         if N%2 ==0: 
#             if tbl[N//3] == None:
#                 tbl[N//3] = process(N//3)
#             if tbl[N//2] == None:
#                 tbl[N//2] = process(N//2)
#             if tbl[N-1] == None:
#                 tbl[N-1] = process(N-1)
#             return 1 + min(tbl[N//3],tbl[N//2],tbl[N-1])
#         else: 
#             if tbl[N//3] == None:
#                 tbl[N//3] = process(N//3)
#             if tbl[N-1] == None:
#                 tbl[N-1] = process(N-1)
#             return 1 + min(tbl[N//3],tbl[N-1])
#     elif N%2 == 0: 
#         if tbl[N//2] == None:
#             tbl[N//2] = process(N//2)
#         if tbl[N-1] == None:
#             tbl[N-1] = process(N-1)
#         return 1 + min(tbl[N//2],tbl[N-1])
#     else: 
#         if tbl[N-1] == None:
#             tbl[N-1] = process(N-1)        
#         return tbl[N-1]

# print(process(N))



N = int(input())

tbl = [0]*(N+1)

for i in range(2, N+1):
    tbl[i] = tbl[i-1]+1
    
    if i%2 == 0:
        tbl[i] = min(tbl[i], tbl[i//2]+1)
    if i%3 == 0:
        tbl[i] = min(tbl[i], tbl[i//3]+1)

print(tbl[N])