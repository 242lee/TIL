'''
4
....
.###
.###
....
'''
N = int(input())
check = [list(input()) for _ in range(N)]

start_i = start_j = 0
for i in range(N):
    for j in range(N):
        if check[i][j] == '#':
            start_i, start_j = i,j
            break
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

