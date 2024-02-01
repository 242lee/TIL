N = 5

di = [0,1,0,-1]
dj = [1,0,-1,0] 

i = 3
j = 4

for i in range(N):
	for j in range(N):
		for k in range(4):
			ni = i + di[k]
			nj = j + dj[k]
			if 0<= ni <N and 0 <=nj<N:
				print(ni, nj, end = ' ')
		print()
