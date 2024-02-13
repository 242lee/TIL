# 방향키 (우하좌상)
dr = [0,1,0,-1]
dc = [1,0,-1,0]

def dfs(r, c):
    stack = []
    while True:
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if Maze[nr][nc] == 0:
                    stack.append((r,c))
                    Maze[nr][nc] = -1
                    r = nr
                    c = nc
                    break
                elif Maze[nr][nc] == 3:
                    # print('1')
                    return 1

        else:
            if stack:
                r, c = stack.pop()
            else:
                break
    return 0
T = int(input())
for testcase in range(1, T+1):               
    N = int(input())
    Maze = [list(map(int, input())) for _ in range(N)]

    # 시작점 = Maze[r][c]
    r = 0
    c = 0
    for i in range(N):
        for j in range(N):
            if Maze[i][j] == 2:
                r = i
                c = j
    # 결과 보기
    print(f'#{testcase} {dfs(r,c)}')
