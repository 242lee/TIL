T = int(input())
for testcase in range(1, T+1):
    stack = []
    check = input() #확인할 문자열
    for i in check:
        # '('나 '{' 를 만나면 stack에 추가
        if i in '{(':
            stack.append(i)
        elif i == ')':
            if len(stack) > 0:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    break
            else:
                stack.append(i)

        elif i == '}':
            if len(stack) > 0:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    break
            #')()'와 같이 오른쪽 괄호를 먼저 입력했을 때 stack에 추가하여 길이가 0이 되지 않게 해야 함
            else:
                stack.append(i)
                    
    if len(stack) == 0:
        print(f'#{testcase} 1')
    else:
        print(f'#{testcase} 0')