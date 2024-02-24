for tc in range(1, 11):
    calcLen = int(input())
    calcList = input()

    stack = []
    for i in range(calcLen):
        if len(stack) == 0:
            if calcList[i].isdigit():
                stack.append(calcList[i])
        elif calcList[i] == '+':
            stack.append(calcList[i+1])
            stack.append(calcList[i])
    # print(stack)

    stack2 = []
    for each in stack:
        if each.isdigit():
            stack2.append(each)
        elif each == '+':
            if len(stack2) >= 2:
                a = int(stack2.pop())
                b = int(stack2.pop())
                stack2.append(int(a+b))
    print(f'#{tc}', *stack2)