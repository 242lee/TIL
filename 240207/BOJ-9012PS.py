# 괄호 짝 확인하기
N = int(input())
for n in range(N):
    stack = []
    check = input() #확인할 문자열
    for i in check:
        #왼쪽 괄호를 만나면 스택에 추가
        if i == '(':
            stack.append(i)
        #오른쪽 괄호를 만나면 스택에서 팝
        elif i == ')':
            #empty list에서 팝 할 수 없으므로 길이 제한
            if len(stack) > 0:
                stack.pop()
            else:
                #마지막 len(stack)을 0 으로 만들지 않기 위해 남은 걸 append
                stack.append(i)
                break
            
    #for문을 다 돌고 난 후의 stack길이가 0 이면 짝이 잘 맞는 거
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')

N = int(input())
for n in range(N):
    stack = []
    check = input()
    for i in check:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                stack.append(i)
                break
            
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')