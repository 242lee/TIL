'''
이진 힙
부모노드 < 자식 노드의 조건이 있고, 이에 맞지 않는 경우
조건을 만족할 때까지 부모 노드와 값을 바꾼다.
6
7 3 5 2 4 6
'''
def orderHeap(T):
    global last
    last += 1
    heap[last] = T
    c = last
    p = c//2
    while c > 1 and (heap[p] > heap[c]):
        heap[c], heap[p] = heap[p], heap[c]
        c = p
        p = c//2
        
N = int(input())
numList = list(map(int, input().split()))
heap = [0] * (N+1)
last = 0
for num in numList:
    orderHeap(num)
numsum = 0
while last:
    last //= 2
    numsum += heap[last]
print(heap)
print(numsum)