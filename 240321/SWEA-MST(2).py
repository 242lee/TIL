'''
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
-> 13
'''
# 최소 신장 트리 - prim
from heapq import heappush, heappop

def prim(start):
    priority = []
    MST = [0] * (V+1)
    costsum = 0
    
    heappush(priority, (0, start))
    while priority:
        cost, now = heappop(priority)
        
        if MST[now]:  
            continue
        MST[now] = 1 
        costsum += cost
        
        for next in range(V+1):
            if graph[now][next] == 0 or MST[next]:
                continue
            heappush(priority, (graph[now][next], next))
    return costsum
 
T = int(input())
for tc in range(1, T+1):   
    V, E = map(int, input().split())
    graph = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        s, d, c = map(int, input().split())
        graph[s][d] = c
        graph[d][s] = c 
    result = prim(0)
    print(f'#{tc} {result}')