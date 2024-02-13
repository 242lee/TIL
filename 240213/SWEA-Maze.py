N = int(input())
Maze = [input() for _ in range(N)]

# 시작점 = Maze[r][c]
r = 0
c = 0
for i in range(N):
    for j in range(N):
        if Maze[i][j] == '2':
            r = i
            c = j

# 방향키 (우하좌상)
dr = [0,1,0,-1]
dc = [1,0,-1,0]

# 길 찾기 시작
find = 0
for r in range(N):
    for c in range(N):
        while True:
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0<=nr<N and 0<=nc<N:
                    if Maze[nr][nc] == '0':
                        r = nr
                        c = nc
                    if Maze[nr][nc] == '3':
                        find = 1
                        break
print(find)




            