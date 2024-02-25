<<<<<<< HEAD
def dfs(i, V):
    stack = []
    visited[i] = 1 #방문표시
    while True:
        for j in adj[i]:
            if visited[j] == 0:
                stack.append(i)
                i = j
                visited[i] = 1
                break
        else:
            if len(stack) != 0:
                i = stack.pop()
            else:
                break
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # E 개의 줄에 걸쳐 간선 정보다 주어짐
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    visited = [0] * (V+1)

    adj = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = arr[i][0], arr[i][1]
        adj[n1].append(n2)
    # print(adj)
    dfs(S, V)
    print(f'#{tc} {visited[G]}')
=======
def dfs(i, V):
    stack = []
    visited[i] = 1 #방문표시
    while True:
        for j in adj[i]:
            if visited[j] == 0:
                stack.append(i)
                i = j
                visited[i] = 1
                break
        else:
            if len(stack) != 0:
                i = stack.pop()
            else:
                break
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # E 개의 줄에 걸쳐 간선 정보다 주어짐
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    visited = [0] * (V+1)

    adj = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = arr[i][0], arr[i][1]
        adj[n1].append(n2)
    # print(adj)
    dfs(S, V)
    print(f'#{tc} {visited[G]}')
>>>>>>> 6cae89679cc613ec6d76d60eb7eb98ceb0ff10a7
