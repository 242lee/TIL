def bfs(i, j):
    q = [[i,j]]
    # 시작점 1로 바꾸기
    countarr[i][j] = 1
    while q: 
        k = q.pop(0)    
        i, j = k[0], k[1]

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < N and countarr[ni][nj] == 0:
                if maze[ni][nj] == '0':
                    q.append([ni,nj])
                    countarr[ni][nj] = countarr[i][j] + 1
                if maze[ni][nj] == '3':
                    countarr[ni][nj] = countarr[i][j] + 1
                    return 1
    return 0

N = 16

for testcase in range(1, 11):
    testcase = int(input())
    maze = [list(input()) for _ in range(N)]
    countarr = [[0] * N for _ in range(N)]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    # print(maze)

    start_i = 0
    start_j = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                start_i = int(i)
                start_j = int(j)
    # print(start_i, start_j)
    print(f'#{testcase} {bfs(start_i, start_j)}')
