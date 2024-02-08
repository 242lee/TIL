def dfs(s,e):#s는 시작, e는 도착
    visited = [0] * 100
    stack = []
    visited[s] = 1
    v = s   # 현재 방문한 위치 v
    while True: #탐색 시작
        # 현재 방문위치 v랑 인접한 w
        if  A[v] != (-1) and visited[A[v]] == 0: #인접한 경우가 있고 and 방문된 적 없다면
            # v 를 push하고 (현재 위치를 저장하고) 이동
            stack.append(v)
            #이동한 후에
            v = A[v]
            #방문표시
            visited[v] = 1
        elif  B[v] != -1 and visited[B[v]] == 0:
                stack.append(v)
                v = B[v]
                visited[v] = 1
        else:    #출발지까지 거슬러와서 가능한 모든 곳을 확인한 경우
            if len(stack) != 0:
                v = stack.pop()
            else:
                break
        if v == e:
            return 1
    return 0
    
for _ in range(10):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))

    A = [-1] * 100 # A[i] i 에 인접한 도시번호
    B = [-1] * 100 # B[i] i 에 인접한 도시번호

    for i in range(0, E*2, 2):
        n1, n2 = arr[i], arr[i+1]
        if A[n1] == -1:
            A[n1] = n2
        else:
            B[n1] = n2

dfs(0,99)