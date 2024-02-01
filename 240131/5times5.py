N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

total = 0
for i in range(N):        #25개 요소는 arr[i][j]
    for j in range(N):
        #그 요소와 이웃(상하좌우)한 요소 arr[ni][nj]
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N:
                #차의 절댓값 구하고 총합
                total += abs(arr[ni][nj] - arr[i][j])

#----------------------------------------------------

di = [0,1,0,-1]
dj = [1,0,-1,0]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

total = 0
for i in range(N):        #25개 요소는 arr[i][j]
    for j in range(N):       
        for k in range(4):
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N:
                #차의 절댓값 구하고 총합
                total += abs(arr[ni][nj] - arr[i][j])

