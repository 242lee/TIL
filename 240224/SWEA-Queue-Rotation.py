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
