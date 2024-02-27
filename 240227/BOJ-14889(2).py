def si(k, depth):
    global min_di

    if k == N//2:
        start = 0
        link = 0

        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += S[i][j]
                if not visited[i] and not visited[j]:
                    link += S[i][j]
        
        di = abs(start-link)
        if min_di > di:
            min_di = di
        return
    
    for t in range(k, N):
        if not visited[t]:
            visited[t] = 1
            si(k+1, depth+1)
            visited[t] = 0

N = int(input())
S = [list(map(int,input().split()))for _ in range(N)]
visited = [0] * (N+1)
min_di = 50 ** 3
si(0,0)
print(min_di)