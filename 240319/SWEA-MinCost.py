def dfs(i, cost):
    global mincost
    if i == N:
        if cost < mincost:
            mincost = cost
            return
    if cost > mincost:
        return
    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            dfs(i+1, cost + costTable[i][j])
            visited[j] = 0

T = int(input())
for tc in range(1, T+1):        
    N = int(input())
    costTable = [list(map(int, input().split()))for _ in range(N)]

    visited = [0] * N
    mincost = 10 * 50 * 50
    dfs(0, 0)
    print(f'#{tc} {mincost}')