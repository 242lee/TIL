# 한시, 세시, 다섯시, 여섯시 방향
di = [-1,0,1,1]
dj = [1,1,1,0]

def omok():
    for i in range(N):
        for j in range(N):
            for k in range(4):
                for r in range(5):
                    ni = i + di[k] * r
                    nj = j + dj[k] * r
                    if 0 <= ni < N and 0 <= nj < N and Board[ni][nj] == 'o':
                        pass
                    else:
                        break
                else:
                    return 'YES'
    return 'NO'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Board = [list(input()) for _ in range(N)]
    result = omok()
    print(f'#{tc} {result}')
