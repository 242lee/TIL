def pre(T):
    if T: # T에 방문했으면
        print(T)
        pre(left[T])
        pre(right[T])


N = int(input())
E = N - 1 # 간선의 수
arr = list(map(int, input().split()))
left = [0] * (N+1)
right = [0] * (N+1)
parent = [0] * (N+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if left[p] == 0: # 왼쪽 자식이 없으면
        left[p] = c
    else:
        right[p] = c
    parent[c] = p
'''
print(parent)   [0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 7, 11]
print(left)     [0, 2, 4, 5, 7, 8, 10, 12, 0, 0, 0, 13, 0, 0]
print(right)    [0, 3, 0, 6, 0, 9, 11, 0, 0, 0, 0, 0, 0, 0]
'''

# 트리의 루트 찾기
c = N
while parent[c] != 0: # 더이상 부모가 없을 때까지
    c = parent[c] # 다시 부모가 자식이 되어서 탐색 
root = c
# print(root)
# 순회 순서
pre(root)

'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''