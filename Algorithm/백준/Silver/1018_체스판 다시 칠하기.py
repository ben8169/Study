# https://www.acmicpc.net/problem/1018
M, N = int(input().split())
testcase = M-7 * N-7


entire_board = []
for i in range(M):
    a = input()
    entire_board.append(a)

def check(src):
    x = src[0][0]
    cnt = 0
    
