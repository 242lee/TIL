'''
1. 자료구조
- 그래프 (인접행렬, 인접리스트)
2. 알고리즘
-BFS
    N번만에 해당 노드를 탐색했다 (level, depth)
    마지막level에서 숫자가 가장 큰 노드
24 2
100 17 39 22 100 8 100 7 7 100 2 7 2 15 15 4 6 2 11 6 4 10 4 2
-> 17
'''

def bfs(start):
    q = [start]
    visited[start] = 1
    maxnum = start
    maxdepth = 1
    while q:
        now = q.pop(0)
        # 갈 수 있는 곳들 q에 더하기
        for next in graph[now]:
            if visited[next]:
                continue
            # depth가 깊어졌다면 maxnum 초기화
            # dpeth는 같은데 maxnum이 커졌다면 초기화
            visited[next] = visited[now] + 1
            if maxdepth < visited[next] or (maxdepth == visited[next] and maxnum < next):
                maxdepth = visited[next]
                maxnum = next
            q.append(next)       
    return maxnum

for tc in range(1, 11):
    N, start = map(int, input().split())
    inputgraph = list(map(int, input().split()))
    # 인접 리스트
    graph = [[] for _ in range(101)]
    for i in range(0, N, 2):
        s = inputgraph[i]
        e = inputgraph[i + 1]
        graph[s].append(e)
    visited = [0] * (101)   
    print(f'#{tc} {bfs(start)}')
