K, N, M = map(int, input().split())
charge = list(map(int, input().split()))

# 충전소 어디있는지 1로 표시
station = [0] * (N+1)
for i in charge:
    station[i] = 1
# 충전소 방문했는지 표시
visited = [0] * (N+1)

# print(station)

# 0번 충전소에서 충전했으니까 버스가 한 번에 갈 수 있는 거리로 시작
bus = K
# 앞으로 한 칸씩 갈 거삼
for now in range(N):
    # 지금 위치에서 바로 다음에 나오는 충전소 번호 저장해두기
    next = 0
    for i in range(now, N):
        if now <= i and station[i] == 1:
            next = i
            break
    
    # 충전소를 지나는데
    if station[now] == 1:
    # 전기가 없으면 충전하고 방문 표시
        if bus == 0:
            bus = K
            visited[now] = 1

    # 전기가 있긴 있어 근데 다음 충전소까지는 못 가
        elif next - now > bus:
            # 그러면 충전을 해
            bus = K
            visited[now] = 1

    # print(now, next, bus)
            
    # 버스는 한 칸 움직일 때마다 에너지 -1
    bus -= 1

print(visited)
'''
3 10 5
1 3 5 7 9
'''