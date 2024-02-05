# # W = 0 , B = 1
# N, M = map(int, input().split())
# Chess =[list(map(input()))for _ in range(M)]

# V = 8 #미니 체스판 크기
 
# di = [0,1,0,-1]
# dj = [1,0,-1,0]
# mincnt = 0
# for i in range(N-(V-1)):
#     for j in range(M-(V-1)):
#         now = Chess[i][j]
#         temp_cnt = 0
#         for c in range(V):
#             for r in range(V):
#                 for k in range(4):
#                     ni = i + di[k]
#                     nj = j + dj[k]
#                     if 0<=ni<N and 0<=nj<N and Chess[ni][nj] == Chess[i][j]:
#                         Chess[ni][nj] = 1-(Chess[ni][nj])
#                         temp_cnt += 1
#                 if temp_cnt < mincnt :
#                     mincnt = temp_cnt
# for row in Chess:
#     print(*row)
# print(mincnt)

CB1 = [
    'WBWBWBWB', 
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB'
       ]
CB1 = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'WBWBWBWB'
       ]

N, M = map(int, input().split())
Chess =[list(map(input()))for _ in range(M)]
cnt = 0
for i in range(N-(8-1)):
    for j in range(M-(8-1)):
        tmp_cnt = 0
        tmp_min = 100
        if Chess[i:i+8][j:j+8] != CB1[i:i+8][j:j+8]:
            tmp_cnt += 1
            if tmp_min > tmp_cnt:
                tmp_min = tmp_cnt