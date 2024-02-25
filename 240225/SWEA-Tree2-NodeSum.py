'''
5 3 2
4 1
5 2
3 3
'''
def leafsum(T):
    c1 = 2 * T
    c2 = 2 * T + 1
    if c1 <= N:
        if c2 <= N:
            return leafsum(c1) + leafsum(c2)
        else: return leafsum(c1)
    else: return heap[T]
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    info = [list(map(int, input().split()))for _ in range(M)]
    heap = [0] * (N+1)
    for each in info:
        i, heap[i] = each[0], each[1]
    # print(heap)
    print(f'#{tc} {leafsum(L)}')