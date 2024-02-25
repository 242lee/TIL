for tc in range(1, 11):
    N = int(input())
    calcList = input()
    priority = {'*':2, '+':1}
    stack = []
    postfix = []
    top = -1

    for i in range(N):
        # 1. 연산자인 경우
        if calcList[i] in '+*' and stack:
            if priority[calcList[i]] > priority[stack[top]]:
                stack.append(calcList[i])
                top += 1
            else:
                while top >= 0 and priority[calcList[i]] <= priority[stack[top]]:
                    top -= 1
                    item = stack.pop()
                    postfix.append(item)
                top += 1
                stack.append(calcList[i])
        elif calcList[i] in '*+' and len(stack) == 0:
            stack.append(calcList[i])
            top += 1
        else: # 2. 숫자인 경우
            postfix.append(calcList[i])
    while stack:
        postfix.append(stack.pop())

    stack2 = []
    for now in postfix:
        if now.isdigit():
            stack2.append(now)
        else:
            if len(stack2) >= 2:
                a = int(stack2.pop())
                b = int(stack2.pop())
                if now == '+':
                    stack2.append(a+b)
                elif now == '*':
                    stack2.append(a*b)
    print(f'#{tc}', *stack2)