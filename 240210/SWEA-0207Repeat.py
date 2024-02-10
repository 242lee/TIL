T = int(input())
for testcase in range(1, T+1):
    strinput = input()
    strList = list(map(str, strinput))
    result = []

    for s1 in strList:
        if len(result) == 0 or s1 != result[-1]:
            result.append(s1)
        elif s1 == result[-1]:
            result.pop()

    cnt = 0
    for s2 in result:
        cnt += 1
    print(f'#{testcase} {cnt}')