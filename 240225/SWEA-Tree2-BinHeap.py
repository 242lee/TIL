'''
6
7 2 5 3 4 6
'''
def binheap(T):
    global last
    last += 1
    heap[last] = T
    c = last
    p = c // 2
    while c > 1 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

N = int(input())
info = list(map(int, input().split()))
heap = [0] * (N+1)
last = 0
for each in info:
    binheap(each)
sum = 0
while last:
    last //= 2
    sum += heap[last]
print(sum)
