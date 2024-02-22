T = int(input())
for tc in range(1,  T+1):
    N = int(input())
    size = list(map(int, input().split()))

    maxcnt = 0
    cnt = 1
    for i in range(N-1):
        if size[i] < size[i+1]:
            cnt += 1
        else:
            cnt = 1
        if maxcnt < cnt:
            maxcnt = cnt
            
    print(f'#{tc} {maxcnt}')