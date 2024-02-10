for testcase in range(1, 11):
    n, numinput = input().split()
    password = list(map(int,str(numinput)))
    result = []

    for i in password:
        if len(result) == 0 or i != result[-1]:
            result.append(i)
        elif i == result[-1]:
            result.pop()

    str1 = ''.join(map(str, result))
    print(f'#{testcase} {str1}')