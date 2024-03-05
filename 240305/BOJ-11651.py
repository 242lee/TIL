N = int(input())
pList = []
for _ in range(N):
    pList.append(list(map(int, input().split())))

pList.sort(key= lambda x : (x[1], x[0]))
for p in pList:
    print(*p)