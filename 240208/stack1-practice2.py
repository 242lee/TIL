def dfs(i):
    visited[i] = 1 #방문표시
    print(i) 
    # i에 인접하고 방문 안 한 w가 있으면
    for w in adjl[i]:
        if visited[w] == 0:
            dfs(w)


V, E = map(int, input().split())
arr = list(map(int, input().split()))

adjl = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)
print(adjl)
visited = [0] * (V+1)
dfs(1)