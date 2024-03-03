'''
()(((()())(())()))(())
17
'''
T = int(input())
for tc in range(1, T+1):
    pipe = list(input())
    N = len(pipe)
    stack = []
    cnt = 0
    for i in range(N):
        if pipe[i] == '(':
            stack.append(pipe[i])
        elif pipe[i] == ')':
            # 레이저
            if pipe[i-1] == '(' :
                stack.pop()
                cnt += len(stack)
            # 그냥 막대 끝
            else:
                stack.pop()
                cnt += 1
    print(f'#{tc} {cnt}')
