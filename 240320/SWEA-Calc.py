def bfs(N, M):
    # 큐 생성 + 시작점 인큐
    q = [N]
    cntarr[N] = 1
    while q:
        t = q.pop(0)    # 디큐
        if t == M:
            return cntarr[t] -1
        # t에 인접한 w를 방문한 적이 없으면 
        if t - 10 > 0 and cntarr[t - 10] == 0:
            q. append(t - 10)
            cntarr[t - 10] = cntarr[t] + 1
        if t - 1 > 0 and cntarr[t - 1] == 0:
            q. append(t - 1)
            cntarr[t - 1] = cntarr[t] + 1
        if t + 1 > 0 and cntarr[t + 1] == 0:
            q. append(t + 1)
            cntarr[t + 1] = cntarr[t] + 1
        if t * 2 > 0 and cntarr[t * 2] == 0:
            q. append(t * 2)
            cntarr[t * 2] = cntarr[t] + 1
    return -1    
T = int(input()) 
for tc in range(1, T+1):   
    N, M = map(int, input().split())
    cntarr = [0] * 1000001
    print(f'#{tc} {bfs(N, M)}')
