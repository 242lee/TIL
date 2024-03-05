'''
[시간초과 이슈]
N = int(input())
card = list(map(int, input().split()))
M = int(input())
sg = list(map(int, input().split()))

cntList = [0] * M

for each in card:
    for i in range(M):
        if each == sg[i]:
            cntList[i] += 1
print(*cntList)
'''
N = int(input())
card = list(map(int, input().split()))
M = int(input())
sg = list(map(int, input().split()))

numdict = dict.fromkeys(sg, 0)
# print(numdict)

for each in card:
    if each in numdict:
        numdict[each] += 1

for s in sg:
    print(numdict[s], end = ' ')