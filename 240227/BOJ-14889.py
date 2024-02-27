N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

index = [i+1 for i in range(N)]
result = []
tmpresult = []
visited = [0] * (N+1)

def si(T):
    if  T == N:
        if tmpresult[::-1] not in result:
            result.append(tmpresult[:])
            return
    for i in range(1, N+1):
        if visited[i] == 0:
            tmpresult.append(i)
            visited[i] = 1
            si(T+1)
            tmpresult.pop()
            visited[i] = 0
si(0)
for r in result:
    print(r)

K = int(len(result))
L = int(len(result[0])/2)
min_di = 100000000
for i in range(K):
    now = result[i]
    start = result[i][:L]
    link  = result[i][L:]
    startSkill = 0
    linkSkill = 0
    # print(start, link)
    for j in range(L-1):
        startSkill += S[start[j]-1][start[j+1]-1]
        startSkill += S[start[j+1]-1][start[j]-1]
        linkSkill += S[link[j]-1][link[j+1]-1]
        linkSkill += S[link[j+1]-1][link[j]-1]
    di = abs(startSkill - linkSkill)
    if min_di > di:
        min_di = di
print(min_di)