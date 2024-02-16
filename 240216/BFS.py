'''
V개의 정점 7
E개의 간선 8
E개의 간선정보
'''
def bfs(S, N): # S 시작점, V 개의 노드
    q = []
    q.append(S)
    visited = [0] * (N+1)
    # 시작점 1로 표시
    visited[S] = 1
    # q 가 비워질 때까지
    while q:
        t = q.pop(0)
        # t에서 할 일
        # 1. 프린트
        print(t)
        # 2. t에 인접인 점 i에 대해
        for i in adj[t]:
            if visited[i]==0:
                q.append(i)
                visited[i] = 1 + visited[t]

            
V, E = map(int, input().split())
info = list(map(int, input().split()))
# 인접 리스트
adj = [[] for _ in range(V+1)]

for i in range(E):
    n1, n2 = info[i*2], info[i*2+1]
    # 방향 없음
    adj[n1].append(n2)
    adj[n2].append(n1)
bfs(1, V)
print(adj)