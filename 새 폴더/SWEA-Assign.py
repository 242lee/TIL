def dfs(i,result):
    global maxsum
    if i == N:
        if maxsum <= result:
            maxsum = result
            return
    if result < maxsum:
        return
    for j in range(N):
        if visited[j] == 0 and poss[i][j]:
            visited[j] = 1
            dfs(i+1, result*poss[i][j]/100)
            visited[j] = 0
                            
T = int(input())
for tc in range(1, T+1):            
    N = int(input())
    poss = [list(map(int,input().split())) for _ in range(N)]

    visited = [0] * N
    maxsum = 0
    dfs(0,1)
    maxsum = maxsum * 100
    print(f"#{tc} {round(maxsum,6):.6f}")