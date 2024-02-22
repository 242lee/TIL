'''
1000101001
1000101111
1000101001
1000111001
1000101001
1111101111
1000101001
1111101001
1000111001
1000101002
'''
for _ in range(1, 11):
    N = 100
    tc = int(input())
    Board = [list(map(int, input().split())) for _ in range(N)]
    i = 99
    j = 0
    for k in range(N):
        if Board[i][k] == 2:
            j = k

    while i > 0:
        # 오른쪽으로
        if 0 <= j+1 < N and Board[i][j+1] == 1:
            while 0 <= j+1 < N and Board[i][j+1] == 1:
                j += 1
            i -= 1
        #왼쪽으로
        elif 0 <= j-1 < N and Board[i][j-1] == 1:
            while 0 <= j-1 < N and Board[i][j -1] == 1:
                j -= 1
            i -= 1
        else:
            i -= 1

    print(f'#{tc} {j}')