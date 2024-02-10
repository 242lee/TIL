T = int(input())
for testcase in range(1, T+1):
    str1 = input()
    str2 = input()
    strList = set(str1) #찾아야 하는 문자들

    cntmax = 0

    for alpha in strList:
        cnt = 0
        for each in str2:
            if alpha == each:
                cnt += 1
        if cntmax < cnt:
            cntmax = cnt
    print(f'#{testcase} {cntmax}')
    