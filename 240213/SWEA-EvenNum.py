T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    numList = list(map(int, input().split()))
    cnt = 0
    for num in numList:
        if num % 2 == 0:
            cnt += 1
        else:
            cnt += 0
    print(f'#{testcase} {cnt}')