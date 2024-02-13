T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    recArr = [list(map(int, input().split())) for _ in range(N)]
    maxcnt = 0
    for i in range(N):
        for j in range(N):
            if recArr[i][j] == 1:
                ni = i
                nj = j
                sidelen = 0
                updownlen = 0
                while 0 <= ni < N and recArr[ni][j] != 0:
                    sidelen += 1
                    ni += 1
                while 0 <= nj < N and recArr[i][nj] != 0:
                    updownlen += 1
                    nj += 1
                cnt = sidelen * updownlen
                if maxcnt < cnt:
                    maxcnt = cnt
    print(f'#{testcase} {maxcnt}')