'''
14
push 1
push 2
top
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
top
'''
N = int(input())
lst = []
for _ in range(N):
    lst.append(input().split())
# print(lst)

stack = []
for each in lst:
    if len(each) > 1:
        do, num = each
    else:
        do = str(each[0])
    # print(do)
        
    if do == 'push':
        stack.append(num)
    elif do == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif do == 'size':
        print(len(stack))
    elif do == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif do == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)

