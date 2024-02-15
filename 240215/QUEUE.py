# qqq = []
# qqq.append(1)
# qqq.append(2)
# qqq.append(3)
# # print(Queue.pop(0))
# # print(Queue.pop(0))
# # print(Queue.pop(0))

# while qqq:
#     print(qqq.pop(0))

# --------------------------------------

# Queue 생성
N = 10
qqq = [0] * N
front = rear = -1

# enQueue
rear += 1
qqq[rear] = 10
rear += 1
qqq[rear] = 20
rear += 1
qqq[rear] = 30
print(qqq)

# deQueue
while front != rear:
    front += 1
    print(qqq[front])