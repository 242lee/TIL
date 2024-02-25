<<<<<<< HEAD
T = int(input())
for tc in range(1, T+1):
    check = list(map(str, input()))
    stack = []

    for s in check:
        if len(stack) == 0 or s != stack[-1]:
            stack.append(s)
        elif s == stack[-1]:
            stack.pop()
        # print(stack)

=======
T = int(input())
for tc in range(1, T+1):
    check = list(map(str, input()))
    stack = []

    for s in check:
        if len(stack) == 0 or s != stack[-1]:
            stack.append(s)
        elif s == stack[-1]:
            stack.pop()
        # print(stack)

>>>>>>> 6cae89679cc613ec6d76d60eb7eb98ceb0ff10a7
    print(f'#{tc} {len(stack)}')