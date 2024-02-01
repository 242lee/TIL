for _ in range(1,10+1):
    testcase = int(input())
    sumList = []
    arr = [list(map(int,input().split())) for _ in range(100)]

    # 좌에서우 방향 sum
    N= 100
    for k in range(N):
        sum = 0
        for side in range(N):
            sum += arr[k][side]
        sumList.append(sum)

    # 위에서아래 방향 sum
    for k in range(N):
        sum = 0
        for down in range(N):
            sum += arr[down][k]
        sumList.append(sum)

    # 우하향대각선 방향
    sum = 0
    for side in range(N):
        for down in range(N):
            if side == down:
                sum += arr[side][down]
    sumList.append(sum)

    # 좌하향대각선 방향
    sum = 0
    for side in range(N):
        for down in range(N):
            if side + down == (N-1):
                sum += arr[side][down]
    sumList.append(sum)

    maxsum = 0
    for num in sumList:
        if maxsum < num:
            maxsum = num

    print(f'#{testcase} {maxsum}') 