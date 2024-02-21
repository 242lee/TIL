T= int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Board = [list(map(int, input().split())) for _ in range(N)]
    deathMax = 0
    for i in range(N-(M-1)):
        for j in range(N-(M-1)):
            death = 0
            for p in range(i, i+M):
                for q in range(j, j+M):
                    death += Board[p][q]
            if deathMax < death:
                deathMax = death
    print(f'#{tc} {deathMax}')