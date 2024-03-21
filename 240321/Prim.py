'''
노드 수, 간선 수
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
# import sys
# input = sys.stdin.readline
from heapq import heappush, heappop

def prim(start):
    priority = []
    MST = [0] * V
    costsum = 0
    
    # 시작점 추가
    # Prim | 가중치가 낮으면 먼저 나와야 함
    #    관리해야 할 데이터) 가중치, 노드 번호
    #    방법 1. 클래스 2. 튜플 (가중치, 시작점)
    heappush(priority, (0, start))
    while priority:
        cost, now = heappop(priority)
        
        if MST[now]:    # 방문했다면 계속 진행
            continue
        MST[now] = 1    # 방문처리
        
        costsum += cost # 비용더하기
        
        # 갈 수 있는 노드들을 보면서
        for next in range(V):
            # 갈 수 없거나 이미 방문했다면
            if graph[now][next] == 0 or MST[next]:
                continue
            heappush(priority, (graph[now][next], next))
    print(costsum)
    
V, E = map(int, input().split())
graph = [[0] * V for _ in range(V)]
for _ in range(E):
    s, d, c = map(int, input().split())
    # 3 -> 4로 가는데 34만큼 비용이 든다.
    # graph[3][4] = 34
    graph[s][d] = c
    graph[d][s] = c # 무방향이므로 양쪽 다

prim(0)