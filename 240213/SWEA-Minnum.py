T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    numList = list(map(int, input().split()))

    minnum = 1000000000000
    index = 0
    for i in range(N):
        if numList[i] < minnum:
            minnum = numList[i]
            index = i+1
    print(f'#{testcase} {index}')