def findset(x):
    # 자기가 대표면
    if parent[x] == x:
        return x
    return findset(parent[x])

def union(a,b):
    a = findset(a)
    b = findset(b)
    if a == b:
        return
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
        
T = int(input()) 
for tc in range(1, T+1):      
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    parent = [i for i in range(N+1)]
    for i in range(M):
        a = arr[i*2]
        b = arr[i*2+1]
        union(a,b)
        
    cnt = 0
    for i in range(1,N+1):
        if i == parent[i]: # 대표가 여전히 자신인지 확인!!
            cnt+=1
 
    print(f'#{tc} {cnt}')
