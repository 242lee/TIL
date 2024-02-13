'''
(6+5*(2-8)/2)
-> 6528-*2/+
'''
fx = '(6+5*(2-8)/2)'
top = -1
stack = [0] * 100

icp = {'(':3, '*':2, '/':2, '+':1 , '-':1} #스택 밖에서 우선순위
isp = {'(':0, '*':2, '/':2, '+':1 , '-':1} #스택 안에서 우선순위

post = ''

for tk in fx:
    # 여는 괄호 push, 연산자이고, top 원소보다 우선순위가 높으면 push
    if tk == '(' or (tk in '*/+-' and isp[stack[top]] < icp[tk]):
        top += 1
        stack[top] = tk
    # 연산자인데 top 원소보다 우선순위가 낮거나 같으면
    elif (tk in '*/+-' and isp[stack[top]] >= icp[tk]):
        # top 원소의 우선순위가 낮을 때까지 pop
        while isp[stack[top]] >= icp[tk]:
            top -= 1
            post += stack[top+1]
        # push
        top += 1
        stack[top] = tk
    # 닫는 괄호가 나오면, 여는 괄호를 만날 때까지 pop
    elif tk == ')':
        while stack[top] != '(':
            top -= 1
            post += stack[top+1]
        top -= 1 # 여는 괄호 pop해서 버리기
        stack[top+1]
    # 피연산자인 경우
    else:
        post += tk
print(post)


