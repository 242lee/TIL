<<<<<<< HEAD
T = int(input())
for tc in range(1, T+1):
    N, Time = map(int, input().split())
    arr = list(map(int, input().split()))
    q = [0] * N
    rear = 0

    for i in range(1, Time+1):
        item = arr[(i) % N]
        # print(item)
        rear = (rear + 1) % N
        q[rear] = item

    print(f'#{tc} {q[rear]}')
=======
T = int(input())
for tc in range(1, T+1):
    N, Time = map(int, input().split())
    arr = list(map(int, input().split()))
    q = [0] * N
    rear = 0

    for i in range(1, Time+1):
        item = arr[(i) % N]
        # print(item)
        rear = (rear + 1) % N
        q[rear] = item

    print(f'#{tc} {q[rear]}')
>>>>>>> 6cae89679cc613ec6d76d60eb7eb98ceb0ff10a7
