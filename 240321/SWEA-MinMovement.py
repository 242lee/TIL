# 최소이동거리
def dijkstra(start):
        priority = []
        heappush(priority, (0, start))
        
        distance[start] = 0
        
        while priority:
            cost, now = heappop(priority)
            if distance[now] < cost :
                continue
            for next in graph[now]:
                nextcost = next[0]
                nextnode = next[1]
                newcost = cost + nextcost
                if newcost >= distance[nextnode]:
                    continue
                distance[nextnode] = newcost
                heappush(priority, (newcost, nextnode))

from heapq import heappush, heappop
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    start = 0
    graph = [[] for _ in range(E)]
    distance = [1e9] * (V+1)

    for _ in range(E):
        s, e, c = map(int, input().split())
        graph[s].append([c, e])
        
    dijkstra(0)
    print(f'#{tc} {distance[-1]}')