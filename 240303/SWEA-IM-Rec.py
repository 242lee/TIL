'''
4
....
.###
.###
....
'''
N = int(input())
check = [list(input()) for _ in range(N)]

pointList = []
answer = 'no'
for i in range(N):
    for j in range(N):
        if check[i][j] == '#':
            pointList.append([i,j])

result = 0
length = 0

if pointList:
    length = len(check[pointList[0][0]][pointList[0][1]])
for k in range(len(pointList)-1):
    if check[pointList[k][0]][pointList[k][1]] == check[pointList[k+1][0]][pointList[k+1][1]]:
        result += 1
    if result == length -1 and length == len(pointList):
        answer = 'yes'
print(answer)

print(start_i, start_j)

# if i>=1 and cnt1[i-1] != cnt1[i]:
#     cnt1[i] = 0


cnt2 = [0] * N
for j in range(N):
    tmp = []
    for i in range(N):
        tmp.append(check[i][j])
        if tmp[i] == '#':
                cnt2[j] += 1
if j>=1 and cnt2[j-1] != cnt2[j]:
    cnt2[j] = 0
print(cnt2)

