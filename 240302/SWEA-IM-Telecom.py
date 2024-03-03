'''
9
XXXXXXXXX
XXXHXXXXX
XXHAHXXHX
XXHHXXXXX
XXXXXXXXX
XXAHHXXXX
XXHXXHAHX
XXAHXXHXX
XXHXHXXXX

3
XXX
XAX
XXX
'''
di = [0,1,0,-1]
dj = [1,0,-1,0]
def A(ai, aj):
    for k in range(4):
        ni = ai + di[k]
        nj = aj + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            Map[ni][nj] = 'A'
def B(bi, bj):
    for k in range(4):
        for t in range(1,3):
            ni = bi + di[k] * t
            nj = bj + dj[k] * t
            if 0 <= ni < N and 0 <= nj < N:
                Map[ni][nj] = 'B'
def C(ci, cj):
    for k in range(4):
        for t in range(1,4):
            ni = ci + di[k] * t
            nj = cj + dj[k] * t
            if 0 <= ni < N and 0 <= nj < N:
                Map[ni][nj] = 'C'
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Map = [list(input())for _ in range(N)]
    AList = []
    BList = []
    CList = []
    for i in range(N):
        for j in range(N):
            if Map[i][j] == 'A':
                AList.append((i,j))
            if Map[i][j] == 'B':
                BList.append((i,j))
            if Map[i][j] == 'C':
                CList.append((i,j))

    for each in AList:
        ai, aj = each
        A(ai, aj)
    for each in BList:
        bi, bj = each
        B(bi, bj)
    for each in CList:
        ci, cj = each
        C(ci, cj)

    cnt = 0
    for p in range(N):
        for q in range(N):
            if Map[p][q] == 'H':
                cnt += 1
    print(f'#{tc} {cnt}')