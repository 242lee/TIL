
def orderHeap(T):
    global last
    last += 1
    heap[last] = T
    c = last
    p = c//2 
    while c > 1 and (heap[p] > heap[c]):
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    numList = list(map(int, input().split()))
    heap = [0] * (N+1)
    last = 0

    for num in numList:
        orderHeap(num)
    sum = 0
    while last:
        last //= 2
        sum += heap[last]
    # print(heap)
    print(f'#{testcase} {sum}')
