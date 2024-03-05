'''
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front
'''
N = int(input())
lst = []
for _ in range(N):
    lst.append(input().split())
# print(lst)
    
q = []
for each in lst:
    if len(each) == 2:
        do, num = each
    else:
        do = str(each[0])
    # print(do)

    if do == 'push':
        q.append(num)
    elif do == 'pop':
        if q:
            print(q.pop(0))
        else:
            print(-1)
    elif do == 'size':
        print(len(q))
    elif do == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif do == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif do == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)