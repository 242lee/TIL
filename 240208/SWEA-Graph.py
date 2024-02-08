def dfs(i, V):
    stack = []
    visited[i] = 1 # 1에서 시작
    # print(i)
    
    while True:
        for w in adjl[i]:
            if visited[w] == 0:
                stack.append(i)
                i = w
                visited[i] = 1 # 방문표시 남기기
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
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    # print(arr)
    visited = [0] * (V+1)

    adjl = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = arr[i][0], arr[i][1]
        adjl[n1].append(n2)
    # print(adjl)

    dfs(S, V)
    print(f'#{testcase} {visited[G]}')