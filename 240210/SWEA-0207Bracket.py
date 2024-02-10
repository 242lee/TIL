T = int(input())
for testcase in range(1, T+1):
    str1 = input()
    result = []
    for i in str1:
        if i in '({})':
            if len(result) == 0:
                result.append(i)
            elif i == '(' or i == '{':
                result.append(i)
            elif i == ')':
                if result[-1] == '(' :
                    result.pop()
                else:
                    result.append(i)
            elif i == '}':
                if result[-1] == '{' :
                    result.pop()
                else:
                    result.append(i)     

    if len(result) == 0:
        print(f'#{testcase} 1')
    else:
        print(f'#{testcase} 0')