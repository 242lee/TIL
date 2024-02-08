T = int(input())

for testcase in range(1, T+1):
    N, M = map(int, input().split())
    Arr = [input() for _ in range(N)]

    #가로
    result = []
    for i in range(N):
        for j in range(N-M+1):
            word = Arr[i][j:j+M]
            if word == word[::-1]:
                result.append(word)

    #세로
    for i in range(N):
        for j in range(N-M+1):
            tmp = []
            for k in range(M):
                tmp.append(Arr[j+k][i])
            word = ''.join(tmp)
            if word == word[::-1]:
                result.append(word)
             
    print(f'#{testcase}', *result)