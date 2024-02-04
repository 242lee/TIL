Arr = [[0,0,1,1,1],[1,1,1,1,0],[0,0,1,0,0],[0,1,1,1,1],[1,1,1,0,1]]
N = 5
K = 3

asw = 0
# 가로 방향 개수 구하기
for i in range(N):
    cnt = 0
    for j in range(N):
        if Arr[i][j] == 1:
            cnt += 1
        else: #Arr[i][j] == 0
            if cnt == K:
                asw += 1
            cnt = 0

for j in range(N):
    cnt = 0
    for i in range(N):
        if Arr[i][j] == 1:
            cnt += 1
        else: #arr[i][j] == 0
            if cnt == K:
                asw += 1
            cnt = 0
print(cnt)