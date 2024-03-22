
def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


T = int(input())
for tc in range(1, T+1):
    # N은 사람 수, M은 관계 수
    N, M = map(int, input().split())
    parents = [i for i in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        union(a,b)
    cnt = 0
    # 대표 다시 한 번 확인
    for i in range(1,N+1):
        if i == parents[i]:
            cnt+=1
    print(f'#{tc} {cnt}')