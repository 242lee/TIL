def dfs(i, V):
    visited = [0] * (V+1)
    stack = []
    visited[i] = 1
    print(i) #방문한 지점 출력
    while True:
        #현재 방문한 점에서 인접한 점 중 방문하기 전인 점이 있으면
        for w in adjl[i]: #현재 방문 i
            if visited[w] == 0:
                stack.append(i) #i를 지나서 w에 방문하겠다
                i = w
                visited[i] = 1 #방문표시 남기기
                print(i) #방문한 부분 출력
                break
        else: #i에 남은 인접 정점이 없으면
            #어디서 왔는지 가
            #지나온 곳이 있으면 (stack이 비어있지 않으면)
            if len(stack) != 0:
                #하나 꺼내
                i = stack.pop()
            else: #정점이 출발점까지 돌아가고 남은 것이 없으면
                break

V, E = map(int, input().split())
arr = list(map(int, input().split()))
print(arr)

adjl = [[] for _ in range(V+1)]

for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)
print(adjl)

dfs(1, V)