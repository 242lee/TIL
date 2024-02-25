def bfs(S,G):
    q = [S]
    visited[S] = 1
    while q:
        t = q.pop(0)
        for next in adj[t]:
            if visited[next] == 0:
                q.append(next)
                visited[next] = visited[t] + 1
            if next == G:
                visited[next] = visited[t] + 1
                return visited[G] - 1
    # 연결된 노드가 없으면 0을 반환
    return 0
T = int(input())
for tc in range(1, T+1):          
    V, E = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for i in range(E):
        n1, n2 = info[i][0], info[i][1]
        adj[n1].append(n2)
        adj[n2].append(n1)
    print(f'#{tc} {bfs(S,G)}')