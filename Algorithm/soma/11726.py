# def compare(idx, rgb):
# 	global lst
# 	if rgb == 0:
# 		if lst[idx][1]>lst[idx][2]:
# 			min_val = lst[idx][2]
# 			rgb = 2
# 		elif lst[idx][1]<lst[idx][2]:
# 			min_val = lst[idx][1]
# 			rgb = 1
# 		else:
# 			if lst[idx+1][1]<lst[idx+1][2]:
# 				min_val = lst[idx][2]
# 				rgb = 2
# 			else:
# 				min_val = lst[idx][1]
# 				rgb = 1
# 	elif rgb == 1:
# 		if lst[idx][0]>lst[idx][2]:
# 			min_val = lst[idx][2]
# 			rgb = 2
# 		elif lst[idx][0]<lst[idx][2]:
# 			min_val = lst[idx][0]
# 			rgb = 0
# 		else:
# 			if lst[idx+1][0]<lst[idx+1][2]:
# 				min_val = lst[idx][2]
# 				rgb = 2
# 			else:
# 				min_val = lst[idx][2]
# 				rgb = 2
# 	else:
# 		if lst[idx][0]>lst[idx][1]:
# 			min_val = lst[idx][1]
# 			rgb = 1
# 		elif lst[idx][0]<lst[idx][1]:
# 			min_val = lst[idx][0]
# 			rgb = 0
# 		else:
# 			if lst[idx+1][0]<lst[idx+1][1]:
# 				min_val = lst[idx][1]
# 				rgb = 1
# 			else:
# 				min_val = lst[idx][0]
# 				rgb = 0
# 	return min_val, rgb


N = int(input())
lst = []

for _ in range(N):
	lst.append(list(map(int,input().split())))


# cost = min(lst[0])
# rgb = lst[0].index(cost)

# for i in range(1,N):
# 	tmp_cost, rgb = compare(i,rgb)
# 	cost += tmp_cost



# print(cost)
tbl = [[0,0,0] for _ in range(N)]

for i in range(N):
    for j in range(3):
    	tbl[i][j] = min(tbl[i-1][:j]+tbl[i-1][j+1:]) + lst[i][j]
print(min(tbl[N-1]))
