# 8방향
di = [0,1,1,1,0,-1,-1,-1]
dj = [1,1,0,-1,-1,-1,0,1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Board = [[0]*(N+1) for _ in range(N+1)]
    # 중앙좌표
    m = N //2
    Board[m][m] = Board[m+1][m+1] = 2 #백
    Board[m][m+1] = Board[m+1][m] = 1 #흑

    for _ in range(M):
        i, j, d = map(int, input().split())
        Board[i][j] = d
        for k in range(8):
            tobe = []
            for r in range(1, N):
                ni = i + di[k] * r
                nj = j + dj[k] * r
                if 1 <= ni <= N and 1 <= nj <= N:
                    if Board[ni][nj] == 0:
                        break
                    elif Board[ni][nj] == d:
                        while tobe:
                            ti, tj = tobe.pop()
                            Board[ti][tj] = d
                        break
                    else:
                        tobe.append((ni, nj))
                else:
                    break


    blackcnt = whitecnt = 0
    for lst in Board:
        whitecnt += lst.count(2)
        blackcnt += lst.count(1)

    print(f'#{tc} {blackcnt} {whitecnt}')
 