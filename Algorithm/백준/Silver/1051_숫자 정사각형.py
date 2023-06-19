N,M = map(int,input().split())
board = [list(map(int,input())) for _ in range(N)]


def calculating(length):
    global N, M, board
    for i in range(N-length):
        for j in range(M-length):
            if board[i][j] == board[i][j+length] and board[i][j] == board[i+length][j] and board[i][j] == board[i+length][j+length]:
                return (length+1)**2
            else:
                pass
    
    else: 
        length -= 1 
        if length == 0:
            return 1
        else: 
            return calculating(length)




if N == 1 or M == 1:
    print(1)
else:
    print(calculating(min(M,N)-1))



