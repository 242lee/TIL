def nodecnt(T):
    global cnt
    if T:
        nodecnt(leftchild[T])
        nodecnt(rightchild[T])
        cnt += 1

T = int(input())
for testcase in range(1, T+1):
    # 노드 1을 루트로 하는 서브트리에 속한 노드 개수 알아내기
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    parent = [0] * (E+2)
    leftchild = [0] * (E+2)
    rightchild = [0] * (E+2)
    cnt = 0
    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        parent[c] = p
        if leftchild[p] == 0:
            leftchild[p] = c
        else:
            rightchild[p] = c
    nodecnt(N)
    print(f'#{testcase} {cnt}')
'''
5 1
2 1 2 5 1 6 5 3 6 4 

print(parent)       [0, 2, 0, 5, 6, 2, 1]
print(leftchild)    [0, 6, 1, 0, 0, 3, 4]
print(rightchild)   [0, 0, 5, 0, 0, 0, 0]
'''
    
