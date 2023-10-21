king, stone, rep = input().split()
cordinate = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6,'G':7,'H':8}
king_x = cordinate[king[0]]; king_y = int(king[1])
stone_x = cordinate[stone[0]]; stone_y = int(stone[1])
rep = int(rep)

def move(i,j,king_x, king_y, stone_x, stone_y):
    tmp_king_x, tmp_king_y, tmp_stone_x, tmp_stone_y = king_x,king_y,stone_x,stone_y
    if (tmp_king_x + i) < 1 or (tmp_king_x + i) > 8 or (tmp_king_y +j ) < 1 or (tmp_king_y + j) > 8:
        tmp_king_x = king_x
        tmp_king_y = king_y
        tmp_stone_x = stone_x
        tmp_stone_y = stone_y
    else:
        tmp_king_x = king_x + i
        tmp_king_y = king_y + j
        if tmp_king_x == stone_x and tmp_king_y == stone_y:
            if (tmp_stone_x + i) < 1 or (tmp_stone_x + i) > 8 or (tmp_stone_y +j ) < 1 or (tmp_stone_y + j) > 8:
                tmp_king_x = king_x
                tmp_king_y = king_y
                tmp_stone_x = stone_x
                tmp_stone_y = stone_y
            else:
                tmp_stone_x = stone_x + i
                tmp_stone_y = stone_y + j
        else:
            tmp_stone_x = stone_x
            tmp_stone_y = stone_y
    return tmp_king_x, tmp_king_y, tmp_stone_x, tmp_stone_y


for i in range(rep):
    input_move = input()
    if input_move == 'R':
        king_x, king_y, stone_x, stone_y = move(1,0,king_x, king_y, stone_x, stone_y)
    elif input_move == 'L':
        king_x, king_y, stone_x, stone_y = move(-1,0,king_x, king_y, stone_x, stone_y) 
    elif input_move == 'B':
        king_x, king_y, stone_x, stone_y = move(0,-1,king_x, king_y, stone_x, stone_y) 
    elif input_move == 'T':
        king_x, king_y, stone_x, stone_y = move(0,1,king_x, king_y, stone_x, stone_y) 
    elif input_move == 'RT':
        king_x, king_y, stone_x, stone_y = move(1,1,king_x, king_y, stone_x, stone_y) 
    elif input_move == 'LT':
        king_x, king_y, stone_x, stone_y = move(-1,1,king_x, king_y, stone_x, stone_y) 
    elif input_move == 'RB':
        king_x, king_y, stone_x, stone_y = move(1,-1,king_x, king_y, stone_x, stone_y) 
    elif input_move == 'LB':
        king_x, king_y, stone_x, stone_y = move(-1,-1,king_x, king_y, stone_x, stone_y) 

print(str(list(cordinate.keys())[(king_x)-1]) + str(king_y))
print(str(list(cordinate.keys())[(stone_x)-1]) + str(stone_y))
