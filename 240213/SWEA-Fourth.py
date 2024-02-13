T = int(input())
for testcase in range(1, T+1):
    check = input().split()
    stack = []
    for each in check:
        if each.isdigit():
            stack.append(int(each))
        elif each in '+-/*':
            if len(stack) >= 2:
                a = int(stack.pop())
                b = int(stack.pop())
                if each == '+':
                    result = b + a
                    stack.append(int(result))
                elif each == '-':
                    result = b - a
                    stack.append(int(result))
                elif each == '*':
                    result = b * a
                    stack.append(int(result))
                elif each == '/':
                    result = b / a
                    stack.append(int(result))
            else:
                print(f'#{testcase} error')
                break
        elif each == '.':
            if len(stack) == 1:
                print(f'#{testcase} {stack[-1]}')
            else:
                print(f'#{testcase} error')
                break
