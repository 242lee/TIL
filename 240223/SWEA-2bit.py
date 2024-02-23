T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # print(bin(M))
    
    cnt = 0
    for i in range((len(bin(M))-N),len(bin(M))):
        if bin(M)[i] == '1':
            cnt += 1
    if cnt == N:
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')