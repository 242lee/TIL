<<<<<<< HEAD
T = int(input())
for tc in range(1, T+1):
    inputList = input().split()
    stack = []

    for each in inputList:
        if each.isdigit():
            stack.append(each)
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
                print(f'#{tc} error')
                break
        elif each == '.':
            if len(stack) == 1:
                print(f'#{tc}', *stack)
            else:
                print(f'#{tc} error')
    # print(inputList)
    # print(stack)

=======
T = int(input())
for tc in range(1, T+1):
    inputList = input().split()
    stack = []

    for each in inputList:
        if each.isdigit():
            stack.append(each)
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
                print(f'#{tc} error')
                break
        elif each == '.':
            if len(stack) == 1:
                print(f'#{tc}', *stack)
            else:
                print(f'#{tc} error')
    # print(inputList)
    # print(stack)

>>>>>>> 6cae89679cc613ec6d76d60eb7eb98ceb0ff10a7
