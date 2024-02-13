for testcase in range(1, 11):
    lenlist = int(input())
    calcList = input()

    # 후위표기식으로 바꾸기
    stack = []
    for i in range(len(calcList)):
        if len(stack) == 0:
            if calcList[i].isdigit():
                stack.append(calcList[i])
        elif calcList[i] == '+':
            stack.append(calcList[i+1])
            stack.append(calcList[i])
    # print(''.join(stack))

    #계산하기
    stack2 = []
    for each in stack:
        if each.isdigit():
            stack2.append(each)
        elif each == '+' :
            if len(stack2) >= 2:
                a = int(stack2.pop())
                b = int(stack2.pop())
                if each == '+':
                    result = b + a
                    stack2.append(int(result))
    print(f'#{testcase}',*stack2)