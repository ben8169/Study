N,M = map(int,input().split())
board = [list(map(int,input())) for _ in range(N)]


if N == 1 or M == 1:
    print(1)


length = min(M,N)-1
answer = 0
while length > 0:
    for i in range(N-length):
        for j in range(M-length):
            if board[i][j] == board[i][j+length] and board[i][j] == board[i+length][j] and board[i][j] == board[i+length][j+length]:
                print((length+1)**2)
                answer = 1
                break
            else:
                pass
    if answer > 0:
        break
    length -= 1

else:
    print(1)



