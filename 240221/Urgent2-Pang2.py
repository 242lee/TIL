T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    Pang = [list(map(int, input().split())) for _ in range(N)]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    maxresult = 0 
    for i in range(N):
        for j in range(M):
            result = Pang[i][j]
            for r in range(1, Pang[i][j]+1):
                for k in range(4):
                    ni = i + di[k] * r
                    nj = j + dj[k] * r
                    if 0 <= ni < N and 0 <= nj < M:
                        result += Pang[ni][nj]
            if maxresult < result:
                maxresult = result
    print(f'#{tc} {maxresult}')
                