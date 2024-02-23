K, N, M = map(int, input().split())
charge = list(map(int, input().split()))

station = [0] * (N+1)
visited = [0] * (N+1)
for i in charge:
    station[i] = 1

print(station)


bus = K
for now in range(N):
    next = 0
    for i in range(now, N):
        if now <= i and station[i] == 1:
            next = i
            break

    if station[now] == 1:
    # 전기가 없고 충전소 만나면
        if bus == 0:
            bus = 3
            visited[now] = 1

    # 전기가 있는데 충전소를 만난 경우
        elif next - now > bus:
        # 다음 충전소까지 못 갈 때
            bus = 3
            visited[now] = 1

    print(now, next, bus)
    bus -= 1

print(visited)
'''
3 10 5
1 3 5 7 9
'''