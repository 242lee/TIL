
T = int(input())

di = [0,1,0,-1]
dj = [1,0,-1,0]

for testcase in range(1, T+1):
	N, M = map(int, input().split())
	arr = [list(map(int, input().split())) for _ in range(N)]
	max_v = 0 #종이 꽃가루 합계
	
	for i in range(N):
		for j in range(M):
			cnt = arr[i][j]
			for k in range(4):
				ni = i + di[k]
				nj = j + di[k]

				if 0<= ni < N and 0<= nj < M:
					cnt += arr[ni][nj]

			#꽃가루 최대값과 비교
			if max_v <= cnt:
				max_v = cnt
	print(max_v)