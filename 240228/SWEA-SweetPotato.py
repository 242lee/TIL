

# cnt = 0
# for i in range(-1, N+1):
#     if sweetpotato[i] < sweetpotato[i+1]:
#         cnt += sweetpotato[i+1]
#     else:
#         cnt = sweetpotato[i+1]
#     print(cnt)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sweetpotato = [0] + list(map(int, input().split())) + [0]
    maxcnt = 0
    cnt = 0
    index = 0
    over2 = 0
    tmpsum = 0
    maxsum = 0
    for i in range(1,N+1):
        if sweetpotato[i-1] < sweetpotato[i]:
            cnt += 1
        else:
            cnt = 1
        if maxcnt < cnt:
            maxcnt = cnt
            index = i
        
        if cnt == 2: # 긴 줄기 개수 구하기
            over2 += 1
        if cnt == maxcnt:
            if 0<= i-maxcnt <= N:
                print(sweetpotato[i-maxcnt+1:i+1])
                tmpsum = sum(sweetpotato[i-maxcnt+1:i+1])
                print(tmpsum)
            if maxsum < tmpsum:
                maxsum = tmpsum
    print(f'#{tc} {over2} {maxsum}')

    # # 가장 긴 줄기에 달린 고구마 개수
    # tmpsum = 0
    # maxsum = 0
    # for j in range(index-maxcnt+1, index+1):
    #     tmpsum += sweetpotato[j]
    #     if maxsum < tmpsum:
    #         maxsum = tmpsum
    # # print(maxsum)
    # print(f'#{tc} {over2} {maxsum}')

