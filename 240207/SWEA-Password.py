
for testcase in range(1,11):
    N, num = input().split()
    numList = list(map(int, str(num)))
    # print(numList)
    result = []

    for n in numList:
        if len(result) == 0 or n != result[-1]:
            result.append(n)
        elif n == result[-1]:
            result.pop()
            
    result_str = ''.join(map(str, result))
    print(f'#{testcase} {result_str}')