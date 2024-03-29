from collections import deque
# 최소비용 구하기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    H = [list(map(int, input().split()))for _ in range(N)]
    
    visited = [[int(1e9)] * N for _ in range(N)]
    visited[0][0] = 0
    
    # 도착 비용이 갱신되는 칸을 인큐(중복될 수 있음)
    q = deque()     # 큐 생성, 비용이 갱신된 칸에 인접한 인큐
    q.append((0,0)) 
    while q:
        i, j = q.popleft()
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                diff = H[ni][nj] - H[i][j] if H[ni][nj] >= H[i][j] else 0
                if visited[ni][nj] > visited[i][j] + diff + 1: # 누적된 비용(기존)보다 연료를 덜 소비하고 도착하면
                    q. append((ni, nj))
                    visited[ni][nj] = visited[i][j] + diff + 1
                    
    print(f'#{tc} {visited[N-1][N-1]}')