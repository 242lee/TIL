def complete(s_i, s_j):
    next = [(s_i, s_j)]
    visited[s_i][s_j] = 1
    while next:
        i, j = next.pop(0)
        # 4방향, 범위내, 미방문, tomato[] == 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and tomato[ni][nj] == 0:
                next.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                tomato[ni][nj] = 1


'''
입력 | 1 익은 토마토, 0 익지 않은 토마토, -1 빈칸
출력 | 며칠이 걸리는지, 이미 다 익어있으면 0, 다 익을 수 없으면 -1
'''
M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

cnt = 0

tototo = False
for i in range(N):
    if 0 not in tomato[i]:
        tototo = True
    else:
        tototo = False
        break
startList = []
if tototo == False:
    for k in range(N):
        for j in range(M):
            if tomato[k][j] == 1:
                startList.append((k,j))
for each in startList:
    s_i, s_j = each
    complete(s_i, s_j)
    # print(visited)
flag = False
maxc = 0
if tototo == True:
    print(0)
else:
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 0:
                flag = True
                print(-1)
            if visited[i][j] > maxc:
                maxc = visited[i][j]
    if flag == False:
        print(maxc - 1)