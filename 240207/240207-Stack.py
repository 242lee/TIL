def push(n):
    global top
    top += 1
    if top == size:
        print('overflow')
    else:
        stack[top] = n

top = -1
size = 10
stack = [0] * size

# 10 20 30 을 push

top += 1
stack[top] = 10
top += 1
stack[top] = 20

push(30)

while 0 <= top:
    top -= 1
    print(stack[top+1])
