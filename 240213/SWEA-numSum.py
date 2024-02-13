T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    numList = list(map(int, input().split()))

    maxnum = -1000000000000
    minnum = 1000000000000
    for i in range(N-1):
        numsum = numList[i] + numList[i+1]

        if maxnum < numsum:
            maxnum = numsum
        if minnum > numsum:
            minnum = numsum

    print(f'#{testcase} {maxnum} {minnum}')