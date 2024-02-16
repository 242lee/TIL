# while 문이 끝나지 않는 문제가 있음.. 다시 풀어볼게..

N = 10
testcase = int(input())
laddermap = [list(input()) for _ in range(N)]
print(laddermap)
# 방향 (우하좌)
di = [0,0,1]
dj = [1,-1,0]
# 시작점 모음
startpoint = []
for k in range(N):
    if laddermap[0][k] == '1':
        startpoint.append([0,k])
print(startpoint)


for t in range(len(startpoint)):
    i, j = startpoint[t]
    print(i,j)
    while i < 9:
        for k in range(3):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                # 좌우에 1이 있는 경우
                if laddermap[ni][nj] == '1':
                    laddermap[ni][nj] = 3
                    i = ni
                    j = nj
                elif laddermap[ni][nj] == '2':
                    print(startpoint[t][1])
                    break
        break
