V, E = map(int, input().split())
arr = list(map(int, input().split()))
print(arr)

adjl = [[] for _ in range(V+1)]
print(adjl)
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)
print(adjl)

# dfs(1, V)