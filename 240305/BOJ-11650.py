'''
5
3 4
1 1
1 -1
2 2
3 3
'''
N = int(input())
pList = []
for _ in range(N):
    pList.append(list(map(int, input().split())))

pList.sort(key= lambda x : (x[0], x[1]))
for p in pList:
    print(*p)