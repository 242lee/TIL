'''
2
1 2
3 4
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]

    min_di = 100 ** 3
    for cline in range(1, N):
        for rline in range(1, N):
            # 구간별 합
            area = [0,0,0,0]
            for a1 in range(0,cline):
                for a2 in range(0,rline):
                    area[0] += arr[a1][a2]
            for b1 in range(cline,N):
                for b2 in range(0,rline):
                    area[1] += arr[b1][b2]
            for c1 in range(0,cline):
                for c2 in range(rline,N):
                    area[2] += arr[c1][c2]
            for d1 in range(cline,N):
                for d2 in range(rline,N):
                    area[3] += arr[d1][d2]
            # print(area)
            di = max(area) - min(area)
            if min_di > di:
                min_di = di
    print(f'#{tc} {min_di}')