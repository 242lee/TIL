#dictionary 로 풀어보기

T = int(input())
for testcase in range(1, T+1):
    str1 = input()
    str2 = input()

    mydict = {}

    for i in set(str1):
        mydict[i] = 0
    for i in str2:
        if i in set(str1):
            mydict[i] += 1

    maxcnt = 0
    for cnt in mydict.values():
        if maxcnt < cnt:
            maxcnt = cnt

    print(f'#{testcase} {maxcnt}')
