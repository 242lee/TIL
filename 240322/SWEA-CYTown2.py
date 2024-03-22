from collections import deque
 
def bfs(start):
    q = deque([start])
    visited[start] = 1
     
    while q:
        now = q.popleft()
        for next in relation[now]:
            if visited[next] == 0:
                q.append(next)
                visited[next] = 1
 
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    relation = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    cnt = 0
    for _ in range(M):
        s, e = map(int, input().split())
        relation[s].append(e)
        relation[e].append(s)
         
    for i in range(1, N+1):
        if visited[i] == 0:
            bfs(i)
            cnt += 1
             
    print(f'#{tc} {cnt}')