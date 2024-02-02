
T = int(input())
for testcase in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N) ] + [[0] * (N+1)]
    N += 1

    asw = 0
    # 가로 방향 개수 구하기
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j]:
                cnt += 1
            else: #arr[i][j] == 0
                if cnt == K:
                    asw += 1
                cnt = 0

    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j]:
                cnt += 1
            else: #arr[i][j] == 0
                if cnt == K:
                    asw += 1
                cnt = 0
    
    print(f'#{testcase} {asw}')