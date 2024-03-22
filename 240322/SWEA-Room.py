from collections import deque
 
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
 
 
def bfs(start):
    global total_max_value
    start_i, start_j = start
    q = deque()
    q.append(start)
    max_distance = 1
    v[start_i][start_j] = 1
    while q:
        now_i, now_j = q.popleft()
        for d in range(4):
            next_i, next_j = now_i + di[d], now_j + dj[d]
            new_distance = v[now_i][now_j] + 1
            if 0 <= next_i < N and 0 <= next_j < N and matrix[next_i][next_j] - matrix[now_i][now_j] == 1:
                if v[next_i][next_j] > new_distance:
                    continue
                v[next_i][next_j] = new_distance
                q.append((next_i, next_j))
                if max_distance < new_distance:
                    max_distance = new_distance
    if total_max_value < max_distance:
        total_max_value = max_distance
    return (matrix[start_i][start_j], max_distance)
 
 
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    v = [[0] * N for _ in range(N)]
    matrix = [list(map(int, input().split())) for _ in range(N)]
    total_max_value = -1
    point_dis_li = []
    for i in range(N):
        for j in range(N):
            point_dis_li.append(bfs((i, j)))
    min_val = 10 ** 9
    for val, distance in point_dis_li:
        if distance == total_max_value:
            if min_val > val:
                min_val = val
    print(f'#{tc}',min_val,total_max_value)
