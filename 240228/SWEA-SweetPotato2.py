T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sweetpotato = [0] + list(map(int, input().split())) + [0]
    maxcnt, cnt = 0, 0
    over2 = 0
    for i in range(1,N+1):
        if sweetpotato[i-1] < sweetpotato[i]:
            cnt += 1
        else:
            cnt = 1
        if maxcnt < cnt:
            maxcnt = cnt
            # index = i
        if cnt == 2: # 긴 줄기 개수 구하기
            over2 += 1
    # print(maxcnt, cnt)

    k = 0
    tmp = 0
    tmpsum, maxsum = 0, 0
    if maxcnt >= 2:
        while k < N:
            for k in range(1,N+1):
                if sweetpotato[k-1] < sweetpotato[k]:
                    tmp += 1
                    # print(tmp)
                else:
                    tmp = 1
                if tmp == maxcnt:
                    tmpsum = sum(sweetpotato[k-maxcnt+1:k+1])
                    k += maxcnt
                else:
                    k += 1
                if maxsum < tmpsum:
                    maxsum = tmpsum
    # print(maxsum)
    print(f'#{tc} {over2} {maxsum}')