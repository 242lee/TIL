from collections import deque
for _ in range(1, 11):
    testcase = int(input())
    password = list(map(int, input().split()))

    dq= deque()
    for i in range(8):
        dq.append(password[i])
    
    minus = 1
    while True:
        next = dq.popleft() - minus
        dq.append(next)
        
        if dq.pop() <= 0:
            dq.append(0)
            break
        else:
            dq.append(next)

        if minus == 5:
            minus = 1
        else: 
            minus += 1

    print(f'#{testcase}', *dq)
    
