T = int(input())
for testcase in range(1, T+1):
    N = int(input())

    tri = [[0] * N for _ in range(N)]
    tri[0][0] = 1
    print(f'#{testcase}')

    for i in range(N):
        for j in range(N):
            if j == 0:
                tri[i][j] = 1
            else:
                tri[i][j] = tri[i-1][j-1] + tri[i-1][j]
            if tri[i][j]:
                print(tri[i][j], end = ' ')
        print()