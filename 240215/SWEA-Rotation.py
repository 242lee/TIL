T =int(input())
for testcase in range(1, T+1):

    Qlen, Time = map(int, input().split())
    numList = list(map(int, input().split()))
    q = [0] * Qlen
    rear = 0

    for i in range(Time):
        item = numList[((i+1) % Qlen)]
        rear = (rear + 1) % Qlen
        q[rear] = item

    print(f'#{testcase} {q[rear]}')

# Qlen, Time = 3, 5
# numList = [1,3,5]
# q = [0] * Qlen
# rear = 0

# for i in range(Time):
#     item = numList[((i+1) % Qlen)]
#     rear = (rear + 1) % Qlen
#     q[rear] = item

# print(q[rear])