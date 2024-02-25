di = [0,1,0,-1]
dj = [1,0,-1,0]
def bfs(i, j):
    q = [[i,j]]
    countarr[i][j] = 0
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
                if  maze[ni][nj] == '3':
                    countarr[ni][nj] = countarr[i][j] + 1
                    return countarr[ni][nj] - 1
    return 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(input())for _ in range(N)]
    countarr = [[0] * N for _ in range(N)]
    # 시작점 찾기
    i = 0
    j = 0
    for r in range(N):
        for c in range(N):
            if maze[r][c] == '2':
                i = r
                j = c
    print(f'#{tc} {bfs(i, j)}')