T = int(input())
for testcase in range(1, T+1):
        
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_death = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            death = 0

            for k in range(M):
                for l in range(M):

                    death += arr[i+k][j+l]

                    
                if max_death <= death:
                    max_death = death

    print(f'#{testcase} {max_death}')
