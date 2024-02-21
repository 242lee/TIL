T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Pang = [list(map(int, input().split())) for _ in range(N)]
    maxresult = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for i in range(N):
        for j in range(N):
            result = Pang[i][j]
            for r in range(1, N):
                for k in range(4):
                    ni = i + di[k] * r
                    nj = j + dj[k] * r
                    if 0 <= ni < N and 0 <= nj < N:
                        result += Pang[ni][nj]
            
            if result > maxresult:
                maxresult = result
    print(f'#{tc} {maxresult}')