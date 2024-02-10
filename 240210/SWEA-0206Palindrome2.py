T = int(input())
for testcase in range(1, T+1):

    N, M = map(int, input().split())
    Board = [input() for _ in range(N)]
    
    result = ''

    #가로
    for i in range(N):
        for j in range(N-(M-1)):
            if Board[i][j:j+M] == Board[i][j:j+M][::-1]:
                result += Board[i][j:j+M]

    #세로
    for j in range(N):
        for i in range(N-(M-1)):
            check = ''
            for k in range(M):
                check += Board[i+k][j]
            if check == check[::-1]:
                result += check

    print(f'#{testcase} {result}')