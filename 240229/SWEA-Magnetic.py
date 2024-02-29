def ccnt(j):
    cnt = 0
    is_red = False
    for i in range(T):
        if Board[i][j] == 1 :
            is_red = True
        elif is_red and Board[i][j] == 2:
            cnt += 1
            is_red = False
    return cnt

# 1 = N(red), 2 = S(blue)
for tc in range(1, 11):
    T = int(input())
    Board = [list(map(int, input().split())) for _ in range(T)]
    totalcnt = 0
    for j in range(T):
        totalcnt += ccnt(j)
    print(totalcnt)
