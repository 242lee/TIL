def dfs(S):
    visited[S] = 1
    stack = []
    while True:
        for j in adj[S]:
            if visited[j] == 0:
                stack.append(S)
                S = j
                visited[S] = 1
                break
        else:
            if len(stack) != 0:
                S = stack.pop()
            else:
                break
        if S == G:
            return 1
    return 0

for _ in range(10):
    testcase, pathnum = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [0] * 101
    adj = [[] for _ in range(101)]

    for i in range(pathnum):
        n1, n2 = arr[i*2], arr[i*2+1]
        adj[n1].append(n2)
        S, G = 0, 99

    print(f'#{testcase} {dfs(S)}')