def pascal(N):
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if j <=  0:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
            
            if arr[i][j]:
                print(arr[i][j], end =' ')
        print()

T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    print(f'#{testcase}')
    pascal(N)
