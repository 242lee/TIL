def dfs(i, V):# V 노드 몇 개
    stack = []
    visited[i] = 1
    # print(i)
    while True:
        for next in adj[i]:
            if visited[next] == 0:
                stack.append(i)
                i = next
                visited[i] = 1
                # print(i)
                break
        else:
            if len(stack) != 0:
                i = stack.pop()
            else:
                break

T = int(input())
for testcase in range(1, T+1):
    V, E = map(int, input().split())
    # V개 노드, E개의 줄에 걸쳐서 제공
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    # 빈 배열
    adj = [[] for _ in range(V+1)]
    visited = [0] * (V+1)

    for i in range(E):
        n1, n2 = arr[i][0], arr[i][1]
        adj[n1].append(n2)
    # print(adj)

    dfs(S,V)
    print(f'#{testcase} {visited[G]}')
