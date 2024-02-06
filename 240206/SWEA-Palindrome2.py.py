T = int(input())
for testcase in range(1, T+1):
    
    N, M = map(int, input().split())
    wordlist = [input() for _ in range(N)]
    #가로
    for i in range(N):
        for j in range(N-M+1):
            check = wordlist[i][j:j+M]
            if check == wordlist[::-1]:
                print(f'{testcase} {check}')

    #세로
    for j in range(N):
        for i in range(N-M+1):
            check = ''
            for k in range(M):
                check += wordlist[i+k][j]
            if check == check[::-1]:
                print(f'{testcase} {check}')
