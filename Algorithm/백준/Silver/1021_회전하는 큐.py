cnt = 0

length, num = map(int, input().split())
lst = list(range(1,length+1))
answer_list = list(map(int,input().split()))

cnt = 0
while answer_list:
    answer = answer_list.pop(0)
    idx = lst.index(answer)
    if idx <= int(len(lst)/2):
        while answer != lst[0]:
            x = lst.pop(0)
            lst.append(x)
            cnt += 1
        
    elif idx > int(len(lst)/2):
        while answer != lst[0]:
            x = lst.pop()
            lst.insert(0,x)
            cnt += 1
        
    lst.remove(answer)

print(cnt)

