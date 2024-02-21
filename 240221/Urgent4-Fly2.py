di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
dr = [-1, 1, 1, -1]
dc = [1, 1, -1, -1]
 
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Board = [list(map(int, input().split())) for _ in range(N)]
    maxresult = 0
    for i in range(N):
        for j in range(N):
            # + 모양으로 분사할 경우
            result1 = Board[i][j]
            for s in range(1, M):
                for k in range(4):
                    ni = i + di[k] * s
                    nj = j + dj[k] * s
                    if 0 <= ni < N and 0 <= nj < N:
                        result1 += Board[ni][nj]
            if maxresult < result1:
                maxresult = result1
            # x 모양으로 분사할 경우
            result2 = Board[i][j]
            for s in range(1, M):
                for k in range(4):
                    ni = i + dr[k] * s
                    nj = j + dc[k] * s
                    if 0 <= ni < N and 0 <= nj < N:
                        result2 += Board[ni][nj]
            if maxresult < result2:
                maxresult = result2
    print(f'#{tc} {maxresult}')