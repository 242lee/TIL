# 최소 신장 트리 - kruskal
def findset(X):
    if parents[X] == X:
        return X
    parents[X] = findset(parents[X])
    return parents[X]

def union(X,Y):
    X = findset(X)
    Y = findset(Y)
    if X == Y:
        return
    if X < Y :
        parents[Y] = X
    else:
        parents[X] = Y
T = int(input())
for tc in range(1, T+1):        
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        s,e,c = map(int, input().split())
        edges.append([s,e,c])
    edges.sort(key = lambda x : x[2])
    parents = [i for i in range(V+1)]

    costsum = 0
    for s,e,c in edges:
        if findset(s) == findset(e) :
            continue
        union(s,e)
        costsum += c
        
    print(f'#{tc} {costsum}')