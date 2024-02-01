T= int(input())

for testcase in range(1, T+1):
    N=int(input())

    arr = [[0]*N for _ in range(N)]
    i, j = 0, 0 #시작 위치
    cnt = 1
    dr = 0

    #우 하 좌 상
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    arr[i][j] = cnt
    
    while cnt <= N*N:
        ni = i + di[dr]
        nj = j + dj[dr]

        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            i, j = ni, nj
            arr[i][j] = cnt
            cnt += 1
        else:
            dr = (dr+1) % 4

    for num in arr:
        print(*num)