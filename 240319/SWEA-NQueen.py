'''
N * N 보드에서 N 개의 Queen을 놓는 방법
좌우 대각선에 퀸이 있으면 안 됨
'''
def f(i, N):
    global cnt
    if i == N:
        cnt += 1
        return
    # i 행에 퀸을 놓는 조건
    # j 열에 다른 퀸이 없어야 함 +  대각선에도 있으면 안 돼
    for j in range(N):
        if check(i, j, N): # 놓을 수 있으면
            board[i][j] = 1
            f(i+1, N)
            board[i][j] = 0
            
def check(i, j, N):
    di = [-1,-1,-1]           
    dj = [-1,0,1] 
    for k in range(3):
        ni, nj = i+di[k], j+dj[k]
        # 이동하다가 다른 퀸을 만나면 이 경우는 아니야
        while 0 <= ni < N and 0 <= nj < N:
            if board[ni][nj]:
                return False
        ni += di[k]
        nj += dj[k]
    return True
    
        
N = int(input())
board = [[0] * N for _ in range(N)]
cnt = 0
f(0, N)
print(cnt)