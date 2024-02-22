T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(N)]
    maxcnt = 0
    for i in range(N):
        cnt = 1
        for j in range(M-1):
            if ground[i][j] == 1 and ground[i][j+1] == 1:
                cnt += 1
        if maxcnt < cnt:
            maxcnt = cnt

    tmpresult = []
    for c in range(M):
        tmp = []
        for r in range(N):
            tmp.append(ground[r][c])
        # print(tmp)
        tmpresult.append(tmp)

    for p in range(M):
        cnt = 1
        for q in range(N-1):
            if tmpresult[p][q] == 1 and tmpresult[p][q+1] == 1:
                cnt += 1
        if maxcnt < cnt:
            maxcnt = cnt
    print(f'#{tc} {maxcnt}')
            