def omok(y, x):
    dy = [1,0,1,-1]
    dx = [0,1,1,1]
    
    for way in range(4):
        cnt = 1
        for distance in range(1, 5):
            ny = y + (dy[way] * distance)
            nx = x + (dx[way] * distance)
            if not (0 < ny <= N and 0 < nx <= N): break
            if arr[ny][nx] =='o': cnt += 1

            if cnt == 5:
                return True
    return False

def gameStart():
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o':
                if omok(r,c):
                    return 'YES'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    result = gameStart()
    print(result)