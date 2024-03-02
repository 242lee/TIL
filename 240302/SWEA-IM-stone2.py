'''
5 1
0 1 0 1 0
2 2
'''
T = int(input())
for tc in range(1, T+1):
    # N 개의 돌의 초기상태
    N, M = map(int, input().split())
    wb = list(map(int, input().split()))
    # M 개의 줄에 걸쳐 i와j
    for _ in range(M):
        i, j = map(int, input().split())
        i = i - 1
        for k in range(1+j):
            if i+k < N and 0<= i-k:
                if wb[i+k] == wb[i-k]:
                    wb[i+k] = 1 - wb[i+k]
                    wb[i-k] = 1 - wb[i-k]
    print(f'#{tc}', *wb)