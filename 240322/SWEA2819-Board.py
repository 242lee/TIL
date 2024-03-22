'''
격자판 -> 이차원 배열
4방향 이동 -> 델타 탐색 고
단순 재귀
1
1 1 1 1
1 1 1 2
1 1 2 1
1 1 1 1
-> 23
'''
di = [0,1,0,-1]
dj = [1,0,-1,0]

def dfs(i, j, path):
    # 7자리가 되면 종료
    if len(path) == 7:
        # 현재까지의 경로 저장
        result.add(path)
        return
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        
        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(ni, nj, path + board[ni][nj])
    
T = int(input())
for tc in range(1, T+1):
    board = [input().split() for _ in range(4)]
    result = set()      # 결과는 중복 제거
    for i in range(4):
        for j in range(4):
            dfs(i, j, board[i][j])
    print(f'#{tc} {len(result)}')
