def dfs(i):
    global result
    if i == N:
        result += 1
        return
    for j in range(0,N):
        if v1[j] == v2[i+j] == v3[i-j] == 0:
            v1[j] = v2[i+j] = v3[i-j] = 1 
            dfs(i+1)
            v1[j] = v2[i+j] = v3[i-j] = 0
            
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = 0
    v1 = [0] * (N+1)
    v2 = [0] * (2*N) # 좌하향 대각석
    v3 = [0] * (2*N) # 우하향 대각선
    dfs(0)
    print(f'#{tc} {result}')