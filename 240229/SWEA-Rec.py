T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Board = [list(map(int, input().split()))for _ in range(N)]

    maxr = 0
    maxc = 0
    for i in range(N):
        for j in range(N):
            if Board[i][j] == 1:
                r = 0
                for p in range(N-i):
                    if i + p <= N and Board[i+p][j] == 1:
                    #    print(i+p, j)
                        r += 1
                    if i + p == 0:
                        r =0
                if maxr < r:
                    maxr = r
                c = 0
                for q in range(N-j):
                    if j + q <= N and Board[i][j+q] == 1:
                    #    print(i, j+q)
                        c += 1
                    if j + q == 0:
                        c =0
                if maxc < c:
                    maxc = c
    area = maxr * maxc
    print(f'#{tc} {area}')