# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
# #[[123], [456], [789]]


# arr2 = [[0]*N for _ in range(N)]
# print(arr2)
# #[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# for i in range(3):  #아래로
#     for j in range(4): #오른쪽으로
#         f(array[i][j])

#------------------------------------------------

	#방향 0, 1, 2, 3
# di = [0,1,0,-1] #방향별로 더할 값
# dj = [1,0,-1,0] 

# i = 3
# j = 4

# for k in range(4):
# 	ni = i + di[k]
# 	nj = j + dj[k]
# 	print(ni, nj)
#------------------------------------------------

# N = 5

# arr = [[0]*N for _ in range(N)]

# di = [0,1,0,-1]
# dj = [1,0,-1,0] 

# i = 3
# j = 4

# for i in range(N):
# 	for j in range(N):
# 		for k in range(4):
# 			ni = i + di[k]
# 			nj = j + dj[k]
# 			if 0<= ni <N and 0 <=nj<N:
# 				print(arr[ni][nj], end = '')
# 		print()

# ----------------------------------------

N = 5
di = [0,1,0,-1]
dj = [1,0,-1,0] 

arr = [[0]*N for _ in range(N)]
for i in range(N):
	for j in range(N):
		for k in range(4):
			ni = i + di[k]
			nj = j + dj[k]
			if 0<= ni <N and 0 <=nj<N:
				print(arr[ni][nj], end = '')