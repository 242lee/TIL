passwordKey = {
    '0': '0001101',
    '1': '0011001',
    '2': '0010011',
    '3': '0111101',
    '4': '0100011',
    '5': '0110001',
    '6': '0101111',
    '7': '0111011',    
    '8': '0110111',
    '9': '0001011', 
}

T = int(input())
for tc in range(1, T+1):
    last_i = 0
    last_j = 0

    N, M = map(int, input().split())
    Screen = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(M-1,-1,-1):
            if Screen[i][j] == '1':
                # print(i, j)
                last_i = i
                last_j = j
                break
    # print(last_i, last_j)

    password = []
    for c in range(last_j+1,-1,-7):
        Screen[last_i][c-7:c]
        temp = ''.join(Screen[last_i][c-7:c])
        for i in range(10):
            if passwordKey.get(str(i)) == temp:
                password.append(i)
    password.reverse()
    # print(password)

    oddindex = []
    evenindex = []
    for i in range(8):
        if i % 2 != 0:
            evenindex.append(password[i])
        else:
            oddindex.append(password[i])

    result = (sum(oddindex) * 3) + sum(evenindex)
    # print(result)
    if result % 10 == 0:
        print(f'#{tc}', sum(oddindex) + sum(evenindex))
    else:
        print(f'#{tc}', 0)

