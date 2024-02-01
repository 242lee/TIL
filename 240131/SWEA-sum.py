# N = int(input())
# arr = [[0]*5 for _ in range(5)]
T = int(input())

for testcase in range(1, T+1):

    N = 100
    arr = [[4,4,3,2,1], [2,2,1,6,5], [3,5,4,6,7], [4,2,5,9,7], [8,1,9,5,6]]

    sumList = []

    #좌에서우 방향 sum
    for k in range(N):
        sum = 0
        for down in range(N):
            for side in range(N):
                if down == k :
                    sum += arr[k][side]
        sumList.append(sum)

    #위에서 아래 방향 sum
    for k in range(N):
        sum = 0
        for down in range(N):
            for side in range(N):
                if side == k :
                    sum += arr[down][k]
        sumList.append(sum)

    # 우하향대각선 방향
    sum = 0
    for side in range(N):
        for down in range(N):
            if side == down:
                sum += arr[side][down]
    sumList.append(sum)

    #좌하향대각선 방향
    sum = 0
    for side in range(N):
        for down in range(N):
            if side + down == (N-1):
                sum += arr[side][down]
    sumList.append(sum)

    print(max(sumList)) 