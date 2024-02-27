def combi(i, N):
    if len(cList) == N:
        situation.append(cList[:])
        return
    for j in range(1, N):
        if visited[j] == 0:
            cList.append(j+1)
            visited[j] = 1
            combi(i+1, N)
            cList.pop()
            visited[j] = 0

T = int(input())
for tc in range(1, T+1):    
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]
    P = [i for i in range(N)]
    visited = [0] * N
    cList = [1]
    situation = []
                
    combi(0,N)
    # print(situation)

    min_energy = 50 ** 3
    for each in situation:
        tmpsum = 0
        # print(each)
        for k in range(0, len(each)-1):
            i = each[k]-1
            j = each[k+1]-1
            # print(e[i][j])
            tmpsum += e[i][j]
        tmpsum += e[each[-1]-1][0]
        # print(tmpsum)
        if min_energy > tmpsum:
            min_energy = tmpsum
    print(f'#{tc} {min_energy}')