numList = '3+3*8+2*7'
N = len(numList)

priority = {'*':2, '+':1}
stack = []
top = -1
postfix =[]

for i in range(N):

    if numList[i] in '*+' and len(stack) != 0:
        if priority[stack[top]] < priority[numList[i]]:
            stack.append(numList[i])
            top += 1
        else:
            while top >= 0 and priority[stack[top]] >= priority[numList[i]]:
                top -= 1
                elem = stack.pop()
                postfix.append(elem)
            top += 1
            stack.append(numList[i])
    
    elif numList[i] in '+*' and len(stack) == 0:
        stack.append(numList[i])
        top += 1
    else:
        postfix.append(numList[i])
while len(stack) > 0 :       
    postfix += stack.pop()


stack2 = []
for each in postfix:
    if each.isdigit():
        stack2.append(each)
    elif each in '+*':
        if len(stack2) >= 2:
            a = int(stack2.pop())
            b = int(stack2.pop())
            if each == '+':
                stack2.append(int(a + b))
                # print(stack2)
            elif each == '*':
                stack2.append(int(a * b))
                # print(stack2)

print(*stack2)