#6
def square_matrix(M,n):
    if n>=len(M): return n**2
    if M[n-1][n-1] == 1: 
        for i in range(n+1):
            for j in range(n+1):
                print(i,j)
                if M[n-j][n-i]==0:
                    break
        else:
          square_matrix(M,n+1)

    return n**2
M = [[1,1],[1,1]]

square_matrix(M,1)

