T = int(input())

di = [0,1,0,-1]
dj = [1,0,-1,0]

for testcase in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    maxcnt = 0
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]
            
            for r in range(1, arr[i][j]+1):
                
                for k in range(4):
                    ni = i + di[k]*r
                    nj = j + dj[k]*r
            
                    if 0<= ni < N and 0<= nj < M:
                        cnt += arr[ni][nj]

            if maxcnt < cnt:
                maxcnt = cnt

    print(f'#{testcase} {maxcnt}')