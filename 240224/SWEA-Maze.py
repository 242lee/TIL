<<<<<<< HEAD
di = [0,1,0,-1]
dj = [1,0,-1,0]
def findroute(i, j):
    stack = []
    while True: 
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if Maze[ni][nj] == 0:
                    stack.append((i,j))
                    #방문표시
                    Maze[ni][nj] = -1
                    i = ni
                    j = nj
                    # 처음으로 돌아가도록
                    break
                if Maze[ni][nj] == 3:
                    return 1
        # 방문 경로가 더 이상 없으면
        else:
            if stack:
                i, j = stack.pop()
            else:
                break
    return 0
T = int(input())
for tc in range(1, T+1):         
    N = int(input())
    Maze = [list(map(int, input())) for _ in range(N)]
    start_i = 0
    start_j = 0
    for i in range(N):
        for j in range(N):
            if Maze[i][j] == 2:
                start_i = i
                start_j = j
    print(f'#{tc} {findroute(start_i, start_j)}')
=======
di = [0,1,0,-1]
dj = [1,0,-1,0]
def findroute(i, j):
    stack = []
    while True: 
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if Maze[ni][nj] == 0:
                    stack.append((i,j))
                    #방문표시
                    Maze[ni][nj] = -1
                    i = ni
                    j = nj
                    # 처음으로 돌아가도록
                    break
                if Maze[ni][nj] == 3:
                    return 1
        # 방문 경로가 더 이상 없으면
        else:
            if stack:
                i, j = stack.pop()
            else:
                break
    return 0
T = int(input())
for tc in range(1, T+1):         
    N = int(input())
    Maze = [list(map(int, input())) for _ in range(N)]
    start_i = 0
    start_j = 0
    for i in range(N):
        for j in range(N):
            if Maze[i][j] == 2:
                start_i = i
                start_j = j
    print(f'#{tc} {findroute(start_i, start_j)}')
>>>>>>> 6cae89679cc613ec6d76d60eb7eb98ceb0ff10a7
            