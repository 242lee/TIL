# N = int(input())
# Board = [list(map(int, input().split())) for _ in range(N)]
# result = []
# P = [i for i in range(N)]

# def arrmin(i, N):
#     if i == N:
#         for k in range(N):
#             print(P[k], end = ' ')
#             # print(Board[k][P[k]], end = ' ')
#         print()
#     else:
#         for k in range(1,N):
#             P[i], P[k] = P[k], P[i]
#             arrmin(i+1, N)
#             P[i], P[k] = P[k], P[i]
# arrmin(0, N)

# def arrmin(i, j, depth, arrsum):
#     global minsum
#     if depth == (N-1) * 2:
#         if minsum > arrsum:
#             minsum = arrsum
#         return
#     else:
#         if 0 <= i < N and 0 <= j+1 < N:
#             arrmin(i, j+1, depth+1, arrsum + Board[i][j+1])
#         elif 0 <= i+1 < N and 0 <= j < N:
#             arrmin(i+1, j, depth+1, arrsum + Board[i+1][j])

def arrmin(i, j, r, arrsum):
    di = [0,1]
    dj = [1,0]
    global minsum
    if r == (N-1) * 2:
        if minsum > arrsum:
            minsum = arrsum
        return

    for k in range(2):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            arrmin(ni,nj,r+1,arrsum+Board[ni][nj])
            
T = int(input())
for tc in range(1, T+1):
        
    N = int(input())
    Board = [list(map(int, input().split())) for _ in range(N)]
    minsum = N ** 3
    arrmin(0,0,0,Board[0][0])
    print(f'#{tc} {minsum}')