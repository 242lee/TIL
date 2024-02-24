def c(i,N):
    global minv
    if i == N:
        subsetsum = 0
        for j in range(N):
            subsetsum += arr[j][P[j]]
        if minv > subsetsum:
            minv = subsetsum
    else:
        for j in range(N):
            P[i], P[j] = P[j], P[i]
            c(i+1, N)
            P[i], P[j] = P[j], P[i]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = [i for i in range(N)]
    minv= 1000
    c(0,N)
    print(f'#{tc} {minv}')
