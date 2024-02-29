check = input()
stack = [check[0]]
N = len(check)
cnt = 0
for i in range(1, N):
    if check[i] == ')':
        if check[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
    else:
        stack.append(check[i])
print(cnt)