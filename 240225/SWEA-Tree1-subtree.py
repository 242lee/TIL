'''
5 1
2 1 2 5 1 6 5 3 6 4 
'''
def nodecnt(N):
    global cnt
    if N:
        nodecnt(c1[N])
        nodecnt(c2[N])
        cnt += 1
T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    # N을 루트로 하는 서브트리 전체 print 해보기
    info = list(map(int, input().split()))
    c1 = [0] * (E+2)
    c2 = [0] * (E+2)
    cnt = 0
    for i in range(E):
        if c1[info[i*2]] == 0:
            c1[info[i*2]] = info[i*2+1]
        else:
            c2[info[i*2]] = info[i*2+1]
    nodecnt(N)
    print(f'#{tc} {cnt}')