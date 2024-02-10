for testcase in range(1, 11):
    F = int(input())

    Board = [input() for _ in range(8)]

    #가로
    cnt = 0
    for i in range(8):
        for j in range(8-(F-1)):
            if Board[i][j:j+F] == Board[i][j:j+F][::-1]:
                cnt += 1

    #세로
    for j in range(8):
        for i in range(8-(F-1)):
            check = ''
            for k in range(F):
                check += Board[i+k][j]
            if check == check[::-1]:
                cnt += 1

    print(f'#{testcase} {cnt}')