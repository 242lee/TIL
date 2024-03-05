from collections import deque

N = int(input())
lst = []
for _ in range(N):
    lst.append(input().split())
# print(lst)

dq = deque([])
for each in lst:
    if len(each) > 1:
        do, num = each
    else:
        do = str(each[0])
    # print(do)

    if do == 'push_front':
        dq.appendleft(num)
    elif do ==  'push_back':
        dq.append(num)
    elif do == 'pop_front':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif do == 'pop_back':
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif do == 'size':
        print(len(dq))
    elif do == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif do == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif do == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)