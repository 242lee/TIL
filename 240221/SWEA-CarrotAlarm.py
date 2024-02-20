'''
0은 땅, 밭은 1, 멧돼지는 2
'''
T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    Board = [list(map(int, input().split())) for _ in range(10)]

    point_i = []
    point_j = []
    for i in range(10):
        for j in range(10):
            if Board[i][j] == 1:
                if i not in point_i:
                    point_i.append(i)
                if j not in point_j:
                    point_j.append(j)
    # print(point_i)
    # print(point_j)

    cnt = 0
    for r in range(10):
        for c in range(10):
            if (0<=r<=int(point_i[0]) and 0<=c<=int(point_j[0])) or (0<=r<=int(point_i[0]) and int(point_j[-1])<=c<=10) or (int(point_i[-1])<=r<=10 and 0<=c<=int(point_j[0])) or (int(point_i[-1])<=r<=10 and int(point_j[-1])<=c<=10):
                if Board[r][c] == 2:
                    cnt += 1
    print(f'#{testcase} {cnt}')
