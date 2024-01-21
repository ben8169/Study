def f_1(*kwagrs):
    print(kwagrs, *kwagrs)

a = f_1(12,'abc',3)


print(*[1, 3, 5], sep='\n')



def f_3(**kwargs):
    print(kwargs)
    


f_3(a='a')
f_3(a='a', color='red')


