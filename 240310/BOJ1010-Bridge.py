'''
N <= M
'''
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    cnt = 0
    arr = [[0] * (M+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            if i == 1:
                arr[i][j] = j
                continue
            if i == j:
                arr[i][j] = 1
            else:
                if j > i:
                    arr[i][j] = arr[i][j-1] + arr[i-1][j-1]
    print(arr[N][M])