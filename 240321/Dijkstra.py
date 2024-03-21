'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''
def dijkstra(start):
        priority = []
        # cost, start 번호를 한 번에 저장
        heappush(priority, (0, start))
        
        distance[start] = 0
        
        while priority:
            # 최단 거리 노드에 대한 정보
            cost, now = heappop(priority)
            # pq의 특성 때문에 더 긴거리가 미리 저장되어 있음
            # now가 이미 더 짧은 거리로 온 적이 있다면 pass
            if distance[now] < cost :
                continue
            # now에서 갈 수 있는 = 인접들을 또 확인
            for next in graph[now]:
                nextcost = next[0]
                nextnode = next[1]
                # 누적 거리 계산
                newcost = cost + nextcost
                # 이미 짧은 거리로 간 경우 pass
                if newcost >= distance[nextnode]:
                    continue
                # 누적 거리를 최단 거리로 갱신
                distance[nextnode] = newcost
                # newx_mode의 인접 노드들을 priority에 추가
                heappush(priority, (newcost, nextnode))

from heapq import heappush, heappop
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    start = 0
    # 인접 리스트
    graph = [[] for _ in range(E)]
    # 누적 거리 저장할 변수
    distance = [1e9] * (V+1)

    # 간선 정보 저장
    for _ in range(E):
        s, e, c = map(int, input().split())
        # 시작점의 cost, node 번호를 한 번에 저장
        graph[s].append([c, e])
        
    dijkstra(0)
    print(distance[-1])

# def daijkstra(start):
#     priority = []
#     # cost와 노드 번호를 한 번에 저장
#     heappush(priority, (0,start))
#     distance[start] = 0
    
#     while priority:
#         # 최단 거리 노드에 대한 정보
#         cost, now = heappop(priority)
#         for next in graph[now]:
#             nextcost = next[0]
#             nextnode = next[1]
            
#             newcost = cost + nextcost  # 누적합
#             # 이미 더 짧은 거리로 간 경우 pass
#             if nextcost >= distance[nextnode]:
#                 continue
#             distance[nextnode] = newcost
#             heappush(priority, (nextcost, nextnode))
            
# inf = int(1e9)

# V, E = map(int, input().split())
# start = 0 # 시작 노드 번호

# # 인접 리스트
# graph = [[] for _ in range(V)]

# # 누적 거리를 저장할 변수
# distance = [inf] * V

# # 간선 정보 저장
# for _ in range(E):
#     s, e, c = map(int, input().split())
#     # graph[3] = [[4, 34]] 3->4 에 34 비용이 듦
#     graph[s].append([c, e])

# daijkstra(0)
# print(distance)

'''
def dijkstra(start):
    Q = []
    heapriority.heappush(Q,(0,start)) # 우선 순위 큐 push
    dist[start] = 0
    while True:
        if Q == []:
            break
        d, current = heapriority.heappop(Q) # 우선 순위 큐 pop
        if dist[current] < d:
            continue # 이미 가공된 것이라면 (d보다 작을 테니) 무시
        for i in matrix[current]:
            new_cost = d+i[1]
            # 거쳐가는 비용 계산 과정
            if new_cost < dist[i[0]]:
                # 거쳐가는 것이 더 저렴하다면
                dist[i[0]] = new_cost
                heapriority.heappush(Q,(new_cost, i[0]))
'''