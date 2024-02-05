Arr = [[2,1,1,2,2],[2,2,1,2,2],[2,2,1,1,2]]
N, M = 3, 5

di = [0,1,0,-1]
dj = [1,0,-1,0]

maxcnt = 0
for i in range(N):
    for j in range(M):
        cnt = Arr[i][j]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0<=ni<N and 0<=nj<M:
                cnt += Arr[ni][nj]

        if maxcnt < cnt:
            maxcnt = cnt
            
print(maxcnt)