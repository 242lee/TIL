<<<<<<< HEAD
'''
1 16
0 1 0 2 1 4 1 3 4 8 4 3 2 9 2 5 5 6 5 7 7 99 7 9 9 8 9 10 6 10 3 7
'''
def dfs(i, B):
    stack = []
    visited[i] = 1
    while True:
        for next in adj[i]:
            if visited[next] == 0:
                stack.append(i)
                visited[next] = 1
                i = next
                break
        else:
            if stack:
                i = stack.pop()
            else:
                break
for _ in range(10):
    Tc, N = map(int, input().split())
    arr = list(map(int, input().split()))
    A, B = 0, 99
    visited = [0] * (100)
    adj = [[] for _ in range(100)]
    for i in range(N):
        n1, n2 = arr[2*i], arr[2*i+1]
        adj[n1].append(n2)

    dfs(A, B)
    print(f'#{Tc} {visited[B]}')
=======
'''
1 16
0 1 0 2 1 4 1 3 4 8 4 3 2 9 2 5 5 6 5 7 7 99 7 9 9 8 9 10 6 10 3 7
'''
def dfs(i, B):
    stack = []
    visited[i] = 1
    while True:
        for next in adj[i]:
            if visited[next] == 0:
                stack.append(i)
                visited[next] = 1
                i = next
                break
        else:
            if stack:
                i = stack.pop()
            else:
                break
for _ in range(10):
    Tc, N = map(int, input().split())
    arr = list(map(int, input().split()))
    A, B = 0, 99
    visited = [0] * (100)
    adj = [[] for _ in range(100)]
    for i in range(N):
        n1, n2 = arr[2*i], arr[2*i+1]
        adj[n1].append(n2)

    dfs(A, B)
    print(f'#{Tc} {visited[B]}')
>>>>>>> 6cae89679cc613ec6d76d60eb7eb98ceb0ff10a7
