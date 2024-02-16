def bfs(i, j):
    # 시작은 2에서
    q = [[i,j]]
    countarr[i][j] = 1

    while q:
        t = q.pop(0)
        i, j = t[0], t[1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and countarr[ni][nj] == 0:
                if maze[ni][nj] == '0':
                    q.append([ni,nj])
                    countarr[ni][nj] = countarr[i][j] + 1
                    # print(q)
                if maze[ni][nj] == '3':
                    countarr[ni][nj] = countarr[i][j] + 1
                    return countarr[ni][nj] - 2
    return 0

T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    countarr = [[0] * N for _ in range(N)]
    # 방향 전환
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    # 시작점 좌표 찾기
    start_i = 0
    start_j = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                start_i = int(i)
                start_j = int(j)

    print(f'#{testcase} {bfs(start_i, start_j)}')
    # print(countarr)