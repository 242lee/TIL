T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    inputnum = str(input())
    cntList = []
    cnt = 0
    for i in range(N):
        if inputnum[i] == '1':
            cnt += 1
        else:
            cnt = 0
        cntList.append(cnt)

    print(f'#{testcase} {max(cntList)}')

