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
        
V, E = map(int, input().split())
edges = []
for _ in range(E):
    s,e,c = map(int, input().split())
    edges.append([s,e,c])
edges.sort(key = lambda x : x[2])
parents = [i for i in range(V)]

costsum = 0
for s,e,c in edges:
    # 사이클이 발생하면 pass
    if findset(s) == findset(e) :
        continue
    # 사이클이 없다면 방문처리
    union(s,e)
    costsum += c
    
print(costsum)