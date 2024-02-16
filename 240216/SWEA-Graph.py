def bfs(S,G):
    q = []
    q.append(S)
    count[S] = 1

    while q:
        t = q.pop(0)
        if t == G:
            return count[G] -1
        for i in adlist[t]:
            if count[i] == 0:
                q.append(i)
                count[i] = count[t] + 1
    return 0

T= int(input())
for testcase in range(1, T+1):
    V, E = map(int, input().split())
    adlist = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        adlist[n1].append(n2)
        adlist[n2].append(n1)
    count = [0] * (V+1)    
    S, G = map(int, input().split())

    print(f'#{testcase} {bfs(S,G)}')