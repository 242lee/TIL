from collections import deque

for testcase in range(1, 11):
    N = int(input())
    origin = list(map(int, input().split()))

    dq = deque()
    for each in origin:
        dq.append(each)

    minusnum = 1

    while True:
        end = dq.popleft()
        end -= minusnum
        if end <= 0:
            end = 0
            dq.append(end)
            break
        else:
            dq.append(end)

        if minusnum == 5:
            minusnum = 1
        else:
            minusnum += 1

    password = []
    for i in range(len(dq)):
        password.append(dq[i])

    print(f'#{testcase}', *password)
